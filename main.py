from grafoPreDeterminado import grafo_pre_determinado
from grafoPersonalizado import grafo_personalizado
from buscaLagura import busca_por_largura
from buscaProfundidade import busca_por_profundidade
from exibeGrafo import exibir_grafo
import os
from time import sleep

listaVertices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(" --=-- Algortimos Avançados --=-- ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(" ")
print("Como deseja seu grafo?")
print("=-=-=-=-=-=-=-=-=-=-=-")
print(" 1 - Pré Determinado")
print(" 2 - Faça você mesmo")
tipoGrafo = int(input())

while True:
    if(tipoGrafo < 1 or tipoGrafo > 2):
        print("Numero invalido!")
        sleep(1)
        os.system('cls') or ('clear') or None
        print("Como deseja seu grafo?")
        print("=-=-=-=-=-=-=-=-=-=-=-")
        print(" 1 - Pré Determinado")
        print(" 2 - Faça você mesmo")
        tipoGrafo = int(input())
    else:
        break

if (tipoGrafo == 1):
    os.system('cls') or ('clear') or None
    grafo = grafo_pre_determinado()

    inicio = 'A'
    final = 'F'
    verticesGrafo = ['A', 'B', 'C', 'D', 'E', 'F']

    print(" ")
elif (tipoGrafo == 2):
    os.system('cls') or ('clear') or None
    grafo, verticesGrafo = grafo_personalizado(listaVertices)

    inicio = verticesGrafo[0]
    final = verticesGrafo[-1]

    print(" ")

print("Selecione seu algoritimo:")
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
print(" ")
print(" 1 - Busca por profundidade")
print(" 2 - Hamiltoniano")
print(" 3 - Busca por Largura")
print(" 4 - Arvore geradora minima")
print(" 5 - Algoritimos gulosos")
print(" 6 - Ordenação topológica")
print(" ")
tipoAlgoritimo = int(input())

while True:
    if(tipoAlgoritimo < 1 or tipoAlgoritimo > 6):
        print("Numero invalido!")
        sleep(1)
        os.system('cls') or ('clear') or None
        print("Selecione seu algoritimo:")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(" ")
        print(" 1 - Busca por profundidade")
        print(" 2 - Hamiltoniano")
        print(" 3 - Busca por Largura")
        print(" 4 - Arvore geradora minima")
        print(" 5 - Algoritimos gulosos")
        print(" 6 - Ordenação topológica")
        print(" ")
        tipoAlgoritimo = int(input())
    else:
        os.system('cls') or ('clear') or None
        break

if (tipoAlgoritimo == 1):
    busca_por_profundidade(grafo, verticesGrafo)
    
elif (tipoAlgoritimo == 3):
    caminho_menor = busca_por_largura(grafo, verticesGrafo)
    if caminho_menor:
        exibir_grafo(grafo)
        print(" ")
        print("Caminho mais curto entre:",inicio,"e", final,'=',' -> '.join(caminho_menor))
        print(" ")
    else:
        print("Não há caminho entre os vértices.")
