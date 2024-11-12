#importando bibliotecas

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


# Excluir um item especifico 
def excluirItem():
    item = listen_microphone()
    print("O item que pediu para excluir é " + item)


# Listar lista de compras 
def listarItens():
    df = pd.read_excel('agenda/lista_de_compras.xlsx')
    itens_para_falar = ', '.join(df['produtos'].astype(str))
    engine = pyttsx3.init()
    engine.say(f"Os itens na lista são: {itens_para_falar}")
    engine.runAndWait()
    

def limparLista():
    df = pd.read_excel('agenda/lista_de_compras.xlsx')
    df_limpo = df.head(0) 
    df_limpo.to_excel('agenda/lista_de_compras.xlsx', index=False)
    pyttsx3.speak("LImpeza de lista realizada com sucesso")



def adicionarItem():
    pyttsx3.speak("Diga um produto para ser adicionado")
    item = listen_microphone()
    speak(''.join(random.sample(respostas[1], k=1)))

    df = pd.read_excel('agenda/lista_de_compras.xlsx')
    if 'id' in df.columns:
        df = df.drop(columns=['id'])
    nova_linha = pd.DataFrame({'produtos': [item]})
    df = pd.concat([df, nova_linha], ignore_index=True)

    df.to_excel('agenda/lista_de_compras.xlsx', index=False)
    print("Nova linha adicionada e arquivo salvo com sucesso!")
    pyttsx3.speak(item + "adicionado na lista com sucesso")

# Função para consultar a temperatura de uma cidade

def consultaTemperatura(cidade):
    parameters = {
        'key': 'jkqxgezgq3adgvx8hksv2k9wky7a6i48w3hb4vif',  
        'place_id': cidade
    }
    url = "https://www.meteosource.com/api/v1/free/point"
    response = requests.get(url, params=parameters)
    data = response.json()
    pyttsx3.speak('A temperatura atual em' + cidade + ' é {} ° Celsius.'.format(data['current']['temperature']))


# Função para tocar uma musica
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

# Função para dizer a data de hoje
def definirData(): 
  locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
  date = datetime.date.today().strftime('%d de %B meu amigo')
  return date

def definirHora():
    hour = datetime.datetime.now().strftime('%H:%M')
    return hour


# Função para buscar uma musica
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

# Função para falar
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200) 
    engine.setProperty('volume', 1) 
    engine.say(audio)
    engine.runAndWait()

playsound('Alexa_Sound.mp3')


# Função para gravar audio
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
print('Tudo pronto')
playsound('n1.mp3')
pyttsx3.speak(f"Me chamo Lume sou um assistente virtual, vamos começar")
pyttsx3.speak(f"Me pergunte")


# Loop assitente
while (1):
    result = listen_microphone()

    if meu_nome in result:
        result = str(result.split(meu_nome + ' ')[1])
        result = result.lower()
        print('-------------------Acionou a assistente!-------------------')
        print('-------------------Após o processamento: ', result)

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

        if result in comandos[4]:
            playsound('Alexa_Sound.mp3')
            pyttsx3.speak('Diga a cidade que gostaria de saber a temperatura')
            cidade = listen_microphone()
            playsound('Alexa_Sound.mp3')
            temperatura = consultaTemperatura(cidade)
            

        # Lista de Compras
        if result in comandos[5]:
            playsound('Alexa_Sound.mp3')
            speak('Pode falar!')
            result = listen_microphone()
            anotacao = open('anotacao.txt', mode='a+', encoding='utf-8')
            anotacao.write(result + '\n')
            anotacao.close()
            speak(''.join(random.sample(respostas[1], k=1)))
            speak('Deseja que eu leia os lembretes?')
            result = listen_microphone()
            if result == 'sim' or result == 'pode ler':
                with open('anotacao.txt') as file_source:
                    lines = file_source.readlines()
                    for line in lines:
                        speak(line)
            else:
                speak('Ok!')

        if result in comandos[6]:
           playsound('Alexa_Sound.mp3')
           pyttsx3.speak('listar, adicionar ou limpar')
           elemento = listen_microphone()

           match elemento:
             case "listar":
                   listarItens()  
             case "adicionar": 
                  adicionarItem()
             case "limpar":
                   limparLista()      
             case "excluir elemento":
                   excluirItem()     
             case _:
                    print("dsadsa")


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
