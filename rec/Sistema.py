# -*- coding: utf-8 -*-
import math
from DataSetUsuarios import usuario
from DataSetCategorias import categoria

def manhattan (rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            return distance
        return "x"

def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            #esse if impede pessoas que nao tem lugares em comum de serem parecidos
            if distance != "x":
                distances.append((distance, user))
    distances.sort()
    return distances


def recommend(username, users, fylter):
    #aqui encontraremos os vizinhos proximos
    proximos = computeNearestNeighbor(username, users)[0][1]
    recomendacoes = []
    neighborRatings = users[proximos]
    userRatings = users[username]
    for jogo in neighborRatings:
        if not jogo in userRatings:
            recomendacoes.append((jogo, neighborRatings[jogo]))
    return sorted(recomendacoes,
                  key=lambda jogoTuple: jogoTuple[1],
                  reverse = True)


def Principal():
    cont = 0
    #Pega os dados no BD:
    users = usuario()
    #vai pegar os dados das categorias no BD:    
    tags = categoria()#usa com sabedoria felipe :)
    lista_jogos = ["Red Dead Redemption",
        "God of War",
        "Far Cry 5",
        "GTA 5",
        "Spider-Man",
        "League of Legends",
        "The Sims 4",
        "Battlefield V",
        "FIFA 19",
        "Overwatch",
        "Counter-Strike: Global Offensive",
        "Kingdom Hearts 3",
        "A lenda do Herói",
        "Relic Hunters",
        "House Flipper",
        "The Forest"]
    #parte dos inputs do usuario:
    jogos = []
    notas = []
    pessoa= input("Digite seu nome:\n")
    print("\nPerfil: ", pessoa)
    print("------------------------------------------")
    Menu_Jogos(lista_jogos)
    print("Informa pelo menos 2 jogos.\n")
    while(True):
        jogo = int(input("Digite o número do %d º jogo que deseja avaliar:\n" % (cont+1)))
        nota = int(input("Digite uma nota (de 0 a 5) para " + lista_jogos[jogo-1] + ":\n"))
        escolha = input("Deseja avaliar mais algum jogo?\n")
        escolha = escolha.upper()
        jogos.append(lista_jogos[jogo-1])
        notas.append(nota)
        if((escolha=="NÃO" or escolha=="NAO")):
            print("------------------------------------------")
            if(cont >= 1):
                break
            else:
                print("Informe o segundo jogo!")
        print("------------------------------------------")
        cont+=1
    #while(True):
    #    opcao = input("\nDeseja escolher alguma categoria?\n")
    #    opcao = opcao.upper()
    #    if(opcao == "SIM"):
    #        Menu_Categorias(tags)
    #        name = input("Qual categoria procura?\n")
    #        fylter = tags[name]
    #        break
    #    elif(escolha=="NÃO" or escolha=="NAO"):
    #        fylter = 'NAO'
    #        break
    #    else:
    #        print("Por favor, informe sim ou não como resposta\n")
        
    Novo_Usuario=dict(zip(jogos,notas))
    #adicionando informaçoes do usuario no BD:
    users[pessoa] = Novo_Usuario
    #chamamos a funçao recomendaçao e fazemos a recomendação ao usuario:
    print(computeNearestNeighbor(pessoa, users))
    Recomendacao = recommend(pessoa,users,fylter)
    return Recomendacao

def Menu_Categorias(tags):
    print("Categorias disponíveis:")
    cont = 0
    for i in tags:
        cont = cont + 1
        print("%d - %s" %(cont,i))
    print("\n")

def Menu_Jogos(jogos):
    print("Jogos disponíveis:")
    for i in range(0,len(jogos)):
        print("%d - %s" %(i+1,jogos[i]))
    print("\n")

def Recomendacao_historico(jogos,catego,recom):
    jogos_ordena = sorted(jogos, key=lambda jogoTuple: jogoTuple[1],reverse = True)
    most_games = []
    games_weight = []
    cont = 0
    for jog in jogos_ordena:
        for cat in catego:
            if(Verifica_em(jog,cat)):
                if(not cat in most_games):
                    most_games.append(cat)
                    games_weight.append(1);
                else:
                    games_weight[verifica_em_categoria(most_games,cat)] +=1
        cont = cont + 1
        if(cont = 5):
            break
    recom_pesos = []
    for i in recom:
        recom_pesos.append({

def verifica_em_categoria(first,second):
    for i in range(0,len(first):
        if(second == first[i]):
            return i

def Verifica_em(user,categorias):
    if user in cat):
        return True
    return False
 
def Mostrar():
    #recupera e mostra a recomendaçao ao usuario
    Rec=Principal()
    print(Rec)

Mostrar()

     



