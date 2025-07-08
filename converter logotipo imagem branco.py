from PIL import Image

# Caminho da imagem PNG
imagem_path = 'C:/Users/thiago.ferreira/OneDrive - PJUS INVESTIMENTOS EM DIREITOS CREDITORIOS LTDA/Pictures/logotipo pedro SALUFIT.png'
imagem = Image.open(imagem_path).convert('RGBA')

# Carregar os pixels
pixels = imagem.load()

# Loop para substituir o preto por branco
for y in range(imagem.height):
    for x in range(imagem.width):
        r, g, b, a = pixels[x, y]
        # Ajuste de tolerância para considerar "quase preto" (0~50)
        if r < 50 and g < 50 and b < 50 and a > 0:
            pixels[x, y] = (255, 255, 255, a)  # Branco, mantendo a transparência

# Salvar imagem final
imagem.save('logo_branca.png')

print("Imagem processada com sucesso.")
