import csv
import random

# Listas realistas de nomes e sobrenomes brasileiros
nomes = ["Ana", "Carlos", "Fernanda", "Lucas", "Juliana", "Pedro", "Mariana", "Rafael", "Larissa", "João"]
sobrenomes = ["Silva", "Oliveira", "Santos", "Costa", "Souza", "Lima", "Pereira", "Barbosa", "Almeida", "Melo"]

def gerar_nome():
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

# Corrigir os nomes na base
with open("farmacia_clientes.csv", mode="r", encoding="utf-8") as entrada:
    leitor = csv.DictReader(entrada)
    colunas = leitor.fieldnames
    dados_corrigidos = []

    for linha in leitor:
        linha["Nome_Cliente"] = gerar_nome()
        dados_corrigidos.append(linha)

with open("farmacia_clientes_corrigido.csv", mode="w", newline="", encoding="utf-8") as saida:
    escritor = csv.DictWriter(saida, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(dados_corrigidos)

print("Arquivo 'farmacia_clientes_corrigido.csv' gerado com sucesso com novos nomes fictícios.")
