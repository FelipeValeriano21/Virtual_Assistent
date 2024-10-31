import datetime
import pyttsx3
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

hour = datetime.datetime.now().strftime('%H:%M')
print("Hora:", hour)

date = datetime.date.today().strftime('%d de %B de %Y')
print("Data formatada:", date)

engine = pyttsx3.init()

engine.setProperty('rate', 150)  

engine.say(f"Hoje é {date}")
engine.runAndWait()
