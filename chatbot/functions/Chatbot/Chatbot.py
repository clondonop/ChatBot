# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:29:35 2022

@author: asus
"""
from contextlib import nullcontext
import colorama 
colorama.init()
from colorama import Fore, Style, Back
from chatbot.functions.Chatbot.create_event import *
import pickle
import json 
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import datetime
import os

with open('Intents.json') as file:
    data = json.load(file)
    
training_sentences = []
training_labels = []
labels = []
responses = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
    
    if intent['tag'] not in labels:
        labels.append(intent['tag'])
        
num_classes = len(labels)
lbl_encoder = LabelEncoder()
lbl_encoder.fit(training_labels)
training_labels = lbl_encoder.transform(training_labels)
vocab_size = 1000
embedding_dim = 16
max_len = 20
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)

# to save the fitted tokenizer
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
# to save the fitted label encoder
with open('label_encoder.pickle', 'wb') as ecn_file:
    pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)
    
with open("Intents.json") as file:
    data = json.load(file)
# load trained model
model = keras.models.load_model('chat_model1')
# load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

  

def chat(msj):
    # parameters
    max_len = 20
   
    if msj != None:
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([msj]),
                                            truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                respuesta=(np.random.choice(i['responses']))

        print(tag)
        if tag == "PedirCita":
            respuesta+=":Cedula,Nombre,Correo electronico,Número de celular, Fecha (dd/mm/aaaa) y Hora (HH:MM)"
        ##print(msj,respuesta)
        if "@" in msj:
            cedula,nombre,correo,numero,fecha,hora = msj.split(',')
            fecha2=datetime.datetime.strptime(fecha.strip(), '%d/%m/%Y')
            hora2=datetime.datetime.strptime(hora.strip(), '%H:%M')  
            print(fecha2)
            create(fecha2,hora2,cedula,numero,correo,nombre)

        return respuesta
       

