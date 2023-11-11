def exibir_grafo(grafo):
    print("Seu Grafo: ")
    for vertice, vizinho in grafo.items():
        print(f"{vertice}: {', '.join(vizinho)}")

def exibir_grafo_com_pesos(grafo):
    for vertice, vizinhos in grafo.items():
        print(f"{vertice}:", end=' ')
        for vizinho, peso in vizinhos:
            print(f"({vizinho} - {peso})", end=' ')
        print()