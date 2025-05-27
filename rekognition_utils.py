import boto3

def detectar_labels(bucket, image_name, max_labels=10, min_confidence=80):
    client = boto3.client("rekognition", region_name="us-east-1")

    response = client.detect-labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': image_name
            }
        },
        Maxlabels=max_labels,
        MinConfidence=min_confidence
    )

    labels = []
    for label in response ['Labels']:
        label.append({
            'Label': label['Name'],
            'Confidence': round(label['confidence'], 2)
        })

    return label    