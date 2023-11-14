from adicionaPeso import adicionar_pesos_aleatorios
from exibeGrafo import exibir_grafo_com_pesos
import os
from time import sleep

def encontra_componente(componentes, vertice):
    for componente, vertices in componentes.items():
        if vertice in vertices:
            return componente

def busca_gulosa_kruskal(grafo):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("     -=- Algoritimos Gulosos -=-     ")
    print("    -=- Algoritimo de Kruskal -=-    ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(" ")
    print("Esse algoritmo utiliza dos conceitos do algoritimos gulosos em grafos")
    print("utilizando do algoritimo de Kruskal, para realizar uma Árvore Minima de") 
    print("Abrangencia, para isso será necessario adicionar pesos para as aréstas")
    print("do grafo. Adicionaremos pesos Aleatórios para cada aresta do seu grafo.")
    print("")
    input("Prescione ENTER para continuar")
    os.system('cls') or ('clear') or None

    exibir_grafo_com_pesos(grafo)
    print(" ")
    sleep(1)

    arvore = set()
    componentes = {vertice: {vertice} for vertice in grafo}

    for u, vizinhos in grafo.items():
        for v, w in vizinhos:
            componente_u = encontra_componente(componentes, u)
            componente_v = encontra_componente(componentes, v)

            if componente_u != componente_v:
                arvore.add((u, v, w))
                componentes[componente_u].update(componentes[componente_v])
                del componentes[componente_v]

                if len(componentes) == 1:
                    return arvore  # Pode encerrar assim que todos os vértices estiverem conectados

    return arvore
