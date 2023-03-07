# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:24:57 2022

@author: horstmann
"""

# Programa  cadastro pacientes consultório:
# O programa se baseia na manipulação de uma lista (chamada cad) composta por 
# várias sublistas, as quais contém as infos de cada paciente.
# A lista pode ser carregada de uma planilha do excel ou de um banco de dados.
# Nas sublistas dos dados dos pacientes sã£o organizados basicamente da seguinte
# forma: nome, telefone, Endereço, cpf, profissão, e-mail, dia próx consulta, 
# horário próx consulta, flag envio e-mail
# Capacidades do sw: cadastro de pacientes, agendamento/ reagendamento/ desmarcação de consultas, 
# visualização da agenda, visualização dos dados dos pacientes, envio de e-mail automático N dias 
# p/ paciente solicitando a confirmação de consulta e integração com google calendar

from __future__ import print_function

import pandas as pd   # importa o pandas para salvar os resultados numa planilha ou arquivo csv

import datetime #importa biblioteca para trabalhar com datas/ tempo

import smtplib

import email.message

import os.path

from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

from googleapiclient.errors import HttpError


# Função para inserir e alterar eventos do google calendar
# If modifying these scopes, delete the file token.json.
# Representa o escopo do que é permitido acessar
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar']

# Inputs: Nome paciente, data da consulta, data de término da consulta
def calendar(nome,data_inicial,data_final,operation,eid):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        if operation == 'insert':
 ######## Insere evento no calendário ######################
 # Summary: nome do evento, location: localização,description: descrição do evento,datetime: hora evento,
 # timeZone: fuso horário, recurrence: qtas vezes o evento se repete, attendees: participantes do evento, reminders: lembrete do evento
            event = {'summary': f'Paciente {nome}', 'location': 'Rua Conde de Bonfim,255, Tijuca, Rio de Janeiro, RJ', 'description': '',f'start': {'dateTime': f'{data_inicial}','timeZone': 'GMT-03:00',
  },
  'end': {
    'dateTime': f'{data_final}', # Data e hora de fim do evento
    'timeZone': 'GMT-03:00',       # Fuso horário (Brasília é GMT-03:00)
  },  
  'attendees': [     # Participantes do evento 
    {'email': 'XXXXXX@gmail.com'},
    
  ],
  # 'reminders': {   # Lembretes do evento
  #   'useDefault': False,
  #   'overrides': [
  #     {'method': 'email', 'minutes': 24 * 60}, # Notificação por e-mail enviado 1 dia antes
  #     {'method': 'popup', 'minutes': 10}, # Lembrete no celular 10 min antes
  #    ],
  #  },
 }

            event = service.events().insert(calendarId='primary', body=event).execute()
            #print ('Event created: %s' % (event.get('htmlLink')))
            print ('Event created: %s' % (event.get('id')))
            print("")
            return(event.get('id')) # retorna a idt do evento
                
############## Exclui os eventos da agenda: ##################################### 
        elif operation == 'del':
            event = service.events().delete(calendarId='primary', eventId=f'{eid}').execute()
            return
        
    except HttpError as error: # Se houver algum erro, o mesmo será mostrado
        print('An error occurred: %s' % error)


# Função que envia email para o paciente N dias antes da data da consulta
# Ordem dos parâmetros: 0-nome, 1-telefone, 2-endereço, 3-cpf, 4-profissão, 5-e-mail, 6-dia próx consulta,
# 7-horário próx consulta, 8-flag ctrl envio de e-mail

def enviar_email(email_dest, nome, dia, hora):      
        corpo_email = f"""
        <p>Prezado(a) {nome}, para melhor atendê-lo(a), solicito que confirme sua 
        consulta odontológica com a Dra Mariana Macedo agendada para o dia {dia} 
        às {hora}.</p>
        <p>A confirmação poderá ser realizada enviando mensagem para o whatsapp 
        021 xxxxx-xxxx ou respondendo este e-mail.</p> 
        <p>Agradecemos sua colaboração.</p>
        """
        
        msg = email.message.Message()
        #Assunto do e-mail
        msg['Subject'] = "Confirmação de agendamento de consulta odontológica" 
        msg['From'] = 'XXXXXX@gmail.com' #E-mail remetente
        msg['To'] = email_dest #E-mail destinatário
        #E-mail oculto
        recipients = ['YYYYY@gmail.com'] 
        password = 'gmail_app_password' #senha APP gmail
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )
            
        s = smtplib.SMTP('smtp.gmail.com', 587, timeout=120)
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']] + recipients, msg.as_string().encode('utf-8'))
        print('Email enviado')


def alerta(u, N): #Parâmetros de entrada lista de paciente e dias de antecedência
    hj = datetime.date.today()    
    for v in u:
        #Verifica se a flag ctrl está desabilitada, se a data da consulta está no 
        # intervalo de tempo desejado, se há consulta marcada e se há e-mail cadastrado  
        if (v[6] != 'n') and (v[8] == 'n') and (datetime.datetime.strptime(v[6],'%d/%m/%Y').date() - hj == datetime.timedelta(days = N)) and (v[6] != 'n') and (v[5] != 'n'): 
            print(v[0])
            enviar_email(v[5],v[0],v[6],v[7])
            v[8] = 's' #seta a flag para indicar o envio do e-mail ao paciente
            #print(cad)
        # Mostra msg ao operador caso o paciente não possua e-mail cadastrado 
        elif (v[6] != 'n') and (v[8] == 'n') and (datetime.datetime.strptime(v[6],'%d/%m/%Y').date() - hj == datetime.timedelta(days = N)) and (v[6] != 'n') and (v[5] == 'n'):
            print(f'Não foi possível enviar e-mail de confirmação para o(a) paciente {v[0]}, pois não há e-mail cadastrado! \n')


# Função que verifica se o dia digitado está no formato correto e se é posterior ao dia atual
def formato_data(d):
    while not ((len(d) == 10) and (d[2] == "/") and (d[5] == "/")):  #verifica se a data está no formato correto
        print("")    
        print('Dia inserido fora do formato correto.')
        d = input('Por favor, insira o dia da próxima consulta no formato DD/MM/AAAA: ')
    dt = datetime.datetime.strptime(d,'%d/%m/%Y').date()
    hj = datetime.date.today()
    while dt < hj: # Verifica se a data inserida é posterior ao dia atual
        print("")
        print('Foi inserida uma data anterior à data atual. Por favor, insira uma data válida.')
        d = input('Qual o novo dia da próxima consulta (formato DD/MM/AAAA)?')
        while not ((len(d) == 10) and (d[2] == "/") and (d[5] == "/")):  #verifica se a data está no formato correto
            print("")
            print('Dia inserido fora do formato correto.')
            d = input('Por favor, insira o dia da próxima consulta no formato DD/MM/AAAA: ')     
            d = formato_data(d)    
        dt = datetime.datetime.strptime(d,'%d/%m/%Y').date()
    return d


# Função que verifica se o horário selecionado está disponã­vel
# Dados entrada (lista cadastro de pacientes, dia e hora selecionados)
def verify(u, d, hr):
    w = (d, hr)
    d = formato_data(d)
    for v in u: #verifica se o horário desejado (dia e hora) já está ocupado                
        while (v[-1] == hr) and (v[-2] == d):        
            print('Já existe paciente marcado para a data selecionada \n')
            d = input('Qual o novo dia da próxima consulta (formato DD/MM/AAAA)? ')            
            d = formato_data(d)
            hr = input('Qual o novo horário da próxima consulta (formato HH:MM)? ')
            w = (d, hr)                  
    return w

    
# Função criada para indicar o elemento a ser selecionado na hora do ordenamento cronológico (mandrake do defltstack)
def thirdElement(element):
    return element[3]


# Função criada para identificar se o CPF foi inserido corretamente
# Input: entrada do cpf pelo usuário/ output: cpf no fortmato correto
def verif_cpf(val):
    flag = 0
    while flag == 0:
        if len(val) == 11:
            val = val[0:3]+'.'+ val[3:6]+'.'+ val[6:9]+'-'+val[9:11]
            flag = 1
        elif (len(val) == 14) and (val[3] =='.') and (val[7] =='.') and (val[11] =='-'):
            val = val
            flag = 1
        else:
            print('CPF inserido fora do formato correto.')
            val = input('Entre com o CPF do paciente (sem pontos e traços): ')
    return val


#Função que mostra os pacientes agendados
def agenda(u,n,t,d,hr):
#parâmetros: u->lista pacientes, n-> índice nome,t-> índice tel, d-> índice dia e hr-> índice hora)
    print(" ")
    print('Digite 1 para ver a agenda em um dia especí­fico')
    print('Digite 2 para ver todos os pacientes agendados\n')
    h = input('Entre com a opção desejada: ')
    print("")
    if h == '1': # Mostra os pacientes agendados num dia específico
        dia = input('Entre com o dia que deseja ver a agenda (formato DD/MM/AAAA): ')
        dia = formato_data(dia)
        print(" ")
        print(f'Pacientes dia {dia}\n')
        flag = 0
        lst = []
        for k in u:
            if k[d] == dia:  #seleciona apenas os pacientes do dia especificado
                data = datetime.datetime.strptime(k[d] + " " + k[hr], '%d/%m/%Y %H:%M') #coloca a data no formato adequado de forma que se possa organizar a lista em ordem cronológica
                lst.append([k[n], k[t], k[hr], data]) #Cria uma lista apenas com os pacientes do dia (nome, tel, hora e data)
                flag = 1
        if flag == 0:
                print(f'Não há pacientes agendados para o dia {dia}\n')
        lst = sorted(lst, reverse = True) #organiza a lista em ordem cronológica  
        for u in lst: # Mostra na tela em ordem cronológica os pacientes agendados 
                print(f'Paciente: {u[n]}')
                print(f'Telefone: {u[t]} ')
                print(f'Hora: {u[2]}\n') 
    if h == '2': # Mostra TODOS os pacientes agendados       
        flag = 0
        lst = []
        for k in u:
            if k[d] != "n":  #seleciona apenas os pacientes agendados
                data = datetime.datetime.strptime(k[d] + " " + k[hr], '%d/%m/%Y %H:%M').date() #coloca a data no formato adequado de forma que se possa organizar a lista em ordem cronológica
                hj = datetime.date.today()
                if data >= hj:
                    lst.append([k[n], k[t], k[hr], data, k[d]]) #Cria uma lista apenas com os pacientes do dia (nome, tel, hora e data)
                    flag = 1
        if flag == 0:
                print('Não há pacientes agendados \n')
        lst =  sorted(lst, key = thirdElement) #organiza a lista em ordem cronológica  
        if lst != []:
            dia = lst[0][4]
            print(f'Consulta do dia {dia}')
        for u in lst: # Mostra na tela em ordem cronológica os pacientes agendados 
            if u[4] == dia:         
                print(f'Paciente: {u[n]}')
                print(f'Telefone: {u[t]} ')
                print(f'Hora: {u[2]}\n')
            else: 
                dia = u[4]
                print(f'Consulta do dia {dia}')
                print(f'Paciente: {u[n]}')
                print(f'Telefone: {u[t]} ')
                print(f'Hora: {u[2]}\n')


# Função para buscar nome numa lista dentro de outra
# Input: nome ou CPF do paciente e lista com dados dos pacientes
# Output: lista contendo os índices (referentes à lista de entrada) dos resultados 
# encontrados
def busca(nome, u):
    lst =[]
    j = 0
    for k in u:
        for v in k:
            if nome in v:
# cria uma lista contendo o índice de onde se encontra o paciente na lista cad
                lst.append(j)
        j += 1
    return(lst)


# Função para mostrar dados específicos do paciente
# Inputs: lista com dados dos pacientes e índice do paciente dentro da lista
def dados_paciente(cad,k): 
    print(f'Paciente: {cad[k][0]}')
    print(f'Telefone: {cad[k][1]}')
    print(f'Endereço: {cad[k][2]}')
    print(f'CPF: {cad[k][3]}')
    print(f'Profissão: {cad[k][4]}')
    print(f'E-mail: {cad[k][5]}')
    print(f'Dia próxima consulta: {cad[k][6]}')
    print(f'Hora próxima consulta: {cad[k][7]} \n')


#Iní­cio do programa principal
#Importação da planilha de pacientes ou cria uma lista vazia
ans = input('Deseja importar dados dos pacientes, s ou n?').upper()
if ans != 'N':
    # Lendo arquivo .xlsx
    df = pd.read_excel('pacientes.xlsx')
    #df = pd.read_excel('pacientes.xlsx', converters= {'CPF':str}) # Lê um arquivo do excel contendo umData arquivo do código e arquivo de dados estão na mesma pasta, não preciso do caminho do arquivo
    df = df.astype(str) # Converte os dados do Dataframe para string
    # Lendo arquivo .csv https://realpython.com/python-csv/
    #df = pd.read_csv('pacientes.csv')
    cad = df.values.tolist() # transforma o dataframe numa lista
    
else:
    cad = [] # Cria nova lista caso não se deseje importar informações antigas   

i = '1'

while (i != '0'):
    alerta(cad, 2) # envia e-mail de alerta ao paciente solicitando confirmação de consulta 
    print(50*'=')
    print("Sistema de cadastro de pacientes do consultório da Dra Mariana Macêdo \n")
    print(50*'=')
    print('Selecione a operação desejada: \n')
    print('Digite 1 para cadastrar novo paciente')
    print('Digite 2 para agendar, reagendar ou desmarcar consulta')
    print('Digite 3 para buscar dados do paciente')
    print('Digite 4 para atualizar dados dos pacientes')
    print('Digite 5 para ver agenda')
    print('Digite 6 para listar todos os pacientes')
    print('Digite 0 para sair \n')
    i = input('Selecione a opção desejada: ')
    print("")
    if i == '1': #Cadastra novo paciente
       nome = input('Entre com o nome do paciente: ').upper()
       tel = input('Entre com o telefone do paciente: ')
       if tel == "":
           tel = 'n'
       end = input('Entre com o Endereço do paciente: ')
       if end == "":
           end = 'n'
       cpf = input('Entre com o CPF do paciente (sem pontos e traços): ')
       if cpf == "":
           cpf = 'n'
       else:
           cpf = verif_cpf(cpf)
       prof = input('Entre com a profissão do paciente: ')
       if prof == "":
           prof = 'n'
       e_mail = input('Entre com o e-mail do paciente: ')
       if e_mail == "":
           e_mail = 'n'
       choice = input('Deseja agendar consulta (s ou n)? ').upper()
       if choice == 'N': # Caso não se deseje marcar consulta          
          cad.append([nome, tel, end, cpf, prof, e_mail,"n","n","n","n"])
          print("")
          print(f'Paciente {nome} cadastrado com sucesso!\n')
       else:
          dia = input('Qual o dia da próxima consulta (formato DD/MM/AAAA)? ')
          dia = formato_data(dia)
          hora = input('Qual o horário da próxima consulta (formato HH:MM)? ')             
          w = verify(cad, dia, hora)  
          #cad.append([nome, tel, end, cpf, prof, e_mail, w[0], w[1],'n','n'])
          # Salva consulta no google calendar
          # Data inicial do evento
          dti = datetime.datetime.strptime(w[0]+''+w[1]+':00','%d/%m/%Y%H:%M:%S')
          # Data final do evento
          dtf = dti + datetime.timedelta(hours = 1)
          # Coloca as datas no formato RFC 3339 adotado pela API do Google
          dti, dtf = dti.isoformat('T')+'-03:00', dtf.isoformat('T')+'-03:00' 
          # Insere novo evento no google calendar e salva id do evento 
          eid = calendar(nome,dti,dtf,'insert','')
          cad.append([nome, tel, end, cpf, prof, e_mail, w[0], w[1],'n',eid])
          print("")
          print(f'Paciente {nome} agendado para o dia {w[0]} às {w[1]} horas!\n')
    elif i == '2': #agenda consulta
               pac = input('Qual o nome ou cpf do paciente que deseja desmarcar, agendar ou reagendar consulta? ').upper()
               print(" ")
# Se a entrada for CPF sem pontos e traço. Buscando por CPF, ou é encontrado 1 paciente ou nenhum
               if pac.isnumeric(): 
                   cpf = verif_cpf(pac)
                   n = busca(cpf, cad) # busca dados do paciente dentro da lista
                   if len(n) == 0: # se não for encontrado nenhum resultado
                       print('Paciente não encontrado com os dados informados.\n')
                   elif len(n) == 1: 
                       # Rotina para desmarcar consulta
                       dados_paciente(cad,n[0]) # mostra dados do paciente
                       print('Digite 1 para desmarcar consulta.\n')
                       print('Digite 2 para reagendar ou agendar nova consulta.\n')
                       opc = input('Selecione a opção desejada: ')
                       if opc == '1':  # Desmarca consulta
                           calendar("","","",'del',cad[n[0]][9]) # desmarca consulta do calendar    
                           cad[n[0]][6] , cad[n[0]][7], cad[n[0]][9] = 'n', 'n', 'n'
                           cad = cad
                           print("")
                           dados_paciente(cad,n[0]) # mostra dados do paciente
                       elif opc == '2': # Agenda nova consulta ou reagenda consulta                           
                               consulta = input('Para qual data deseja reagendar ou agendar a consulta (formato DD/MM/AAAA)? ')
                               consulta = formato_data(consulta)
                               hora = input('Para qual o horário deseja reagendar ou agendar a consulta (formato HH:MM)? ')
                               print("")
                               cad[n[0]][6], cad[n[0]][7] = verify(cad, consulta, hora)
                               print(cad[n[0]][6], cad[n[0]][7])
                               cad = cad
                               if cad[n[0]][9] != 'n':
                                   calendar("","","",'del',cad[n[0]][9]) # desmarca consulta do calendar
                               # Salva consulta no google calendar
                               # Data inicial do evento
                               dti = datetime.datetime.strptime(cad[n[0]][6]+''+cad[n[0]][7]+':00','%d/%m/%Y%H:%M:%S')
                               # Data final do evento
                               dtf = dti + datetime.timedelta(hours = 1)
                               # Coloca as datas no formato RFC 3339 adotado pela API do Google
                               dti, dtf = dti.isoformat('T')+'-03:00', dtf.isoformat('T')+'-03:00' 
                               # Insere novo evento no google calendar e salva id do evento 
                               eid = calendar(cad[n[0]][0],dti,dtf,'insert','')
                               print("")
                               cad[n[0]][9] = eid # Salva idt do evento do calendar
                               dados_paciente(cad,n[0]) # mostra dados do paciente
                       # elif opc == '3': # Agenda nova consulta                          
                       #         consulta = input('Qual a data da nova consulta (formato DD/MM/AAAA)? ')
                       #         consulta = formato_data(consulta)
                       #         hora = input('Qual o horário da nova consulta (formato HH:MM)? ')
                       #         print("")
                       #         cad[n[0]][6], cad[n[0]][7] = verify(cad, consulta, hora)
                       #         print(cad[n[0]][6], cad[n[0]][7])
                       #         cad = cad
                       #         # Salva consulta no google calendar
                       #         # Data inicial do evento
                       #         dti = datetime.datetime.strptime(cad[n[0]][6]+''+cad[n[0]][7]+':00','%d/%m/%Y%H:%M:%S')
                       #         # Data final do evento
                       #         dtf = dti + datetime.timedelta(hours = 1)
                       #         # Coloca as datas no formato RFC 3339 adotado pela API do Google
                       #         dti, dtf = dti.isoformat('T')+'-03:00', dtf.isoformat('T')+'-03:00' 
                       #         # Insere novo evento no google calendar e salva id do evento 
                       #         eid = calendar(cad[n[0]][0],dti,dtf,'insert','')
                       #         print("")
                       #         cad[n[0]][9] = eid # Salva idt do evento do calendar
                       #         dados_paciente(cad,n[0]) # mostra dados do paciente                              
                   elif len(n) > 1: # Se houverem mais de 1 paciente com o mesmo cpf
                       print('Erro no cadastro, pois há mais de um paciente cadastrado com o mesmo CPF.')
               else: # Busca por nome, podem haver várias opções
                   n = busca(pac, cad) # busca dados do paciente dentro da lista
                   if len(n) > 1: # Se a busca resultar em mais de 1 resultado
                       print(f'Foram encontrados {len(n)} pacientes com os dados informados.\n')
                       for i in range(len(n)):
                           print(f'Para selecionar o paciente {cad[n[i]][0]} digite {i}\n')
                       w = int(input("Selecione a opção desejada: "))
                       dados_paciente(cad,n[w])
                       print('Digite 1 para desmarcar consulta.\n')
                       print('Digite 2 para reagendar ou agendar nova consulta.\n')
                       opc = input('Selecione a opção desejada: ')
                       if opc == '1': # Desmarca consulta
                           calendar("","","",'del',cad[n[w]][9]) # desmarca consulta do calendar
                           cad[n[w]][6] , cad[n[w]][7], cad[n[w]][9] = 'n', 'n', 'n'
                           cad = cad
                           print("")
                           dados_paciente(cad,n[w]) # mostra dados do paciente
                       elif opc == '2': # Agenda nova consulta ou reagenda consulta
                           consulta = input('Para qual dia deseja agendar ou reagendar a consulta (formato DD/MM/AAAA)? ')
                           consulta = formato_data(consulta)
                           hora = input('Para qual horário deseja agendar ou reagendar a consulta (formato HH:MM)? ')
                           print("")
                           cad[n[w]][6], cad[n[w]][7] = verify(cad, consulta, hora)
                           print(cad[n[w]][6], cad[n[w]][7])
                           cad = cad
                           if cad[n[w]][9] != 'n':
                               calendar("","","",'del',cad[n[w]][9]) # desmarca consulta do calendar
                           # Salva consulta no google calendar
                           # Data inicial do evento
                           dti = datetime.datetime.strptime(cad[n[w]][6]+''+cad[n[w]][7]+':00','%d/%m/%Y%H:%M:%S')
                           # Data final do evento
                           dtf = dti + datetime.timedelta(hours = 1)
                           # Coloca as datas no formato RFC 3339 adotado pela API do Google
                           dti, dtf = dti.isoformat('T')+'-03:00', dtf.isoformat('T')+'-03:00' 
                           # Insere novo evento no google calendar e salva id do evento 
                           eid = calendar(cad[n[w]][0],dti,dtf,'insert','')
                           print("")
                           cad[n[w]][9] = eid # Salva idt do evento do calendar
                           print("")
                           dados_paciente(cad,n[w])   
                   elif len(n) == 1:
                        dados_paciente(cad,n[0])
                        print('Digite 1 para desmarcar a consulta.\n')
                        print('Digite 2 para agendar uma nova consulta ou reagendá-la.\n')
                        opc = input('Selecione a opção desejada: ')
                        #resp = input(f'Deseja agendar nova consulta para {cad[n[0]][0]}, sim ou não?' ).upper()
                        if opc == '1':
                           calendar("","","",'del',cad[n[0]][9]) # desmarca consulta do calendar
                           cad[n[0]][6] , cad[n[0]][7], cad[n[0]][9] = 'n', 'n', 'n'
                           cad = cad
                           print("")
                           dados_paciente(cad,n[0]) # mostra dados do paciente
                        else:
                           consulta = input('Qual a data da próxima consulta (formato DD/MM/AAAA)? ')
                           consulta = formato_data(consulta)
                           hora = input('Qual o horário da próxima consulta (formato HH:MM)? ')
                           print("")
                           cad[n[0]][6], cad[n[0]][7] = verify(cad, consulta, hora)
                           print(cad[n[0]][6], cad[n[0]][7])
                           cad = cad
                           if cad[n[0]][9] != 'n':
                               calendar("","","",'del',cad[n[0]][9]) # desmarca consulta do calendar
                           # Salva consulta no google calendar
                           # Data inicial do evento
                           dti = datetime.datetime.strptime(cad[n[0]][6]+''+cad[n[0]][7]+':00','%d/%m/%Y%H:%M:%S')
                           # Data final do evento
                           dtf = dti + datetime.timedelta(hours = 1)
                           # Coloca as datas no formato RFC 3339 adotado pela API do Google
                           dti, dtf = dti.isoformat('T')+'-03:00', dtf.isoformat('T')+'-03:00' 
                           # Insere novo evento no google calendar e salva id do evento 
                           eid = calendar(cad[n[0]][0],dti,dtf,'insert','')
                           cad[n[0]][9] = eid # Salva idt do evento do calendar
                           print("")
                           dados_paciente(cad,n[0])
                   elif len(n) == 0:        
                       print('Paciente não encontrado com os dados informados.\n')
    elif i == '3': #busca dados paciente
           pac = input('Qual o nome ou cpf do paciente que deseja buscar? ').upper()
           print(" ")
           if pac.isnumeric(): # Se a entrada for CPF sem pontos e traço
               cpf = verif_cpf(pac)
               n = busca(cpf, cad) # Se a busca for por CPF só haverá uma resposta
               if len(n) == 0:
                   print('Paciente não encontrado com os dados informados.\n')
               else:
                   dados_paciente(cad,n[0]) # mostra dados do paciente
           else: # Busca por nome, podem haver várias opções ou apenas uma
               n = busca(pac, cad)
               if len(n) > 1: # Se a busca resultar em mais de 1 resultado
                   print(f'Foram encontrados {len(n)} pacientes com os dados informados.\n')
                   for i in range(len(n)):
                       print(f'Para selecionar o paciente {cad[n[i]][0]} digite {i}\n')
                   w = int(input("Selecione a opção desejada: "))
                   dados_paciente(cad,n[w])
               elif len(n) == 1:
                   dados_paciente(cad,n[0])
               elif len(n) == 0:
                   print('Paciente não encontrado com os dados informados.\n')
    elif i == '4': #atualiza dados contato
               pac = input('Qual o nome ou cpf do paciente que deseja atualizar os dados? ').upper()
               print(" ")
               if pac.isnumeric(): # Se a entrada for CPF sem pontos e traço
                   cpf = verif_cpf(pac)
                   n = busca(cpf, cad) # Se a busca for por CPF só haverá uma resposta               
                   if len(n) == 0:
                       print('Paciente não encontrado com os dados informados.\n')
                   else:
                       dados_paciente(cad,n[0]) # mostra dados do paciente
                   print('Digite 1 para atualizar o nome do paciente')
                   print('Digite 2 para atualizar o telefone do paciente')
                   print('Digite 3 para atualizar o Endereço do paciente')
                   print('Digite 4 para atualizar o cpf do paciente')
                   print('Digite 5 para atualizar a profissão do paciente')
                   print('Digite 6 para atualizar o e-mail do paciente')
                   print('Digite 0 para retornar ao menu anterior \n')
                   v = input('Selecione a opção desejada: ')
                   print(" ")
                   if v == '0': #retorna ao menu anterior        
                          print('Retornando ao menu anterior... \n')
                   elif v == '1': #atualiza nome paciente
                           dado = input('Qual o nome correto do paciente? ').upper()
                           cad[n[0]][0] = dado 
                   elif v == '2': #atualiza telefone paciente
                           dado = input('Qual o novo telefone do paciente? ')
                           cad[n[0]][1] = dado
                   elif v == '3': #atualiza Endereço paciente
                           dado = input('Qual o novo Endereço do paciente? ')
                           cad[n[0]][2] = dado
                   elif v == '4': #atualiza cpf paciente
                           dado = input('Qual o cpf correto do paciente? ')
                           dado = verif_cpf(dado)
                           cad[n[0]][3] = dado
                   elif v == '5': #atualiza profissão paciente
                           dado = input('Qual a profissão correta do paciente? ')
                           cad[n[0]][4] = dado
                   elif v == '6': #atualiza e-mail paciente
                           dado = input('Qual o novo e-mail do paciente? ')
                           cad[n[0]][5] = dado     
                   print(" ")
                   print(cad[n[0]])
               else: # Busca por nome, podem haver várias opções ou apenas uma
                   n = busca(pac, cad)
                   if len(n) > 1: # Se a busca resultar em mais de 1 resultado
                       print(f'Foram encontrados {len(n)} pacientes com os dados informados.\n')
                       for i in range(len(n)):
                           print(f'Para selecionar o paciente {cad[n[i]][0]} digite {i}\n')
                       w = int(input("Selecione a opção desejada: "))
                       dados_paciente(cad,n[w]) # mostra dados do paciente
                       print('Digite 1 para atualizar o nome do paciente')
                       print('Digite 2 para atualizar o telefone do paciente')
                       print('Digite 3 para atualizar o Endereço do paciente')
                       print('Digite 4 para atualizar o cpf do paciente')
                       print('Digite 5 para atualizar a profissão do paciente')
                       print('Digite 6 para atualizar o e-mail do paciente')
                       print('Digite 0 para retornar ao menu anterior \n')
                       v = input('Selecione a opção desejada: ')
                       print(" ")
                       if v == '0': #retorna ao menu anterior        
                          print('Retornando ao menu anterior... \n')
                       elif v == '1': #atualiza nome paciente
                           dado = input('Qual o nome correto do paciente? ').upper()
                           cad[n[w]][0] = dado 
                       elif v == '2': #atualiza telefone paciente
                           dado = input('Qual o novo telefone do paciente? ')
                           cad[n[w]][1] = dado
                       elif v == '3': #atualiza Endereço paciente
                           dado = input('Qual o novo Endereço do paciente? ')
                           cad[n[w]][2] = dado
                       elif v == '4': #atualiza cpf paciente
                           dado = input('Qual o cpf correto do paciente? ')
                           dado = verif_cpf(dado)
                           cad[n[w]][3] = dado
                       elif v == '5': #atualiza profissão paciente
                           dado = input('Qual a profissão correta do paciente? ')
                           cad[n[w]][4] = dado
                       elif v == '6': #atualiza e-mail paciente
                           dado = input('Qual o novo e-mail do paciente? ')
                           cad[n[w]][5] = dado     
                       print(" ")
                       print(cad[n[w]])
                   elif len(n) == 1:
                       dados_paciente(cad,n[0]) # mostra dados do paciente
                       print('Digite 1 para atualizar o nome do paciente')
                       print('Digite 2 para atualizar o telefone do paciente')
                       print('Digite 3 para atualizar o Endereço do paciente')
                       print('Digite 4 para atualizar o cpf do paciente')
                       print('Digite 5 para atualizar a profissão do paciente')
                       print('Digite 6 para atualizar o e-mail do paciente')
                       print('Digite 0 para retornar ao menu anterior \n')
                       v = input('Selecione a opção desejada: ')
                       print(" ")
                       if v == '0': #retorna ao menu anterior        
                          print('Retornando ao menu anterior... \n')
                       elif v == '1': #atualiza nome paciente
                           dado = input('Qual o nome correto do paciente? ').upper()
                           cad[n[0]][0] = dado 
                       elif v == '2': #atualiza telefone paciente
                           dado = input('Qual o novo telefone do paciente? ')
                           cad[n[0]][1] = dado
                       elif v == '3': #atualiza Endereço paciente
                           dado = input('Qual o novo Endereço do paciente? ')
                           cad[n[0]][2] = dado
                       elif v == '4': #atualiza cpf paciente
                           dado = input('Qual o cpf correto do paciente? ')
                           dado = verif_cpf(dado)
                           cad[n[0]][3] = dado
                       elif v == '5': #atualiza profissão paciente
                           dado = input('Qual a profissão correta do paciente? ')
                           cad[n[0]][4] = dado
                       elif v == '6': #atualiza e-mail paciente
                           dado = input('Qual o novo e-mail do paciente? ')
                           cad[n[0]][5] = dado     
                       print(" ")
                       print(cad[n[0]])
                   elif len(n) == 0:
                        print('Paciente não encontrado com os dados informados.\n')                
    elif i == '5': #mostra agenda 
        agenda(cad,0,1,6,7)      
        print(" ") 
    elif i == '6': 
        pacientes = pd.DataFrame(cad, columns=['Paciente','Telefone','Endereço','CPF',
                                               'profissão','e-mail','Data prox consulta',
                                               'Hora prox consulta','E-mail alerta','Event id'])
        print(pacientes)
     
    # Cria um frame de dados (tabela) do cadastro de pacientes 
    pacientes = pd.DataFrame(cad, columns=['Paciente','Telefone','Endereço','CPF',
                                           'profissão','e-mail','Data prox consulta',
                                           'Hora prox consulta','E-mail alerta','Event id'])
    pacientes = pacientes.astype(str) # Converte os dados do Dataframe para string

# Salva o frame de dados num arquivo excel chamado pacientes sem mostrar o índice (index = False)
    pacientes.to_excel('pacientes.xlsx', index=False)
    #pacientes.to_excel('pacientes.xlsx', index=False,converters= {'CPF':str})