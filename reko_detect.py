import boto3
import json
import os

client = boto3.client ('rekognition', region_name= 'us-east-1')

bucket = 'bucket-derick-sabino'
image = 'tenis-teste.png'

response = client.detect_labels (
    Image={
        'S3Object': {
            'Bucket': bucket,
            'Name': image
        }
    },
    MaxLabels=10, ## mostra no máximo 10 objetos (ou rótulos) que você encontrou na imagem.
    MinConfidence=70 ## só mostra resultados com 70% ou mais de certeza
)

#extrair os rotulos 
labels_detectados = response['Labels']

# Criar a pasta outputs se não existir
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# Criar uma lista simplificada com nome e confiança
resultado_formatado = []
for label in labels_detectados:
    resultado_formatado.append({
        "Label": label['Name'],
        "Confidence": round(label['Confidence'], 2)
    })


    # Nome do arquivo de saida
    nome_saida = f"outputs/{image.split('.')[0]}-result.json"

    # salvar o resultaado em JSON
    with open(nome_saida,'w') as f:
        json.dump(resultado_formatado, f, indent=4)

        print(f"Resultado salvo em: {nome_saida}")