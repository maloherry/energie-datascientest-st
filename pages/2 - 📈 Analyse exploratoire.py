import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')

st.title("Analyse exploratoire")
st.header("Visualisation des variations mensuelles sur une année (moyenne)")
data_month_viz = pd.read_pickle('data/data_month_viz.pkl')
fig = plt.figure(figsize=(16,10))
colors = sns.color_palette("RdBu", 7)
labels = ['Nucleaire','Thermique','Eolien','Solaire','Hydraulique','Bioénergies']
plt.stackplot(data_month_viz.month, data_month_viz.nucleaire, data_month_viz.thermique, data_month_viz.eolien, data_month_viz.solaire, data_month_viz.hydraulique, data_month_viz.bioenergies, labels=labels, colors=colors)
plt.plot(data_month_viz.month, data_month_viz.consommation, c='green', label = 'Consommation')
plt.legend(loc = "upper center", bbox_to_anchor=(1.1, 0.8), ncol=1)
plt.title('Production par filière et consommation, par mois')
plt.ylabel('MW(1/2h)')
plt.xlabel('Mois')
plt.xticks(np.arange(1,13,1), rotation=40);
st.pyplot(fig)

data_month_reg = pd.read_pickle('data/data_month_reg_viz.pkl')

reg_option_m = st.selectbox(
     'Sélectionnez la région à afficher',
     ('Île-de-France', 'Centre-Val de Loire', 'Bourgogne-Franche-Comté', 'Normandie', 'Hauts-de-France', 'Grand Est', 'Pays de la Loire', 'Bretagne', 'Nouvelle-Aquitaine', 'Occitanie', 'Auvergne-Rhône-Alpes', "Provence-Alpes-Côte d'Azur"), key = 1)
data_month_viz = data_month_reg[data_month_reg.region == reg_option_m]

fig = plt.figure(figsize=(16,10))
colors = sns.color_palette("RdBu", 7)
labels = ['Nucleaire','Thermique','Eolien','Solaire','Hydraulique','Bioénergies']
plt.stackplot(data_month_viz.month, data_month_viz.nucleaire, data_month_viz.thermique, data_month_viz.eolien, data_month_viz.solaire, data_month_viz.hydraulique, data_month_viz.bioenergies, labels=labels, colors=colors)
plt.plot(data_month_viz.month, data_month_viz.consommation, c='green', label = 'Consommation')
plt.legend(loc = "upper center", bbox_to_anchor=(1.1, 0.8), ncol=1)
plt.title('Production par filière et consommation, par mois')
plt.ylabel('MW(1/2h)')
plt.xlabel('Mois')
plt.xticks(np.arange(1,13,1), rotation=40);
st.pyplot(fig)

st.header("Visualisation des variations horaires sur une journée (moyenne)")
data_hour_viz = pd.read_pickle('data/data_hour_viz.pkl')

fig = plt.figure(figsize=(16,10))
labels = ['Nucleaire','Thermique','Eolien','Solaire','Hydraulique','Bioénergies']
plt.stackplot(data_hour_viz.hour, data_hour_viz.nucleaire, data_hour_viz.thermique, data_hour_viz.eolien, data_hour_viz.solaire, data_hour_viz.hydraulique, data_hour_viz.bioenergies, labels=labels, colors=colors)
plt.plot(data_hour_viz.hour, data_hour_viz.consommation, c='green', label = 'Consommation')
plt.legend(loc = "upper center", bbox_to_anchor=(1.1, 0.8), ncol=1)
plt.title('Production par filière et consommation, par heure')
plt.ylabel('MW(1/2h)')
plt.xlabel('Heure')
plt.xticks(np.arange(0,24,1), rotation=40);
st.pyplot(fig)

data_hour_reg = pd.read_pickle('data/data_hour_reg_viz.pkl')

reg_option_h = st.selectbox(
     'Sélectionnez la région à afficher',
     ('Île-de-France', 'Centre-Val de Loire', 'Bourgogne-Franche-Comté', 'Normandie', 'Hauts-de-France', 'Grand Est', 'Pays de la Loire', 'Bretagne', 'Nouvelle-Aquitaine', 'Occitanie', 'Auvergne-Rhône-Alpes', "Provence-Alpes-Côte d'Azur"), key = 2)
data_hour_viz = data_hour_reg[data_hour_reg.region == reg_option_h]
fig = plt.figure(figsize=(16,10))
labels = ['Nucleaire','Thermique','Eolien','Solaire','Hydraulique','Bioénergies']
plt.stackplot(data_hour_viz.hour, data_hour_viz.nucleaire, data_hour_viz.thermique, data_hour_viz.eolien, data_hour_viz.solaire, data_hour_viz.hydraulique, data_hour_viz.bioenergies, labels=labels, colors=colors)
plt.plot(data_hour_viz.hour, data_hour_viz.consommation, c='green', label = 'Consommation')
plt.legend(loc = "upper center", bbox_to_anchor=(1.1, 0.8), ncol=1)
plt.title('Production par filière et consommation, par heure')
plt.ylabel('MW(1/2h)')
plt.xlabel('Heure')
plt.xticks(np.arange(0,24,1), rotation=40);
st.pyplot(fig)