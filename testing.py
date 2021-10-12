import dataInterpreter as dt
import enrichmentAnalysis as ea
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
pd.options.mode.chained_assignment = None  # default='warn'

import xgboost as xgb
from sklearn.metrics import mean_squared_error

path = "C:\\Users\\Pedro\\Documents\\BicPAMS\\bicpams_5.1\\data\\latecovid\\"

cols_healthy_Calu3 = dt.get_columns('Calu3', 'healthy')
cols_cov2_Calu3 = dt.get_columns('Calu3', 'sars-cov2')

labels_calu3 = [0] * len(cols_healthy_Calu3) + [1] * len(cols_cov2_Calu3)

data_calu3 = dt.get_data('Calu3', 'healthy', 'sars-cov2')

filtered_data_calu3 = dt.get_p_values('mannwhitneyu', data_calu3, cols_healthy_Calu3, cols_cov2_Calu3)
filtered_data_calu3.drop(['p-value'], axis = 1, inplace = True)

parameters = {
    'seed': 42,
    'use_label_encoder': False,
    'booster': 'gbtree',
    'eta': 0.3,
    'gamma': 0,
    'alpha': 0,
    'n_estimators': 200,
    'eval_metric': 'mlogloss',
}

stats_calu3 = dt.apply_loocv(filtered_data_calu3.T.values, np.array(labels_calu3), xgb.XGBClassifier(**parameters))