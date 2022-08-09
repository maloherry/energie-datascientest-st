import streamlit as st
import pandas as pd
import numpy as np

# Mise en forme
st.title("Les données")
st.markdown("[Les données](https://odre.opendatasoft.com/explore/dataset/eco2mix-regional-cons-def/information/?disjunctive.libelle_region&disjunctive.nature) sont issues de l’application éCO2mix de RTE qui nous donne accès à la consommation et à la production par filière depuis 2013, avec un pas temporel de 30 minutes et par région.")

st.markdown("Une fois la phase exploratoire terminée, on garde seulement la variable cible (la consommation), la date, l'heure et la région, les variables liées à la production n'étant pas prévisibles à l'avance.")

st.markdown(
    """
Nous ajoutons plusieurs variables :
* Des données **météorologiques** (humidité, température, vitesse du vent précipitations dans la dernière heure) obtenues en faisant la moyenne des observations des stations d'une région à partir de la [base SYNOP](file:///home/maloherry/Dropbox/datascientest/projet_energie/rapport/)(https:/public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/)
* Des données **démographiques** : les chiffres annuels de la population [fournis par l'INED](https://www.ined.fr/fr/tout-savoir-population/chiffres/france/structure-population/regions-departements/) (Institut national d'études démographiques)
* La **puissance installée** en centrales nucléaires et thermiques [gérées par EDF](https://www.data.gouv.fr/fr/datasets/centrales-de-production-nucleaire-et-thermique-a-flamme-de-edf-sa/)
* Une variable **confinement** qui prend la valeur de 1 les jours du premier confinement (du 17 mars au 10 mai 2020) pour prendre en compte la baisse d'activité économique importante qu'il a causé
* Une variable **jour férié** à partir des [données Etalab](https://www.data.gouv.fr/fr/datasets/jours-feries-en-france/)
""")