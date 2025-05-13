

import random
from datetime import datetime, timedelta
from openpyxl import Workbook

# Gera uma data aleatória entre duas datas
def gerar_data_aleatoria(inicio, fim):
    delta = fim - inicio
    dias_aleatorios = random.randint(0, delta.days)
    return inicio + timedelta(days=dias_aleatorios)

# Configurações
quantidade_linhas = 5000
data_inicio = datetime(2017, 1, 1)
data_fim = datetime(2021, 12, 25)

# Cria planilha
wb = Workbook()
ws = wb.active
ws.title = "Cadastros"

# Cabeçalho
ws.append(["Data de Cadastro"])

# Gera e adiciona as datas
for _ in range(quantidade_linhas):
    data = gerar_data_aleatoria(data_inicio, data_fim)
    ws.append([data.strftime('%d/%m/%Y')])

# Salva o arquivo
wb.save("C:/Users/thiago.ferreira/Downloads/MEUS PROJETOS BI/cadastros.xlsx")
print("Arquivo 'cadastros.xlsx' gerado com sucesso!")
