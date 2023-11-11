from exibeGrafo import exibir_grafo
import os
from time import sleep

def grafo_personalizado(lista_de_caracteres):
    grafo = {}
 
    verticesGrafo = []

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" -=- Criação de Grafo -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Quantos vértices? (1 a 26)")
    escolha = int(input())

    while True:
        if(escolha > 26 or escolha < 1):
            print("Numero invalido!")
            sleep(1)
            os.system('cls') or ('clear') or None
            print("Quantos vértices? (1 a 26)")
            escolha = int(input())
        else:
            break

    os.system('cls') or ('clear') or None

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" -=- Criação de Grafo -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Seus Vértices: ")

    for i in range (escolha):
        verticesGrafo.append(lista_de_caracteres[i])

    print(" ")
    print(verticesGrafo)
    print("Prescione ENTER para continuar")
    print(" ")
    input()
    
    for i, caracter in enumerate(verticesGrafo):
        grafo[caracter] = []
    
    for i, caracter in enumerate(verticesGrafo):
        while True:
            print(f"Escolha um vértice para adicionar uma conexão para '{caracter}' (ou digite -1 para parar): ")
            escolha = input()
            if escolha == '-1':
                os.system('cls') or ('clear') or None
                break
            if escolha not in verticesGrafo or escolha == caracter:
                print("Vértice inválido. Escolha outro vértice.")
            else:
                if escolha not in grafo[caracter]:
                    grafo[caracter].append(escolha)
                    grafo[escolha].append(caracter)  # Garante a conexão bidirecional
                else:
                    print(f"A conexão entre '{caracter}' e '{escolha}' já existe.")

    os.system('cls') or ('clear') or None
    exibir_grafo(grafo)

    return grafo, verticesGrafo