from limpaTela import limpaTela
from exibeGrafo import exibir_grafo
import os
from time import sleep

def testar_combinações(atuais, restantes):
    if not restantes:   # Se não há vértices restantes, retorna a combinação atual
        return [atuais]
    caminhos = []
    for i in range(len(restantes)):   # Percorre os vértices restantes para gerar todas as combinações
        vizinho = restantes[i]
        restantes_restantes = restantes[:i] + restantes[i + 1:]
        caminhos.extend(testar_combinações(atuais + [vizinho], restantes_restantes))
    return caminhos

def grafo_hamiltoniano(grafo, lista_vertices):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-=- Grafos Hamiltonianos -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Esse algoritmo utiliza dos conceitos de Grafos Hamiltonianos")
    print("pra encontrar o caminho Hamiltoniano a partir de determinado")
    print("vértice de um grafo.")
    print("")
    input("Prescione ENTER para continuar")
    limpaTela()

    exibir_grafo(grafo)
    print(" ")

    vertice_inicial = input("Caminho Hamiltoniano a partir de qual vértice? ")
    vertice_inicial = vertice_inicial.upper()

    while True:

        if vertice_inicial not in lista_vertices: 
            limpaTela()
            print("O vértice não está no grafo")
            sleep(1)
            limpaTela()
            exibir_grafo(grafo)
            print(" ")
            vertice_inicial = input("Caminho Hamiltoniano a partir de qual vértice? ")
            vertice_inicial = vertice_inicial.upper()
        else:
            limpaTela()
            print(" ")
            break

    vertices = list(grafo.keys()) # Pega a lista de vértices do grafo
    for permutacao in testar_combinações([], vertices):    # Gera todas as combinações dos vértices e verifica se há um caminho Hamiltoniano válido
        if all(permutacao[i + 1] in grafo[permutacao[i]] for i in range(len(permutacao) - 1)):
            return permutacao
    return None # Retorna None se não encontrar um caminho Hamiltoniano
