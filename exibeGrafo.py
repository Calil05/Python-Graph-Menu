def exibir_grafo(grafo):
    print("Seu Grafo: ")
    for vertice, vizinho in grafo.items():
        print(f"{vertice}: {', '.join(vizinho)}")