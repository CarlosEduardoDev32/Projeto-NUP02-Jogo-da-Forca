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
name_user = str(input("Olá, seja bem-vindo(a) ao JOGO DA FORCA. \n Por gentileza, qual o seu nome? "))
print(f'Muito bem, {name_user}! Você deverá advinhar uma palavra com base em duas dicas. \n Para tanto, você terá 03 tentativas. Caso exceda o número de tentativas você terá falhado M-I-Z-E-R-A-V-E-L-M-E-N-T-E.')
go = str(input("Digite 1 para iniciar o jogo, ou 0 para desistir: "))
if go == '1':
  print(f"Está palavra possui {len(name)} caracteres e a seguinte descrição: ")
  print(tips)
  while True:
    response = input("Qual a palavra?")
    if response == name:
      print("Resposta correta!")
      break
    else:
      print("Resposta incorreta, tente novamente!")
else:
  print("Você escolheu a saída mais fácil. Adeus...")










    
