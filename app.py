import streamlit as st
import numpy as np
from PIL import Image
import joblib

model = joblib.load(filename="model_random.joblib")
st.sidebar.title("Bienvenu dans le futur")
foto=Image.open('port.jpg')
st.sidebar.image(foto, caption=f"Transformez votre exploitation agricole avec la puissance de la technologie")
st.write('')       
st.sidebar.write(f"L'application de classification des cultures sur le machine learning utilise des algorithmes pour identifier les différents types de cultures en fonction des caractéristiques chimiques, physiques et environnementales telles que l'azote, le phosphore, le potassium, le pH, l'humidité et la précipitation. Elle permet aux professionnels de mieux comprendre la qualité du sol et de planifier les cultures, la construction et les projets environnementaux de manière efficace et durable.")
image=Image.open('image.jpg')
st.write('')
st.sidebar.image(image,caption =f"Augmentez votre rendement avec l'agriculture intelligente")
st.title('Cultivez avec précision grâce à la technologie de pointe')
st.subheader("Prédiser d'abord le type de culture adequate dans votre sol")
st.markdown("Veuillez récolter d'abord les données nécessaires")
azote = st.number_input(label="Entrer la valeur de l'azote", value=0)
phosphore = st.number_input(label="Entrer la valeur du Phosphore", value=0)
potassium = st.number_input(label="Entrer la valeur du potassium", value=0)
temperature = st.number_input(label="Entrer la temperature du sol", value=0.0000)
humidite = st.number_input(label="Entrer la valeur de l'humidité du sol", value=0.0)
ph = st.number_input(label="Entrer le PH du sol", value=0)
precipitation = st.number_input(label="Entrer la précipitation du sol", value=0)

def inference(azote, phosphore, potassium, temperature, humidite, ph, precipitation):
    new_data = np.array([
        azote, phosphore, potassium, temperature, humidite, ph, precipitation
    ])
    predict = model.predict(new_data.reshape((1,-1)))
    return predict 

if st.button("Prediction"):
    prediction = inference(azote, phosphore, potassium, temperature, humidite, ph, precipitation)
    if prediction==2:
        st.success(f"Le sol est adapté a la culture de pois chiches ")
    if prediction==1:
        st.success(f"Le sol est adapté à la culture du maïs")
    if prediction==0:
        st.success(f"Le sol est adapté à la culture du Riz")
    if prediction==3:
        st.success(f"Le sol est adapté à la culture haricots rouges")
    if prediction==4:
        st.success(f"Le sol est adapté à la culture du pois d'Angole")
    if prediction==5:
        st.success(f"Le sol est adapté à la culture du haricot mungo")
    if prediction ==6:
        st.success(f"Le sol est adapté à la culture du haricot mungo")
    if prediction==7:
        st.success(f"Le sol est adapté à la culture du blackgram")
    if prediction==8:
        st.success(f"Le sol est adapté à la culture du lentille")
    if prediction==9:
       st.success(f"Le sol est adapté à la culture du grenade")
    if prediction==10:
       st.success(f"Le sol est adapté à la culture du banane")
    if prediction==11:
        st.success(f"Le sol est adapté à la culture du mangue")
    if prediction==12:
        st.success(f"Le sol est adapté à la culture du raisin")
    if prediction==13:
        st.success(f"Le sol est adapté à la culture du pastèque")
    if prediction==14:
        st.success(f"Le sol est adapté à la culture du melon musqué")   
    if prediction==15:
        st.success(f"Le sol est adapté à la culture du pomme")
    if prediction==16:
        st.success(f"Le sol est adapté à la culture du orange")
    if prediction==17:
        st.success(f"Le sol est adapté à la culture du papaye")
    if prediction==18:
        st.success(f"Le sol est adapté à la culture du coton")
    if prediction==19:
        st.success(f"Le sol est adapté à la culture du jute")
    if prediction==20:
        st.success(f"Le sol est adapté à la culture du café")

st.markdown("<p style='text-align: center; color: gray;'>© Bakary SALL - 2023</p>", unsafe_allow_html=True)