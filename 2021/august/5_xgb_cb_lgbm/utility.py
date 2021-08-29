import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import optuna
import lightgbm as lgbm
import catboost as cb
import xgboost as xgb
from sklearn.model_selection import (
    cross_validate, KFold, train_test_split, StratifiedKFold
)
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, log_loss
from sklearn.compose import ColumnTransformer, make_column_transformer, make_column_selector
from sklearn.pipeline import make_pipeline, Pipeline
import joblib
import logging
import time

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
SEED = 1121218
N_BOOST = 20000


# class MasterTask:
#     def __init__(self, data_path: str, data_name: str, target: str, task_type: str):
#         self.models = []

class Data:
    def __init__(self, data_path: str, data_name: str, target: str):
        self.df = pd.read_csv(data_path)
        self.name = data_name
        self.X = self.df.drop(target, axis=1)
        self.y = self.df[[target]].values.flatten()

        # Get categorical features and extract their indices
        cat_names = self.X.select_dtypes(exclude=np.number).columns.tolist()
        cat_idx = [self.X.columns.get_loc(col) for col in cat_names]
        self.categoricals = cat_idx
        self.has_missing = True if self.X.isnull().sum().sum() > 0 else False
        self.shape = self.X.shape


class XGBTask:
    def __init__(self, data_path: str, data_name: str, target: str, task_type: str):
        self._data = Data(data_path, data_name, target)
        self.task_type = task_type

        kf = KFold(n_splits=7, shuffle=True, random_state=SEED)
        strat_kf = StratifiedKFold(n_splits=7, shuffle=True, random_state=SEED)
        self._cv = kf if task_type == 'regression' else strat_kf

    @property
    def _preprocessed_data(self):
        num_pipeline = make_pipeline(SimpleImputer(strategy='constant', fill_value=-9999))
        cat_pipeline = make_pipeline(SimpleImputer(strategy='most_frequent'),
                                     OneHotEncoder(handle_unknown='ignore', sparse=False))
        full_pipe = ColumnTransformer(transformers=[
            ('num_pipe', num_pipeline, make_column_selector(dtype_include=np.number)),
            ('cat_pipe', cat_pipeline, make_column_selector(dtype_exclude=np.number))
        ])
        X = full_pipe.fit_transform(self._data.X)

        return X, self._data.y

    def _model(self, **kwargs):
        """
        Build an XGBoost model based on the task_type
        """
        global_params = dict(random_state=SEED, n_estimators=N_BOOST)
        if self.task_type == 'regression':
            model = xgb.XGBRegressor(**global_params, **kwargs)
        elif self.task_type == "binary":
            model = xgb.XGBClassifier(**global_params, **kwargs)
        else:
            model = xgb.XGBClassifier(objective='multi:softprob', **global_params, **kwargs)
        return model

    @property
    def _metric(self):
        if self.task_type == 'regression':
            return 'rmse'
        elif self.task_type == 'binary':
            return 'logloss'
        else:
            return 'mlogloss'

    @property
    def _scorer(self):
        if self.task_type == 'regression':
            return lambda y_true, y_pred: mean_squared_error(y_true, y_pred, squared=False)
        else:
            return log_loss

    def cross_validate(self, **kwargs):
        scores = dict()
        X, y = self._preprocessed_data

        logging.info(12 * "=" + f"Training XGBoost model on {self._data.name.strip()} data" + 12 * "=" + "\n")
        for idx, (tr_idx, val_idx) in enumerate(self._cv.split(X, y)):
            logging.info(10 * "=" + f"Training fold {idx}" + 10 * "=")
            start = time.time()

            X_train, X_valid = X[tr_idx], X[val_idx]
            y_train, y_valid = y[tr_idx], y[val_idx]

            model = self._model(**kwargs).fit(X_train, y_train,
                                              eval_set=[(X_valid, y_valid)],
                                              eval_metric=self._metric,
                                              early_stopping_rounds=150,
                                              verbose=False)
            if self.task_type == 'regression':
                preds = model.predict(X_valid)
            else:
                preds = model.predict_proba(X_valid)

            score = self._scorer(y_valid, preds)
            fold_time = time.time() - start

            scores[idx] = [score, fold_time]
        return scores


