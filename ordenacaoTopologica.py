from exibeGrafo import exibir_grafo
import os
from time import sleep

def ordenacao_topologica(grafo, pre_determinado):

    novo_grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-=- Ordenação Topológica -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" ")
    print("Esse algoritimo utiliza dos conceitos de Ordenação Topológica")
    print("pra armazenar a ordem topológica dos vértices de um grafo.")
    print("")
    input("Prescione ENTER para continuar")
    os.system('cls') or ('clear') or None

    if (pre_determinado == True):

        while True:
            print("-=-=-=-=-=-=-=-=-=")
            print(" -=- ATENÇÃO! -=- ")
            print("-=-=-=-=-=-=-=-=-=")
            print(" ")
            print("Seu Grafo pré determinado possui um ciclo!")
            print("A Ordenação Topológica não funciona em grafos com ciclos.")
            print(" ")
            escolha = input("Gostaria que trocasse-mos seu grafo por um sem ciclos? [S/N]")
            escolha = escolha.upper()

            if (escolha != 'S' and escolha != 'N'):
                print(" ")
                print("Escolha Invalida!")
                os.system('cls') or ('clear') or None
                sleep(1)
            else:
                if (escolha == 'S'):
                    grafo = novo_grafo
                    break
                else:
                    break

    os.system('cls') or ('clear') or None                  
    exibir_grafo(grafo)
    print(" ")

    visitados = set()
    pilha = []

    for vertice in grafo:
        if vertice not in visitados:
            stack = [(vertice, iter(grafo[vertice]))]

            while stack:
                v, vizinhos_iter = stack[-1]
                try:
                    vizinho = next(vizinhos_iter)
                except StopIteration:
                    stack.pop()
                    pilha.append(v)
                    continue

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    stack.append((vizinho, iter(grafo[vizinho])))

    if len(pilha) != len(grafo):
        print("Não é possível encontrar uma ordenação topológica. O grafo contém um ciclo.")
        return None

    return pilha[::-1]
