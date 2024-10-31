import pyttsx3
import speech_recognition as sr
from playsound import playsound
import random
import datetime
import webbrowser as wb
import numpy as np
import librosa
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import locale
import pygame
import time
import requests
import os
sns.set()
import requests
from pydub import AudioSegment
from pydub.playback import play
import requests
from io import BytesIO
import datetime



def play_audio(url):

    response = requests.get(url)
    if response.status_code == 200:  
      
        temp_file = 'temp_audio.mp3'
        with open(temp_file, 'wb') as f:
            f.write(response.content)  
        
    
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file) 
        pygame.mixer.music.play()  

  
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10) 
        os.remove(temp_file)
        return None
   
    else:
        print("Falha ao baixar o áudio:", response.status_code)
        return None


def definirData(): 
  locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
  date = datetime.date.today().strftime('%d de %B meu amigo')
  return date

def definirHora():
    hour = datetime.datetime.now().strftime('%H:%M')
    return hour


def chamamusica(musica):
    url = f'https://deezerdevs-deezer.p.rapidapi.com/search?q={musica}'
    headers = {
        'X-RapidAPI-Key': '494f4935f7msh69281d3099327d6p1d498ejsn321e400c749f',
        'X-RapidAPI-Host': 'deezerdevs-deezer.p.rapidapi.com'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()

     
        if data['data']:
            item = data['data'][0]  
            artista = item['artist']['name']
            titulo = item['title']
            preview = item['preview']
            pyttsx3.speak(f"Tocando a música {titulo} de {artista}")
            print(f"Artista: {artista}")
            print(f"Título: {titulo}")
            print(f"Preview: {preview}")
            return preview  
        else:
            print("Nenhuma música encontrada.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None


from modules import comandos_respostas
comandos = comandos_respostas.comandos
respostas = comandos_respostas.respostas

meu_nome = 'lume'

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200) 
    engine.setProperty('volume', 1) 
    engine.say(audio)
    engine.runAndWait()

playsound('Alexa_Sound.mp3')

def listen_microphone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        audio = microfone.listen(source)
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    return frase

playing = False
mode_control = False
print('Lume iniciando...')
playsound('n1.mp3')
pyttsx3.speak(f"Me chamo Lume sou um assitente virtual")

while (1):
    result = listen_microphone()

    if meu_nome in result:
        result = str(result.split(meu_nome + ' ')[1])
        result = result.lower()
        print('Acionou a assistente!')
        print('Após o processamento: ', result)

        if result in comandos[0]:
            pyttsx3.speak('Até agora minhas funções são: ' + respostas[0])

        if result in comandos[1]:
            pyttsx3.speak('Agora são ' + definirHora())

        if result in comandos[2]:
            pyttsx3.speak('Hoje é dia ')
            pyttsx3.speak(definirData())

        if result in comandos[3]:
            playsound('Alexa_Sound.mp3')
            pyttsx3.speak('Diga uma musica para eu tocar ')
            musica = listen_microphone()
            playsound('Alexa_Sound.mp3')
            url = chamamusica(musica)
            play_audio(url)

        if result == 'encerrar':
            playsound('Alexa_Sound.mp3')
            pyttsx3.speak(''.join(random.sample(respostas[4], k = 1)))
            break
    else:
         playsound('Alexa_Sound.mp3')



playing = False
mode_control = False
playsound('Alexa_Sound.mp3')
print('\nPronto para começar!')
