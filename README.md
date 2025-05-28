# 🧠 Analisador de Imagens com AWS Rekognition e Flask

Projeto simples e direto que permite ao usuário fazer upload de uma imagem, e o sistema retorna os objetos detectados utilizando o **Amazon Rekognition**, tudo isso com uma interface web feita em **Flask**.

---

## 💡 O que esse projeto faz?

- ✅ Permite upload de imagens via navegador
- ✅ Salva temporariamente a imagem local
- ✅ Envia a imagem para o Amazon S3
- ✅ Utiliza o **Amazon Rekognition** para detectar objetos na imagem
- ✅ Retorna os rótulos (labels) com confiança (confidence) em formato visual e JSON

---

## 🚀 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo 

2.  Instale as dependências:
pip install -r requirements.txt

3. Configure sua AWS (via credenciais padrão)
Você precisa ter um bucket no S3 e permissões no Rekognition.

4. Rode o app com: python app.py

5. Abra no navegador: http://127.0.0.1:5000/
  
📌 Dica
Esse projeto é um ótimo exemplo de como usar IA da AWS em algo visual. Pode ser adaptado pra:

🛍️ e-commerce (análise de fotos de produtos)

🎥 vídeos/imagens de segurança

⚽ imagens esportivas

📲 Autor
Feito por Derick Sabino
🔗 https://www.linkedin.com/in/derick-sabino-84052320b/

