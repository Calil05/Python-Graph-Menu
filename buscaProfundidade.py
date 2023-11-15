from exibeGrafo import exibir_grafo
import os
from time import sleep

def busca_por_profundidade(grafo, lista_vertices):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("-=- Algoritmo de Busca por Profundidade -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(" ")
    print("Esse algoritmo realiza a busca por profundidade no")
    print("grafo a partir do vértice selecionado pelo usuario")
    print("e imprime o resultado.")
    print("")
    input("Prescione ENTER para continuar")
    os.system('cls') or ('clear') or None

    exibir_grafo(grafo)
    print(" ")

    while True:
        vertice_inicial = input("Realizar busca por profundidade a partir de qual vértice? ")
        vertice_inicial = vertice_inicial.upper()

        if vertice_inicial not in lista_vertices:
            os.system('cls') or ('clear') or None
            print("O vértice não está no grafo")
            sleep(1)
            os.system('cls') or ('clear') or None
            exibir_grafo(grafo)
            print(" ")
            vertice_inicial = input("Realizar busca por profundidade a partir de qual vértice? ")
            vertice_inicial = vertice_inicial.upper()
        else:
            os.system('cls') or ('clear') or None
            print(" ")
            break
        
    visitados = set()

    def busca(vertice):
        nonlocal visitados
        visitados.add(vertice)
        print(vertice, end=' ')

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                busca(vizinho)

    print("Busca em Profundidade a partir do vértice '{}': ".format(vertice_inicial))
    busca(vertice_inicial)