import pandas as pd
import numpy as np

data_dict = {
    'id': list(range(100, 115)),
    'film': ['Iron Man', 'The Incredible Hulk', 'Iron Man 2', 'Thor', 'Captain America 1', 'The Avengers 1',
             'Iron Man 3', 'Thor: The Dark World', 'Captain America 2', 'Guardians of the Galaxy', 'Avengers 2',
             'Ant-Man', 'Captain America 3', 'Doctor Strange', 'Spider-Man: Homecoming'],
    'release_date': ['2008-05-02', '2008-07-13', '2010-05-07', '2011-05-06', '2011-08-22', '2012-05-04',
                     '2013-05-03', '2013-11-08', '2014-04-04', '2014-08-01', '2015-05-01', '2015-07-17',
                     '2016-05-06', '2016-11-04', '2017-07-07'],
    'sequel_id': [102, np.nan, 106, 107, 108, 110, np.nan, np.nan, 112, np.nan, np.nan, np.nan, np.nan, np.nan,
                  np.nan],
    'director_id': [201, 202, 201, 203, 204, 205, 206, 207, 208, 209, 205, 210, 208, 211, 212]
}
films = pd.DataFrame(data_dict)

data_dict_2 = {
    'director_id': [201, 202, 201, 203, 204, 205, 206, 207, 208, 209, 205, 210, 208, 211, 212],
    'name': ['Jon Favreau', 'Louis Leterrier', 'Jon Favreau', 'Kenneth Branagh', 'Joe Johnston', 'Joss Whedon',
             'Shane Black', 'Alan Taylor', 'Anthony and Joe Russo', 'James Gunn', 'Joss Whedon', 'Peyton Reed',
             'Anthony and Joe Russo', 'Scott Derrickson', 'Jon Watts']
}
directors = pd.DataFrame(data_dict_2)

data_dict_3 = {
    'name': ['Clark Gregg', 'Samuel L. Jackson', 'Jon Favreau', 'Robert Downey Jr.', 'Scarlett Johansson',
             'Jeremy Renner', 'Idris Elba', 'Chris Hemsworth', 'Tom Hiddleston', 'Chris Evans', 'Sebastian Stan',
             'Stanley Tucci', 'Mark Ruffalo'],
    'introduced_film': [100, 100, 100, 100, 100, 102, 103, 103, 103, 103, 104, 104, 101]
}

actors = pd.DataFrame(data_dict_3)

# Save dataframes to CSVs
films.to_csv('data/films.csv', index=False)
directors.to_csv('data/directors.csv', index=False)
actors.to_csv('data/actors.csv', index=False)
