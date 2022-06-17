import time
import random 
import os
os.system("cls")
def limparTela():{ os.system("cls")}

#Setup Variáveis
palavra = ""
acertos = 0
erros = 0
letrasChutadas = []
chuteCerto = []
chancesRestantes = 5
x = 0
dicas = 0


#Funções
def menuEscolhas():
    print('O que deseja? \n (1) Tentar uma letra \n (2) Pedir uma dica \n (3) Chutar a palavra')
    x = input()
    return x
def arquivo(x,y,z):
    arquivojogoforca = open("jogoforca.txt","r")
    historico = arquivojogoforca.readlines()
    historico.append(x)#palavra
    historico.append(y)#ganhador
    historico.append(z)#perdedor
    arquivojogoforca = open("jogoforca.txt", "w")
    arquivojogoforca.writelines(historico)

#Jogo
print("."*40)
print("BEM VINDO AO JOGO DA FORCA!!!")
print("."*40)
desafiante = str(input('Primeiramente, peço que digite o nome do desafiante:\n'))
competidor = str(input('Agora, peço que digite o nome do competidor:\n'))
print("Já podemos jogar? \n")
jogar = str(input('Sim ou Não: ')).upper()

limparTela()


if jogar == "SIM" or jogar == "S" or jogar == "Y" or jogar == "YES":
    print(desafiante,", cadastre aqui a palavra-chave e as dicas.")
    palavra = input("Digite palavra escolhida aqui: ").upper().strip()
    dica1 = input("Dê a primeira dica: ")
    dica2 = input("Dê a segunda dica: ")
    dica3 = input("Dê a terceira dica: ")
    

elif jogar == "NÃO" or jogar == "N" or jogar == "NO":
    exit()
else:
    print("Eu perguntei Sim ou Não!!")

palavraEmLista = list(palavra)
asteriscos = []
listaChute = []

for a in range(0,len(palavraEmLista)):
    asteriscos.append("*")

listaDescobertos = []

for y in range(0, len(palavraEmLista)):
    listaDescobertos.append('_')

limparTela()
iniciar = 1

while iniciar == 1:
    print('Erros: ',erros)
    print('')
    print("\n Você tem", chancesRestantes ,"chances para acertar a palavra :D")
    print(asteriscos)
    print('')
    print('Você já chutou: ',letrasChutadas)
    print('')
    x = menuEscolhas()
    if x == '1':
        chute = str(input("Que letras tem nessa palavra? Faça uma tentativa: ")).upper()

        if chute in letrasChutadas:
            palavraEmLista.append(chute)
            limparTela()
            print('Essa já foi, tenta outra!')
        elif chute in palavraEmLista:
            limparTela()
            print('Bom chute, acertou!')
            for i in range(0, len(palavra)):
                if chute == palavra[i]:
                     asteriscos[i] = chute
            letrasChutadas.append(chute)
        else:
            chancesRestantes = chancesRestantes - 1 
            erros = erros + 1
            letrasChutadas.append(chute)
            limparTela()
            print('Errouu')
            
    elif x == '2':
        try:
            if dicas == 0:
                limparTela()
                print('Aqui está sua Dica 1: ',dica1)
                dicas = dicas + 1
            elif dicas == 1:
                limparTela()
                print('Aqui está sua Dica 2: ',dica2)
                dicas = dicas + 1    
            elif dicas == 2:
                limparTela()
                print('Aqui está sua última Dica: ',dica3)
        except:
            pass
    elif x == '3':
        chuteFinal = input('Qual seu chute? ').upper() 
        if set(chuteFinal).issubset(set(palavraEmLista)):
            print('Parabéns! Você acertou!')
            print('')
            print(competidor, ' ganhou!!')
            break

    else:
        print('Número inválido')


chuteFinalLista = list(chuteFinal)

if chancesRestantes == 0:
    print('Você perdeu, ',competidor)
    print('Quem ganhou foi o ',desafiante)