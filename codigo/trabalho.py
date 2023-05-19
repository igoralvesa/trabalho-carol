import os
from funcao import menu
from funcao import tabelacategoria
dicnatalia = {"CASA" : [], "USOPESSOAL" : [], "TRANSPORTE" : [], "COMIDA" : []}
decisao = int(input("voce deseja entrar no menu? [ 1- SIM, 2- NÃO ] "))

while decisao == 1:
    menu()

    pergunta = int(input("o que voce deseja realizar? "))
    if pergunta == 1:
        tabelacategoria()
        escolhacategoria = int(input("O gasto se encaixa em qual categoria? "))
        arquivo = open("dados.csv", "r+")
        
        if escolhacategoria == 1:
            nome = input("Com o que você gastou? ")
            valor = input("Quanto custou? ")
            dicnatalia["CASA"].append(nome)  
            dicnatalia["CASA"].append(valor)
            arquivo.write(",".join([nome, valor]))  
               
            
        elif escolhacategoria == 2:
            nome = input("Com o que você gastou? ")
            valor = input("Quanto custou? ")
            arquivo.write(",".join([nome, valor]))  
            dicnatalia["USOPESSOAL"].append(valor)   
            
        elif escolhacategoria == 3:
            nome = input("Com o que você gastou? ")
            valor = input("Quanto custou? ")
            arquivo.write(",".join([nome, valor]))  
            dicnatalia["TRANSPORTE"].append(valor)   
            
        elif escolhacategoria == 4:
            nome = input("Com o que você gastou? ")
            valor = input("Quanto custou? ")
            arquivo.write(",".join([nome, valor]))  
            dicnatalia["COMIDA"].append(valor)   
            arquivo.close()
        else:
            print("categoria inválida, insira novamente!")
        arquivo.write(f"{dicnatalia['CASA']}, {dicnatalia['USOPESSOAL']}, {dicnatalia['TRANSPORTE']}, {dicnatalia['COMIDA']}\n")

    elif pergunta == 2:
        tabelacategoria()
        escolhaler = int(input("Digite a categoria que você deseja ver os gastos: "))
        if escolhaler == 1:
            
              with open("dados.csv", "r") as arquivo:
                  for linha in arquivo:
                   for item in dicnatalia["CASA"]:
                      if item in linha:
                       print(linha.strip())
           
        elif escolhaler == 2:
            print("Seus gastos com COMIDA foram: ", dicnatalia["COMIDA"])
        elif escolhaler == 3:
            print("Seus gastos com TRANSPORTE foram: ", dicnatalia["TRANSPORTE"])
        elif escolhaler == 4:
            print("Seus gastos com USO PESSOAL foram: ", dicnatalia["USOPESSOAL"])
        
    print("retornando ao menu.....")
