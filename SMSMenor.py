#!/usr/bin/env python
# coding: utf-8

# # Diminuindo o tamanho do executável final - Ambiente Virtual
# 
# ### Objetivo
# 
# Para diminuir o tamanho do arquivo a ser distribuído no final, vamos criar um ambiente virtual para garantir que teremos apenas as bibliotecas importantes.
# 
# - Passo 1: Garantir que o código está funcionando
# - Passo 2: Criar o ambiente virtual
# - Passo 3: Executar o nosso código por dentro do ambiente virtual
# - Passo 4: Identificar erros e instalar bibliotecas que faltam, apenas as que o programa pede.
# - Passo 5: Instalar o pyinstaller e transformar em executável o programa Python

# In[ ]:


#rodar o código de um programa que fazemos durante o curso que funcione. Exemplo o do outlook de enviar email
from twilio.rest import Client

account_sid = 'AC274236461c28f62d429961289af45b82'
token = '6a2d1ea365d3674c749ce4cb7367d823'

client = Client(account_sid, token)

remetente = '+18126153399'
destino = '+5521972795556'

message = client.messages.create(
    to=destino, 
    from_=remetente,
    body="Coe, é o Lira aqui!")

print(message.sid)

