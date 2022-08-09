import streamlit as st
import pandas as pd
import numpy as np

st.title("Modélisation - méthode")

st.markdown(
    """
L’objectif est de prédire une variable continue (la consommation). Nous avons donc choisi de tester les modèles suivants :
* Régression linéaire multiple
* Régression linéaire régularisée : Ridge, Lasso, Elastic Net
* XGB Regressor
* SGD Regressor
* Random Forest Regressor
Notre travail de modélisation a commencé par la génération des ensembles d'entraînement et de test au niveau horaire puis par l’application de chaque modèle avec ses hyperparamètres par défaut.
""")

scores = pd.read_pickle('data/scores.pkl')
st.dataframe(scores)

st.markdown("A partir de ce tableau, on sélectionne les modèles pour lesquels nous allons chercher les meilleurs hyperparamètres : Ridge, SGD, XGB et Random Forest.")