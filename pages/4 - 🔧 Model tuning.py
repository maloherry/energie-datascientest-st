import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joblib import load
from xgboost import XGBRegressor

st.title("Modélisation - model tuning")

st.markdown("""
Le travail effectué jusqu’à présent concerne des modèles testés avec leurs paramètres par défaut. On cherche maintenant à optimiser ces modèles en cherchant les meilleurs hyperparamètres pour nos données.

Nous générons les ensembles d’entraînement et de test sur les données horaires, hebdomadaires et mensuelles sur ce modèle :
""")
st.code("""
df_h = data_hour.copy().drop('datetime', axis = 1)
data_h = df_h.drop('conso', axis = 1)
target_h = df_h['conso']
X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(data_h, target_h, test_size = 0.2, shuffle = False)
scaler_h = preprocessing.StandardScaler().fit(X_train_h)
X_train_h = scaler_h.transform(X_train_h)
X_test_h = scaler_h.transform(X_test_h)
""")

st.markdown("On détermine les meilleurs hyperparamètres avec `GridSearchCV`.")

model_sel = st.selectbox(
     'Sélectionnez le modèle pour afficher ses résultats',
     ('Ridge', 'SGD', 'XGB', 'Random Forest Regressor')
)

if model_sel == 'Ridge':
    st.code("""
Score (données horaires) : 0.8262878111407227
Meilleurs paramètres (données horaires) : {'alpha': 0.01, 'fit_intercept': True, 'solver': 'saga'}
Score (données hebdomadaires) : 0.8970031138948403
Meilleurs paramètres (données hebdomadaires) : {'alpha': 1, 'fit_intercept': True, 'solver': 'saga'}
Score (données mensuelles) : 0.9050046346076753
Meilleurs paramètres (données mensuelles) : {'alpha': 0.0001, 'fit_intercept': True, 'solver': 'sag'}
""")

if model_sel == 'SGD':
    st.code("""
Score (données horaires) : 0.8277417155608037
Meilleurs paramètres (données horaires) : {'alpha': 0.001, 'fit_intercept': True, 'penalty': 'elasticnet'}
Score (données hebdomadaires) : 0.8923362675773058
Meilleurs paramètres (données hebdomadaires) : {'alpha': 0.1, 'fit_intercept': True, 'penalty': 'elasticnet'}
Score (données mensuelles) : 0.9019155244014166
Meilleurs paramètres (données mensuelles) : {'alpha': 0.1, 'fit_intercept': True, 'penalty': 'l2'}
""")

if model_sel == 'XGB':
    st.code("""
Score (données horaires) : 0.9704201574914171
Meilleurs paramètres (données horaires) : {'eta': 0.3, 'max_depth': 6}
Score (données hebdomadaires) : 0.984319877146753
Meilleurs paramètres (données hebdomadaires) : {'eta': 0.1, 'max_depth': 7}
Score (données mensuelles) : 0.9857172435564758
Meilleurs paramètres (données mensuelles) : {'eta': 0.1, 'max_depth': 5}
""")

if model_sel == 'Random Forest Regressor':
    st.code("""
Score (données horaires) : 0.9510424490768887
Meilleurs paramètres (données horaires) : {'criterion': 'squared_error'}
Score (données hebdomadaires) : 0.9788280916605485
Meilleurs paramètres (données hebdomadaires) : {'criterion': 'squared_error'}
Score (données mensuelles) : 0.9845557614698054
Meilleurs paramètres (données mensuelles) : {'criterion': 'squared_error'}
""")

st.markdown("Le XGB Regressor est le modèle qui obtient les meilleurs scores sur les trois échelles temporelles. Il se base très largement (comme les autres modèles), sur la population et la température :")

model_h = load('data/model_h.joblib') 
model_w = load('data/model_w.joblib') 
model_m = load('data/model_m.joblib') 

columns = ['reg_code', 'hum', 'temp', 'vent', 'prec', 'pop', 'puiss_edf',
       'confinement', 'feries', 'year', 'month', 'week', 'weekday', 'day',
       'hour']
plt.style.use('dark_background')
fig = plt.figure(figsize = (22,10))
plt.subplot(1,3,1)
pd.Series(model_h.feature_importances_, index=['reg_code', 'hum', 'temp', 'vent', 'prec', 'pop', 'puiss_edf', 'confinement', 'feries', 'year', 'month', 'week', 'weekday', 'day', 'hour']).sort_values(ascending = False).plot(kind = 'barh')
plt.title('XGB - Données horaires');

plt.subplot(1,3,2)
pd.Series(model_w.feature_importances_, index=['reg_code', 'hum', 'temp', 'vent', 'prec', 'pop', 'puiss_edf', 'confinement', 'feries', 'year', 'month', 'week']).sort_values(ascending = False).plot(kind = 'barh')
plt.title('XGB - Données hebdomadaires');

plt.subplot(1,3,3)
pd.Series(model_m.feature_importances_, index=['reg_code', 'hum', 'temp', 'vent', 'prec', 'pop', 'puiss_edf', 'confinement', 'feries', 'year', 'month']).sort_values(ascending = False).plot(kind = 'barh')
plt.title('XGB - Données mensuelles');

st.pyplot(fig)
