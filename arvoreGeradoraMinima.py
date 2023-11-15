from adicionaPeso import adicionar_pesos_aleatorios
from exibeGrafo import exibir_grafo_com_pesos
import os
from time import sleep

def arvore_geradora_minima(grafo, lista_vertices):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     -=- Arvores Geradoras Minimas -=-     ")
    print("         -=- Algoritmo de Prim -=-     ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Esse algoritmo utiliza dos conceitos do algoritmo de Prim em")
    print("Arvores Gerados Minimas de um grafo, para isso será necessario")
    print("adicionar pesos para as aréstas do grafo. Adicionaremos pesos")
    print("aleatórios para cada aresta do seu grafo.")
    print("")
    input("Prescione ENTER para continuar")
    os.system('cls') or ('clear') or None

    exibir_grafo_com_pesos(grafo)
    print(" ")
    sleep(1)

    arvore_geradora = set()
    vertices = list(grafo.keys())
    visitados = set()

    vertice_inicial = vertices[0]
    visitados.add(vertice_inicial)

    while len(visitados) < len(vertices):
        menor_peso = float('inf')
        aresta_menor_peso = None

        for vertice_visitado in visitados:
            for vizinho, peso in grafo[vertice_visitado]:
                if vizinho not in visitados and peso < menor_peso:
                    menor_peso = peso
                    aresta_menor_peso = (vertice_visitado, vizinho)

        if aresta_menor_peso:
            arvore_geradora.add(aresta_menor_peso)
            visitados.add(aresta_menor_peso[1])

    return arvore_geradora
