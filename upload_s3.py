import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket_name = 'bucket-derick-sabino'
image_file = 'tenis-teste.png'

try:
    s3.upload_file(image_file, bucket_name, image_file)
    print(f'✅Upload da imagem "{image_file}" feito com sucesso no bucket "{bucket_name}".')
except Exception as e:
    print(f'❌ Erro ao fazer upload: {e}')
