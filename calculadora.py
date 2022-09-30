import time #Esse import serve para ativar a função sleep, que da um tempo para verificarmos o resultado.
import os  #Esse import serve para ativar o Clear, para limpar após executar/receber o resultado.

def soma(): #Criando a função de soma em "float" pois podem surgir números reais (quebrados) e na forma "int" não irá aparecer o restante após o ponto. 
  v1 = float(input("Digite um número: "))
  v2 = float(input("Digite um número: "))
  soma = v1 + v2
  print(soma)  
  time.sleep (1) #Aqui chamamos o sleep, já que temos a biblioteca importada conseguimos fazer com que ele funcione no código, sem apresentar erros.
  os.system('clear') #Aqui chamamos o clear, para que faça a limpeza da tela após dar o resultado.
  inicio()
def sub(): #Criando a função de subtração
  v1 = float(input("Digite um número: "))
  v2 = float(input("Digite um número: "))
  sub = v1 - v2
  print(sub)
  time.sleep (1)
  os.system('clear')
  inicio()
def mult(): #Criando a função de multiplicação
  v1 = float(input("Digite um número: "))
  v2 = float(input("Digite um número: "))
  mult = v1 * v2
  print(mult)
  time.sleep (1)
  os.system('clear')
  inicio()
def div(): #Criando a função de divisão
  v1 = float(input("Digite um número: "))
  v2 = float(input("Digite um número: "))
  div = v1 / v2
  print(div)
  time.sleep (1)
  os.system('clear')
  inicio()
def inicio(): #Criando a função de inicio
  #Após o Escolha colocamos o "str" para que as escolhas sejam ativavéis por STRINGER (Caracteres) 
  escolha = str(input("""Escolha uma operação: 
  [ "+" ] Soma
  [ "-" ] Subtração
  [ "*" ] Multiplicação
  [ "/" ] Divisão
  
  """))
  
  if escolha == "+":
    soma()
  elif escolha == "-":
    sub()
  elif escolha == "*":
    mult()
  elif escolha == "/":
    div()
  else:
    print("Esse valor não está na tabela, tente novamente!")
    time.sleep (1)
    os.system('clear')
    inicio() #Chamando a função inicio para recomeçar o programa caso o usuário escreva algum caractere ou outras coisas que não seja uma das opções a cima.
    
inicio() #Chamando a função inicio para começar o programa e inicar a calculadora.