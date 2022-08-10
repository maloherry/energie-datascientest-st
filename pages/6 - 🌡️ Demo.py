import streamlit as st
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from joblib import load
from xgboost import XGBRegressor
#plt.style.use('dark_background')

data_month = pd.read_pickle('data/data_month.pkl')
data_week = pd.read_pickle('data/data_week.pkl')
data_hour = pd.read_pickle('data/data_hour.pkl.gz')

model_h = load('data/model_h.joblib') 
model_w = load('data/model_w.joblib') 
model_m = load('data/model_m.joblib') 

dicreg = {11 : 'Île-de-France',
          24 : 'Centre-Val de Loire',
          27 : 'Bourgogne-Franche-Comté',
          28 : 'Normandie',
          32 : 'Hauts-de-France',
          44 : 'Grand Est',
          52 : 'Pays de la Loire',
          53 : 'Bretagne',
          75 : 'Nouvelle-Aquitaine',
          76 : 'Occitanie',
          84 : 'Auvergne-Rhône-Alpes',
          93 : 'Provence-Alpes-Côte d\'Azur',
          94 : 'Corse'
          }
st.title('Prédictions selon la température')

pas_sel = st.selectbox(
     'Sélectionnez le pas temporel :',
     ('Mensuel', 'Horaire sur une semaine')
)
delta_temp = st.slider('Variation de la température moyenne', min_value=-5, max_value=5, value=1)
delta_pop = st.slider('Variation de la population (100 000)', min_value=-10, max_value=10, value=1)


if pas_sel == 'Mensuel':

    df_m = data_month.copy().drop('datetime', axis = 1)
    data_m = df_m.drop('conso', axis = 1)
    target_m = df_m['conso']
    X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(data_m, target_m, test_size = 0.2, shuffle = False)
    scaler_m = preprocessing.StandardScaler().fit(X_train_m)
    X_test_m_temp = X_test_m.copy()
    X_train_m = scaler_m.transform(X_train_m)
    X_test_m = scaler_m.transform(X_test_m)

    X_test_m_temp['temp'] = X_test_m_temp['temp'] + delta_temp
    X_test_m_temp['pop'] = X_test_m_temp['pop'] + (delta_pop*100000)

    X_test_m_temp = scaler_m.transform(X_test_m_temp)

    xgb_pred_test = model_m.predict(X_test_m)
    xgb_pred_test_temp = model_m.predict(X_test_m_temp)

    reg = data_month.reg_code.tail(len(y_test_m))
    datetime = data_month.datetime.tail(len(y_test_m))
    comp = pd.DataFrame({'datetime' : datetime, 'pred_origine' : xgb_pred_test, 'pred_mod' : xgb_pred_test_temp,'reg' : reg})
    comp['reg'] = comp['reg'].replace(dicreg)

    fig, axs = plt.subplots(4,3, figsize=(20, 15))
    fig.subplots_adjust(hspace = .25, wspace=.1)
    axs = axs.ravel()
    for n, i in enumerate(comp.reg.unique()):
        data = comp[comp.reg == i]
        axs[n].plot(data.datetime, data.pred_mod, c='#318e9a')
        axs[n].plot(data.datetime, data.pred_origine, c='#DE5B45')
        axs[n].title.set_text(i)
        axs[n].set_xticks(axs[n].get_xticks()[::2])
        plt.setp(axs[n].get_xticklabels()[-1], visible=False)

    fig.legend(['Prédiction modifiée', 'Prédiction d\'origine'], bbox_to_anchor=(0., 0., 0.5, 0.95))
    st.pyplot(fig)

if pas_sel == 'Horaire sur une semaine':
    df_h = data_hour.copy().drop('datetime', axis = 1)
    data_h = df_h.drop('conso', axis = 1)
    target_h = df_h['conso']
    X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(data_h, target_h, test_size = 0.2, shuffle = False)
    scaler_h = preprocessing.StandardScaler().fit(X_train_h)
    X_test_h_temp = X_test_h.copy()
    X_train_h = scaler_h.transform(X_train_h)
    X_test_h = scaler_h.transform(X_test_h)

    X_test_h_temp['temp'] = X_test_h_temp['temp'] + delta_temp
    X_test_h_temp['pop'] = X_test_h_temp['pop'] + (delta_pop*100000)
    X_test_h_temp = scaler_h.transform(X_test_h_temp)

    xgb_pred_test = model_h.predict(X_test_h)
    xgb_pred_test_temp = model_h.predict(X_test_h_temp)

    reg = data_hour.reg_code.tail(len(y_test_h))
    datetime = data_hour.datetime.tail(len(y_test_h))
    comp = pd.DataFrame({'datetime' : datetime, 'pred_origine' : xgb_pred_test, 'pred_mod' : xgb_pred_test_temp,'reg' : reg})
    comp['reg'] = comp['reg'].replace(dicreg)
    comp = comp[(comp['datetime'] < '2022-05-08') & (comp['datetime'] > '2022-05-01')]

    fig, axs = plt.subplots(4,3, figsize=(20, 15))
    fig.subplots_adjust(hspace = .25, wspace=.1)
    axs = axs.ravel()
    for n, i in enumerate(comp.reg.unique()):
        data = comp[comp.reg == i]
        axs[n].plot(data.datetime, data.pred_mod, c='#318e9a')
        axs[n].plot(data.datetime, data.pred_origine, c='#DE5B45')
        axs[n].title.set_text(i)
        axs[n].set_xticks(axs[n].get_xticks()[::2])
        plt.setp(axs[n].get_xticklabels()[-1], visible=False)

    fig.legend(['Prédiction modifiée', 'Prédiction d\'origine'], bbox_to_anchor=(0., 0., 0.5, 0.95))
    st.pyplot(fig)