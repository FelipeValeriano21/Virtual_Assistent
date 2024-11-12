import datetime

import pandas as pd

agenda = pd.read_excel("agenda.xlsx")
print(agenda)

descricao, responsavel, hora_agenda = [], [], []

for index, row in agenda.iterrows():
    #print(index)
    #print(row)
    data = datetime.datetime.date(row['data'])
    #print(data)
    hora_completa = datetime.datetime.strptime(str(row['hora']), '%H:%M:%S')
    #print(hora_completa)
    hora = datetime.datetime.time(hora_completa).hour
    #print(hora)

    if data_atual == data:
        if hora >= hora_atual:
            descricao.append(row['descricao'])
            responsavel.append(row['responsavel'])
            hora_agenda.append(row['hora'])


#print(descricao)
#print(responsavel)
#print(hora_agenda)

def carrega_agenda():
    if descricao:
        return descricao, responsavel, hora_agenda
    else:
        return False



if result in comandos[6]:
            playsound('n2.mp3')
            if carrega_agenda.carrega_agenda():
                speak('Estes são os eventos agendados para hoje:')
                for i in range(len(carrega_agenda.carrega_agenda()[1])):
                    speak(carrega_agenda.carrega_agenda()[1][i] + ' ' + carrega_agenda.carrega_agenda()[0][i] + ' agendada para as ' + str(carrega_agenda.carrega_agenda()[2][i]))
            else:
                speak('Não há eventos agendados para hoje a partir do horário atual!')




