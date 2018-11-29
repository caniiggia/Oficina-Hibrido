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
    for turistico in neighborRatings:
        if not turistico in userRatings:
            if fylter != "NAO" and turistico in fylter:
                recomendacoes.append((turistico, neighborRatings[turistico]))
            elif fylter == "NAO":
                recomendacoes.append((turistico, neighborRatings[turistico]))
    return sorted(recomendacoes,
                  key=lambda turisticoTuple: turisticoTuple[1],
                  reverse = True)

def Principal():
    cont = 0
    #Pega os dados no BD:
    users = usuario()
    #vai pegar os dados das categorias no BD:    
    filtros = categoria()#usa com sabedoria felipe :)
    #parte dos inputs do usuario:
    lugares = []
    notas = []
    pessoa= input("Digite seu nome:\n")
    print("\nPerfil: ", pessoa)
    print("------------------------------------------")
    Menu_Lugares()
    while(True):
        lugar = input("Digite seu lugar turístico " + str(cont+1) + ":\n")
        nota = int(input("Digite uma nota (de 0 a 5) para " + lugar + ":\n"))
        escolha = input("Deseja avaliar mais lugares?\n")
        escolha = escolha.upper()
        lugares.append(lugar)
        notas.append(nota)
        if(escolha=="NÃO" or escolha=="NAO"):
            print("------------------------------------------")
            break
        print("------------------------------------------")
        cont+=1
    while(True):
        opcao = input("Deseja escolher alguma categoria?\n")
        opcao = opcao.upper()
        if(opcao == "SIM"):
            Menu_Categorias()
            name = input("Qual categoria procura?\n")
            fylter = filtros[name]
            break
        elif(escolha=="NÃO" or escolha=="NAO"):
            fylter = 'NAO'
            break
        else:
            print("Por favor, informe sim ou não como resposta\n")
        
    
    Novo_Usuario=dict(zip(lugares,notas))
    #adicionando informaçoes do usuario no BD:
    users[pessoa]=Novo_Usuario
    #chamamos a funçao recomendaçao e fazemos a recomendação ao usuario:
    print(computeNearestNeighbor(pessoa, users))
    Recomendacao = recommend(pessoa,users,fylter)
    return Recomendacao

def Menu_Categorias():
    print("Categorias Existentes:\
          \n1-Bares\
          \n2-Cultural\
          \n3-Zoológicos\
          \n4-Compras\
          \n5-Esportivo\
          \n6-Lazer\
          \n7-Alimentação\n")

def Menu_Lugares():
    print("Lugares Existentes:\
          \n1-Teatro Amazonas\
          \n2-Centro Cultural dos Povos da Amazônia\
          \n3-Porão do Alemão\
          \n4-Bar Axerito\
          \n5-Bosque da Ciência\
          \n6-CIGS\
          \n7-Amazonas Shopping\
          \n8-Mercado Municipal Adolpho Lisboa\
          \n9-Arena da Amazonia\
          \n10-Arena Paintball\
          \n11-Shot in the Dark\
          \n12-Praia da Ponta Negra\
          \n13-Cachoeira Alto do Tarumã\
          \n14-Praça da Saudade\
          \n15-Parque Cidade da Criança\
          \n16-Praça de Alimentação do Parque 10\
          \n17-Praça de Alimentação do Parque das Laranjeiras\n")

def Mostrar():
    #recupera e mostra a recomendaçao ao usuario
    Rec=Principal()
    print(Rec)

Mostrar()

     



