import pandas as pd
import os

# Caminho da planilha original
arquivo_origem = r'C:\Users\thiago.ferreira\Downloads\TRIBUNAL GO\4mti 30-05.xlsx'
# Caminho da nova planilha (com nome final do arquivo)
arquivo_destino = os.path.join(
    r'C:\Users\thiago.ferreira\Downloads\TRIBUNAL GO',
    '00_In_Geral_tradado.xlsx'
)

# Dicionário de mapeamento: 'nome atual' -> 'nome padrão'
colunas_renomeadas = {
    "Tribunal": "Tribunal",
    "Precatorio": "Precatorio",
    "Processo": "Processo",
    "Valor_Bruto": "Valor",
    "Cpf_Beneficiario": "CPF",
    "Beneficiario": "Nome",
    "Data_Nascimento": "Data_Nascimento",
    "UF": "UF",
    "Orgao": "Orgao",
    "Data_Liquidacao": "Data_Liquidacao",
    "Estado_Processo": "UF_Proc",
    "Advogado": "Advogado",
    "Numero_Oab": "OAB",
    "Percentual_Honorario_Advogadoa": "Percentual_Honorarios",
    "Data_Transito_Julgado_Conhecimento": "DataTransitoConhecimento",
    "Data_Transito_Julgado_Excecao": "DataTransitoExecucao",
    "Tipo_Desconto_Previdencia": "Tipo_Previdencia",
    "Valor_PSS": "Valor_PSS",
    "Tipo_Processo": "TipoProcesso",
    "Processo_Delegado_Tj": "ProcessoDelegado",
    "Natureza_Precatorio": "NaturezaPrecatorio",
    "Data_Autuacao": "DataAutuacao",
    "Vencimento": "AnoVencimento",
    "Valor_Principal": "ValorPrincipal",
    "Valor_Juros": "ValorJuros",
    "Imposto_Renda": "Imposto_Renda",
    "Meses_RRA": "Meses_RRA",
    "Data_Inicio_Formacao_RRA": "Data_Inicio_Formacao_RRA",
    "Data_Fim_Formacao_RRA": "Data_Fim_Formacao_RRA",
    "Data_Ec_62": "Data_Ec_62",
    "Valor_Ec_62": "Valor_Ec_62",
    "Vara": "vara"
}

# Carregar a planilha
df = pd.read_excel(arquivo_origem)

# Selecionar e renomear colunas que existem
colunas_existentes = {col: novo for col, novo in colunas_renomeadas.items() if col in df.columns}
df_tratado = df[list(colunas_existentes.keys())].rename(columns=colunas_existentes)

# Reordenar de acordo com a ordem do dicionário original
ordem_final = list(colunas_existentes.values())
df_tratado = df_tratado[ordem_final]

# Salvar a nova planilha
df_tratado.to_excel(arquivo_destino, index=False)

print("✅ Planilha tratada salva com sucesso em:")
print(arquivo_destino)
