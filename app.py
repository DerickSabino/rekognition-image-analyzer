from flask import Flask, render_template, request
import boto3
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

rekognition = boto3.client('rekognition', region_name='us-east-1')
s3 = boto3.client('s3')
bucket = 'bucket-derick-sabino'

@app.route('/', methods=['GET', 'POST'])
def index():
    labels = [] 
    image_url = ''

    if request.method == 'POST':
        file = request.files['file']
        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)
            image_url = '/' + image_path

            # envia imagem pro S3
            s3.upload_file(image_path, bucket, file.filename)

            # detecta labels com Rekognition
            response = rekognition.detect_labels(
                Image={
                    'S3Object': {
                        'Bucket': bucket,
                        'Name': file.filename
                    }
                },
                MaxLabels=10,
                MinConfidence=80
            )

            labels = response['Labels']

    return render_template('index.html', labels=labels, image=image_url)

if __name__ == '__main__':
    app.run(debug=True)
