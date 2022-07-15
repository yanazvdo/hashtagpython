#MENTOLIRA

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# escolher a planilha que quer conectar e um range só para conferir se conectou
SAMPLE_SPREADSHEET_ID = '1PMkVjComwBTNlx0y-d6qIxfMt1sflNFHbsQot6u2kf4'
SAMPLE_RANGE_NAME = 'PRO_COMPRA_AUTO!A2:D10'


"""Shows basic usage of the Sheets API.
Prints values from a sample spreadsheet.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    print('Conexão bem sucecida')
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials_2.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())


#mini-desafio -> Recuperação de vendas da Hashtag

#Passo 1: Ler o intervalo de células
try:
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    print(values)
except:
    print(erro_do_yan)

#Passo 2: Verificar se o status está preenchido

linha = 2
for lista in values:
    # Passo 3: Se o status n tá preenchido verificar o problema
    if len(lista) < 4:
        # Passo 4: Enviar msg e registrar o novo status
        if lista[2] == 'Boleto Gerado':
            print('Enviar email para {}, email: {}'.format(lista[0], lista[1]))

            #Preencher a coluna status com a mensagem "Mensagem do boleto enviada"
            try:
                service = build('sheets', 'v4', credentials=creds)
                values = [
                    [
                        # Cell values ...
                        "Mensagem do boleto enviada"
                    ],
                    # Additional rows ...
                ]
                body = {
                    'values': values
                }
                result = service.spreadsheets().values().update(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="PRO_COMPRA_AUTO!D{}".format(linha),
                    valueInputOption="USER_ENTERED", body=body).execute()
                print(f"{result.get('updatedCells')} cells updated.")

            except HttpError as error:
                print(f"An error occurred: {error}")


        elif lista[2] == 'Comprou':
            #Vai preencher no status da planilha com "Compra finalizada"
            try:

                service = build('sheets', 'v4', credentials=creds)
                values = [
                    [
                        # Cell values ...
                        "Compra finalizada"
                    ],
                    # Additional rows ...
                ]
                body = {
                    'values': values
                }
                result = service.spreadsheets().values().update(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"PRO_COMPRA_AUTO!D{linha}",
                    valueInputOption="USER_ENTERED", body=body).execute()
                print(f"{result.get('updatedCells')} cells updated.")

            except HttpError as error:
                print(f"An error occurred: {error}")

        elif lista[2] == 'Sem Saldo':
            print('Enviar msg Sem saldo no cartão')
            try:
                service = build('sheets', 'v4', credentials=creds)
                values = [
                    [
                        # Cell values ...
                        "Msg sem saldo enviada"
                    ],
                    # Additional rows ...
                ]
                body = {
                    'values': values
                }
                result = service.spreadsheets().values().update(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"PRO_COMPRA_AUTO!D{linha}",
                    valueInputOption="USER_ENTERED", body=body).execute()
                print(f"{result.get('updatedCells')} cells updated.")

            except HttpError as error:
                print(f"An error occurred: {error}")
    linha = linha + 1








