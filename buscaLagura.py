from exibeGrafo import exibir_grafo
import os
from time import sleep

def busca_por_largura(grafo, lista_vertices):

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("-=- Algoritimo de Busca por Largura -=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(" ")
    print("Esse algoritimo utiliza dos conceitos de busca por largura")
    print("pra encontrar o caminho mais curto entre dois veértices de")
    print("um grafo.")
    print("")
    input("Prescione ENTER para continuar")
    os.system('cls') or ('clear') or None

    exibir_grafo(grafo)
    print(" ")

    while True:
        inicial = input("Escolha o vértice inicial: ")

        if inicial not in lista_vertices:
            print("O vértice não está no grafo")
            sleep(1)
            os.system('cls') or ('clear') or None
            exibir_grafo(grafo)
            print(" ")
            inicial = input("Escolha o vértice inicial: ")
        else:
            # os.system('cls') or ('clear') or None
            print(" ")
            break

    while True:
        final = input("Escolha o vértice final: ")

        if final not in lista_vertices:
            print("O vértice não está no grafo")
            sleep(1)
            os.system('cls') or ('clear') or None
            exibir_grafo(grafo)
            print(" ")
            final = input("Escolha o vértice final: ")
        else:
            os.system('cls') or ('clear') or None
            break

    visitado = set()
    sequencia = ([(inicial, [inicial])])  # Fila utilizada para rastrear os vértices e caminhos.

    while sequencia:    # Laço de repetição
        vertice, caminho = sequencia.pop(0) # Retiramos o primeiro vertice da fila

        if vertice == final:    # Verificando se o vertice é igual o final do caminho
            return caminho  

        visitado.add(vertice)   # Marcamos o vizinho como visitado

        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitado:     # Verificação se o vizinho já foi visitado
                novo_caminho = caminho + [vizinho]  # Adicionamos o vizinho a um novo caminho
                sequencia.append((vizinho, novo_caminho))   # Adicionamos o vizinho e o novo caminho a fila

    return None