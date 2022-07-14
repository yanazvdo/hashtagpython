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
SAMPLE_RANGE_NAME = 'Página1!A1:A5'


def main():
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

#    try:
#        service = build('sheets', 'v4', credentials=creds)

#        # Call the Sheets API
#        sheet = service.spreadsheets()
#        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                    range=SAMPLE_RANGE_NAME).execute()
#        values = result.get('values', [])
#        print(values)

#        if not values:
#            print('No data found.')
#            return

#        print('Name, Major:')
#        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
#           print('%s, %s' % (row[0], row[4]))
#    except HttpError as err:
#        print(err)



    #A PARTIR DAQUI A GENTE VAI BRINCAR COM OS COMANDOS DO GOOGLE SHEET
        # Call the Sheets API
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range='Página1!A1:B5').execute()
        values = result.get('values', [])
        print(values)
    except:
        print(erro_do_yan)


    #COMO ADD VALORES NUMA GOOGLE PLANILHA:

    try:

        service = build('sheets', 'v4', credentials=creds)
        values = [
            [
                # Cell values ...
                'A1Y'
            ],
            # Additional rows ...
        ]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId="1PMkVjComwBTNlx0y-d6qIxfMt1sflNFHbsQot6u2kf4", range="PÁGINA1!A1",
            valueInputOption="USER_ENTERED", body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")

    except HttpError as error:
        print(f"An error occurred: {error}")




#ADD VALORES NO FINAL DA PLANILHA

    try:

        service = build('sheets', 'v4', credentials=creds)
        values = [
            [
                # Cell values ...
                'Yan', 'yan@yan.com', 'rico'
            ],
            [
                'Diego', 'diego@diego.com', 'pobre'
            ]
            # Additional rows ...
        ]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().append(
            spreadsheetId="1PMkVjComwBTNlx0y-d6qIxfMt1sflNFHbsQot6u2kf4", range="PÁGINA1!A1",
            valueInputOption="USER_ENTERED", body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")

    except HttpError as error:
        print(f"An error occurred: {error}")




#mini-desafio -> Recuperação de vendas da Hashtag






if __name__ == '__main__':
    main()