class LGBMTask(XGBTask):
    def __init__(self, data_path: str, data_name: str, target: str, task_type: str):
        super().__init__(data_path, data_name, target, task_type)

    @property
    def _preprocessed_data(self):
        num_pipeline = make_pipeline(SimpleImputer(strategy='constant', fill_value=-9999))
        cat_pipeline = make_pipeline(SimpleImputer(strategy='most_frequent'),
                                     OrdinalEncoder(dtype=np.int))
        full_pipe = ColumnTransformer(transformers=[
            ('num_pipe', num_pipeline, make_column_selector(dtype_include=np.number)),
            ('cat_pipe', cat_pipeline, make_column_selector(dtype_exclude=np.number))
        ])
        X = full_pipe.fit_transform(self._data.X)

        return X, self._data.y

    @property
    def _metric(self):
        if self.task_type == 'regression':
            return 'rmse'
        elif self.task_type == 'binary':
            return 'binary_logloss'
        else:
            return 'multi_logloss'

    def _model(self, **kwargs):
        """
        Build a LightGBM model based on the task_type
        """
        global_params = dict(random_state=SEED, n_estimators=N_BOOST)
        if self.task_type == 'regression':
            model = lgbm.LGBMRegressor(**global_params, **kwargs)
        elif self.task_type == "binary":
            model = lgbm.LGBMClassifier(objective='binary', **global_params, **kwargs)
        else:
            model = lgbm.LGBMClassifier(objective='multiclass', **global_params, **kwargs)

        return model

    def cross_validate(self, **kwargs):
        scores = dict()
        X, y = self._preprocessed_data

        logging.info(12 * "=" + f"Training LightGBM model on {self._data.name.strip()} data" + 12 * "=" + "\n")
        for idx, (tr_idx, val_idx) in enumerate(self._cv.split(X, y)):
            logging.info(10 * "=" + f"Training fold {idx}" + 10 * "=")
            start = time.time()

            X_train, X_valid = X[tr_idx], X[val_idx]
            y_train, y_valid = y[tr_idx], y[val_idx]

            model = self._model(**kwargs).fit(X_train, y_train,
                                              eval_set=[(X_valid, y_valid)],
                                              eval_metric=self._metric,
                                              early_stopping_rounds=150,
                                              categorical_feature=self._data.categoricals,
                                              verbose=False)
            if self.task_type == 'regression':
                preds = model.predict(X_valid)
            else:
                preds = model.predict_proba(X_valid)

            score = self._scorer(y_valid, preds)
            fold_time = time.time() - start

            scores[idx] = [score, fold_time]
        return scores


class CBTask(LGBMTask):
    def __init__(self, data_path: str, data_name: str, target: str, task_type: str):
        super().__init__(data_path, data_name, target, task_type)

    @property
    def _preprocessed_data(self):
        num_pipeline = make_pipeline(SimpleImputer(strategy='constant', fill_value=-9999))
        cat_pipeline = make_pipeline(SimpleImputer(strategy='most_frequent'),
                                     OrdinalEncoder(dtype=np.int))
        full_pipe = ColumnTransformer(transformers=[
            ('num_pipe', num_pipeline, self._data.X.columns[~self._data.X.columns.isin(self._data.categoricals)]),
            ('cat_pipe', cat_pipeline, self._data.categoricals)
        ])
        X = full_pipe.fit_transform(self._data.X)

        return X, self._data.y

    @property
    def _metric(self):
        if self.task_type == 'regression':
            return 'RMSE'
        elif self.task_type == 'binary':
            return 'Logloss'
        else:
            return 'MultiClassOneVsAll'

    def _model(self, **kwargs):
        """
        Build a CatBoost model based on the task_type
        """
        global_params = dict(random_state=SEED, n_estimators=N_BOOST)
        if self.task_type == 'regression':
            model = cb.CatBoostRegressor(**global_params, **kwargs)
        elif self.task_type == 'binary':
            model = cb.CatBoostClassifier(**global_params, **kwargs)
        else:
            model = cb.CatBoostClassifier(**global_params, **kwargs)

        return model

    def cross_validate(self, **kwargs):
        scores = dict()
        X, y = self._preprocessed_data

        logging.info(12 * "=" + f"Training CatBoost model on {self._data.name.strip()} data" + 12 * "=" + "\n")
        for idx, (tr_idx, val_idx) in enumerate(self._cv.split(X, y)):
            logging.info(10 * "=" + f"Training fold {idx}" + 10 * "=")
            start = time.time()

            X_train, X_valid = X[tr_idx], X[val_idx]
            y_train, y_valid = y[tr_idx], y[val_idx]

            model = self._model(**kwargs, loss_function=self._metric, eval_metric=self._metric, one_hot_max_size=15) \
                .fit(pd.DataFrame(X_train), y_train,
                     eval_set=[(pd.DataFrame(X_valid), y_valid)],
                     early_stopping_rounds=150,
                     cat_features=self._data.categoricals,
                     verbose=False)
            if self.task_type == 'regression':
                preds = model.predict(X_valid)
            else:
                preds = model.predict_proba(X_valid)

            score = self._scorer(y_valid, preds)
            fold_time = time.time() - start

            scores[idx] = [score, fold_time]
        return scores
