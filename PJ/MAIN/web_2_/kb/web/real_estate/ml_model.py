import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import timeit
import sklearn
import warnings
warnings.filterwarnings('ignore')
import sys
plt.rc("font", family="Malgun Gothic")
from sklearn.linear_model import ElasticNet, Lasso
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import lightgbm as lgb
import joblib
apt_price = pd.read_csv('web\아파트_전처리.csv',encoding='utf8')
X = apt_price.drop(columns='거래금액(만원)')
y = apt_price['거래금액(만원)']
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3)
forest = RandomForestRegressor(n_estimators = 30, n_jobs = -1)
xgboost = xgb.XGBRegressor()
lightgbm = lgb.LGBMRegressor(num_leaves = 100, min_data_in_leaf = 15, max_depth=6,
                            learning_rate = 0.1, min_child_samples = 30, feature_fraction=0.9, bagging_freq= 1,
                            bagging_fraction = 0.9, bagging_seed = 11, lambda_l1 = 0.1, verbosity = -1 )
models = [{'model':xgboost, 'name':'XGBoost'},
          {'model':lightgbm, 'name':'LightGBM'},
         {'model':forest, 'name' : 'RandomForest'}]

def AveragingBlending(models, x, y, sub_x):
    for m in models : 
        m['model'].fit(x.values, y)
    
    predictions = np.column_stack([m['model'].predict(sub_x.values) for m in models])
    return predictions
y_test_pred = AveragingBlending(models, X_train, y_train, X_test)
c1 = models[0]['model'].predict(X_test.values)
c2 = models[1]['model'].predict(X_test.values)
c3 = models[2]['model'].predict(X_test.values)
joblib.dump(models[0]['model'], 'XGB1.pkl')
joblib.dump(models[1]['model'], 'LGBM1.pkl')
joblib.dump(models[2]['model'], 'RandomForest1.pkl')