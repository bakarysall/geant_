import streamlit as st
import numpy as np
import joblib

model = joblib.load(filename="model_random.joblib")

# Titre et introduction
st.title("Application de classification des sols")
st.write("Cette application vous permet de prédire la culture adaptée à un sol en fonction de certaines caractéristiques.")

st.header("Entrer les données")
st.write("Veuillez renseigner les valeurs suivantes :")
azote = st.number_input(label="Azote")
phosphore = st.number_input(label="Phosphore")
potassium = st.number_input(label="Potassium")
temperature = st.number_input(label="Température du sol")
humidite = st.number_input(label="Humidité du sol")
ph = st.number_input(label="pH du sol")
precipitation = st.number_input(label="Précipitation")

# Fonction de prédiction
def inference(azote, phosphore, potassium, temperature, humidite, ph, precipitation):
    new_data = np.array([
        azote, phosphore, potassium, temperature, humidite, ph, precipitation
    ])
    predict = model.predict(new_data.reshape((1,-1)))
    return predict 

# Bouton de prédiction
if st.button("Prédire"):
    # Affichage de la prédiction
    prediction = inference(azote, phosphore, potassium, temperature, humidite, ph, precipitation)
    culture = {
        0: "Riz", 
        1: "Maïs", 
        2: "Pois chiches", 
        3: "Haricots rouges", 
        4: "Pois d'Angole", 
        5: "Haricot mungo", 
        6: "Haricot mungo", 
        7: "Blackgram", 
        8: "Lentille", 
        9: "Grenade", 
        10: "Banane", 
        11: "Mangue", 
        12: "Raisin", 
        13: "Pastèque", 
        14: "Melon musqué", 
        15: "Pomme", 
        16: "Orange", 
        17: "Papaye", 
        18: "Coton", 
        19: "Jute", 
        20: "Café"
    }
    st.subheader(f"Culture adaptée dans le sol : {culture[prediction[0]]}")

# Pied de page
st.markdown("---")
st.write("© Bakary SALL - 2023")
