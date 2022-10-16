import sys
import os
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
import xgboost as xgb
import lightgbm as lgb
import joblib
import numpy as np
import pandas as pd
import sklearn

def logic_layer(x):
    workpath = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(workpath, './RandomForest1.pkl'), 'rb') as f:
        RF = joblib.load(f)
    f.close()
    with open(os.path.join(workpath, './XGB1.pkl'), 'rb') as f:
        XGB = joblib.load(f)
    f.close()
    with open(os.path.join(workpath, './LGBM1.pkl'), 'rb') as f:
        LGBM = joblib.load(f)
    f.close()
    layer_features = ['전용면적(㎡)','계약일','층','건축년도','구','동','평','계약년','계약월','한강','건물나이','재건축']
    x = np.array(x).reshape(1,-1)
    LGBM_predict= LGBM.predict(x)
    XGB_predict = XGB.predict(x)
    RF_predict = RF.predict(x)
    predictions = (LGBM_predict*0.1)+(XGB_predict*0.05)+(RF_predict*0.85)
    return np.round(np.expm1(predictions),-3)[0]/10000
if __name__ == "__main__":
    x = [4.744323,28,2.772589,2001,16,195,3.653252,2025,6,0.0,24,0.0]
    x = np.array(x).reshape(1,-1)
    print(logic_layer(x))