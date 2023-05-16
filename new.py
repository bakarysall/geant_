import streamlit as st
import openai
import numpy as np
import joblib

# Initialisation de l'API OpenAI
openai.api_key = "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"

# Chargement du modèle de classification des sols
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
# Définition de la variable culture
culture = {
    0: "Riz", 
    1: "Maïs", 
    2: "Pois chiches", 
    3: "Haricots rouges", 
    4: "Pois d'Angole", 
    5: "Haricot mungo", 
    6: "Arachides", 
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

# Initialisation de la variable prediction à None
prediction = None

# Code pour les boutons
if st.button("Prédire"):
    # Affichage de la prédiction
    prediction = inference(azote, phosphore, potassium, temperature, humidite, ph, precipitation)
    st.subheader(f"Culture adaptée dans le sol : {culture[prediction[0]]}")
    
    # Génération de la stratégie avec ChatGPT
    prompt = f"Donne moi les rendements de la culture du {culture[prediction[0]]} au Sénégal les 5 dernières années. "
    response = openai.Completion.create(
        engine="davinci", prompt=prompt,max_tokens=2000, n=1, stop=None, temperature=0.5)
    strategy = response.choices[0].text.strip()
    st.write(f"{strategy}")

# Pied de page
st.markdown("---")
st.write("© Bakary SALL - 2023")
