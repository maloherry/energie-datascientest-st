import streamlit as st
st.set_page_config(layout="wide", page_title="Prédiction de la consommation d'énergie")
import pandas as pd
import numpy as np

# Mise en forme
st.image('home.jpg')
st.title("Consommation d'énergie électrique")
st.header("Analyse et prédiction à l'échelle régionale")
st.markdown("Dans un contexte de tension sur le marché de l’énergie, la capacité de RTE (Réseau de transport d'électricité) et des producteurs d’énergie à prévoir la consommation en avance est un enjeu sectoriel important. Garantir la **sécurité d’approvisionnement** en prévoyant les pics de consommation est en effet primordial pour éviter des coupures. L’indisponibilité d’une partie du parc nucléaire français pour des raisons de maintenance et les difficultés d’approvisionnement en gaz augmentent fortement les risques de décalage entre production et consommation sur l’année à venir.")

st.markdown("A partir des données de consommation et de production en temps réel fournies par RTE, l’objectif est d’étudier à l’échelle régionale le phasage entre consommation et production et de construire un modèle de **prédiction de la consommation à différentes échelles temporelles**.")

st.markdown("Un modèle suffisamment précis permet au régulateur de piloter la mise en route des différentes capacités de production électrique disponibles, les échanges entre régions et si nécessaire, d’acheter de l’énergie aux pays voisins.")

