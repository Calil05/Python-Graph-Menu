from grafoPersonalizado import grafo_personalizado
import json
from exibeGrafo import exibir_grafo

def salvar_grafo_em_json(nome_grafo, grafo, nome_arquivo):
    # Tenta carregar o arquivo existente
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados_salvos = json.load(arquivo_json)
    except FileNotFoundError:
        dados_salvos = []

    # Adiciona o novo grafo ao final da lista
    dados_salvos.append({'nome': nome_grafo, 'grafo': grafo})

    # Salva a lista atualizada no arquivo JSON
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados_salvos, arquivo_json)

def carregar_grafo_do_json_por_nome(nome_arquivo, nome_grafo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados_carregados = json.load(arquivo_json)
    except FileNotFoundError:
        return None

    for item in dados_carregados:
        if item['nome'] == nome_grafo:
            return item['grafo']

    return None

# Exemplo de uso:
lista_de_caracteres = ['A', 'B', 'C', 'D', 'E', 'F']

# Criar um grafo de exemplo
grafo, vertices = grafo_personalizado(lista_de_caracteres)

# Nomear o grafo
nome_grafo = "Grafo Exemplo54"

# Salvar o grafo em um arquivo JSON
nome_arquivo = 'grafos.json'
salvar_grafo_em_json(nome_grafo, grafo, nome_arquivo)

nome_grafo_selecionado = "Grafo Exemplo22"
grafo_selecionado = carregar_grafo_do_json_por_nome(nome_arquivo, nome_grafo_selecionado)

if grafo_selecionado:
    print(f"Nome do Grafo: {nome_grafo_selecionado}")
    exibir_grafo(grafo_selecionado)
else:
    print(f"Grafo com o nome '{nome_grafo_selecionado}' não encontrado.")