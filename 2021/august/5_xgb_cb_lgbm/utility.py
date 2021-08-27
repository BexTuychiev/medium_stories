import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import optuna
import lightgbm as lgbm
import catboost as cb
import xgboost as xgb
from sklearn.model_selection import cross_validate, KFold, train_test_split
from sklearn.metrics import mean_squared_error, log_loss
import joblib

SEED = 1121218
N_BOOST = 20000


class Data:
    def __init__(self, data_path: str, data_name: str, target: str):
        self.df = pd.read_csv(data_path)
        self.name = data_name
        self.X = self.df.drop(target, axis=1)
        self.y = self.df[[target]]

        categoricals_list = self.X.select_dtypes(exclude=np.number).columns.tolist()
        self.categoricals = categoricals_list if len(categoricals_list) > 0 else None
        self.has_missing = True if self.X.isnull().sum().sum() > 0 else False
        self.shape = self.X.shape


class Task:
    def __init__(self, data: Data, task_type: str):
        self.data = data
        self.task_type = task_type

    def _get_xgb(self, **kwargs):
        global_params = dict(random_state=SEED, n_estimators=N_BOOST, tree_method='gpu_hist')
        if self.task_type == 'regression':
            model = xgb.XGBRegressor(objective='reg:squarederror', **global_params, **kwargs)
        elif self.task_type == "binary":
            model = xgb.XGBClassifier(**global_params, **kwargs)
        else:
            model = xgb.XGBClassifier(objective='multi:softprob', **global_params, **kwargs)
        return model

    def _get_lgbm(self, **kwargs):
        global_params = dict(random_state=SEED, n_estimators=N_BOOST, device_type='gpu')
        if self.task_type == 'regression':
            model = lgbm.LGBMRegressor(**global_params, **kwargs)
        elif self.task_type == "binary":
            model = lgbm.LGBMClassifier(objective='binary', **global_params, **kwargs)
        else:
            model = xgb.XGBClassifier(objective='multiclass', **global_params, **kwargs)

        return model

    def _get_cb(self, **kwargs):
        global_params = dict(random_state=SEED, n_estimators=N_BOOST, device_type='gpu')
        if self.task_type == 'regression':
            model = cb.CatBoostRegressor(**global_params, **kwargs)
        elif self.task_type == 'binary':
            model = lgbm.LGBMRegressor(**global_params, **kwargs)
        else:
            model = lgbm.LGBMRegressor(**global_params, **kwargs)

        return model
