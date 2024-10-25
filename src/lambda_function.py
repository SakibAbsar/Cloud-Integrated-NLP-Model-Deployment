
import json
import boto3
import os
from transformers import pipeline

# Initialize S3 client
s3 = boto3.client('s3')

def download_model(bucket_name, model_path):
    """Download the model from S3 if not already present."""
    if not os.path.exists('/tmp/sentiment_model'):
        os.makedirs('/tmp/sentiment_model', exist_ok=True)
        s3.download_file(bucket_name, model_path, '/tmp/sentiment_model/model.bin')
    return '/tmp/sentiment_model/model.bin'

def lambda_handler(event, context):
    # Load config
    bucket_name = os.getenv('bucket_name', 'your-s3-bucket-name')
    model_path = os.getenv('model_path', 'path/to/your/sentiment_model')
    
    # Download and load model
    model_file = download_model(bucket_name, model_path)
    nlp_pipeline = pipeline('sentiment-analysis', model=model_file)
    
    # Process input text
    text = event.get("text", "")
    result = nlp_pipeline(text)[0]
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
