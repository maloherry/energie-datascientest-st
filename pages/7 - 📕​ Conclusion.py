import streamlit as st
import pandas as pd
import numpy as np

st.title('Conclusion')


st.markdown(
    """
La prédiction de la consommation d’électricité par région à différents pas temporels est donc faisable avec une marge d’erreur relativement faible avec les modèles testés et des données prévisibles à l’avance. Le fait que la population soit la variable la plus utilisée par la majorité des modèles permet en effet de faire des prédictions sur des périodes assez longues, puisqu’il s’agit d’une variable qui évolue lentement et pour laquelle on dispose d’estimations à court, moyen et long terme.

Le XGB Regressor est le modèle qui semble le plus robuste sur les trois pas temporels que nous avons testé. A l’échelle mensuelle, il utilise très largement la variable population. Aux échelles hebdomadaires et horaires, la température prend de l’importance, ce qui permet donc d’avoir des estimations avec cette précision dès que l’on dispose des prévisions météorologiques suffisamment fiables (environ [10 jours à l’avance](https://journals.ametsoc.org/view/journals/atsc/76/4/jas-d-18-0269.1.xml)).

Pour améliorer la précision, on pourrait essayer d’optimiser le modèle par région. Des modèles entraînés et optimisés sur des données régionalisées permettraient probablement d’éviter le risque de sous-estimer la consommation dans certaines régions ou à certaines périodes de l’année.
""")