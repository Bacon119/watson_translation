import json

import requests

from const import URL, IDE_URL

from keys import username, password, model_id

text=input('Please Enter A Text:')

auth=(username, password)

params={'text':text, 'model_id':model_id}

headers={'Accept':'application/json'}

def language_identify():

    identified_language=requests.get(IDE_URL,auth=auth,params=params,headers=headers)
    print(identified_language.json())

def translate_text():

    response=requests.get(URL,auth=auth,params = params,headers=headers)

    print(response.json())

language_identify()
