import pandas as pd
import re

# Caminho da planilha
caminho_arquivo = (f'C:\\Users\\thiago.ferreira\\OneDrive - PJUS INVESTIMENTOS EM DIREITOS CREDITORIOS LTDA\\Desktop\\RPA\\ROBO - Homonimos\\Homonimos\\rpa-enriquecimento_novo\\input\\In_Geral_Sem_CPF.xlsx' )# substitua pelo caminho real

# Lê a planilha
df = pd.read_excel(caminho_arquivo)

# Função para limpar o nome
def limpar_nome(nome):
    if isinstance(nome, str):
        nome_limpo = re.split(r'\bREPRESENTADO\b|\bREP\b|\bREGISTRADOA\b', nome)[0].strip()
        return nome_limpo
    return nome

# Aplica a função na coluna 'Nome'
df['Nome'] = df['Nome'].apply(limpar_nome)

# Salva em um novo arquivo
df.to_excel('C:\\Users\\thiago.ferreira\\OneDrive - PJUS INVESTIMENTOS EM DIREITOS CREDITORIOS LTDA\\Desktop\\RPA\\ROBO - Homonimos\\Homonimos\\rpa-enriquecimento_novo\\input\\planilha_limpa.xlsx', index=False)

print("Nomes limpos e arquivo salvo como 'planilha_limpa.xlsx'")
