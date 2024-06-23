import json
import requests #importando a biblioteca capaz de realizar requisições.
address = "https://raw.githubusercontent.com/CarlosEduardoDev32/arquivo.json/main/arquivo.json"
content = requests.get(address)
data = content.json()
len(data)
type(data)
import random
secret_value = random.choice(data)
tips = secret_value["dica"]
name = secret_value["palavra"]
print(f"Está palavra possui {len(name)} caracteres e a seguinte descrição: ")
print(tips)
while True:
  response = input("Qual a palavra?")
  if response == name:
    print("Resposta correta!")
    break
  else:
    print("Resposta incorreta, tente novamente!")










    # "https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json"