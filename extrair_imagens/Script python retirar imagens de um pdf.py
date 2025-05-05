#AUTORIA TOTALMENTE MINHA

import fitz  # PyMuPDF
import os

# Caminho do PDF
arquivo_pdf = "Apresentacao_ED_Pavimentacoes_2024.pdf"
saida = "imagens_extraidas"

# Criar pasta de saída, se não existir
if not os.path.exists(saida):
    os.makedirs(saida)

# Abrir documento
doc = fitz.open(arquivo_pdf)

# Percorrer páginas
for pagina_num in range(len(doc)):
    imagens = doc.get_page_images(pagina_num)
    for img_index, img in enumerate(imagens):
        xref = img[0]
        imagem_pix = doc.extract_image(xref)
        imagem_bytes = imagem_pix["image"]
        extensao = imagem_pix["ext"]
        nome_arquivo = f"{saida}/pagina_{pagina_num+1}_img_{img_index+1}.{extensao}"
        with open(nome_arquivo, "wb") as img_file:
            img_file.write(imagem_bytes)

print("Imagens extraídas com sucesso.")
