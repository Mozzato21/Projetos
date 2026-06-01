import requests
import os

# Defina o diretório onde as imagens serão armazenadas
output_directory = "C:/..."

# Leia as URLs e nomes das imagens do arquivo "urls.txt"
with open('urls.txt', 'rt') as entrada:
    image_data = [line.strip().split(';') for line in entrada]

# Baixe as imagens
for i, (url, image_name) in enumerate(image_data, start=1):
    try:
        response = requests.get(url, verify=False)
        with open(os.path.join(output_directory, image_name), "wb") as image_file:
            image_file.write(response.content)
        print(f"Imagem {image_name} baixada com sucesso.")
    except Exception as e:
        print(f"Erro ao baixar a imagem {image_name}: {e}")
