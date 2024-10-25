
# Cloud-Integrated NLP Model Deployment

This project demonstrates deploying a sentiment analysis model on AWS Lambda for real-time performance. 
The model file is stored on S3, and Lambda fetches it to process text input.

## Features
- Sentiment Analysis via NLP
- Real-time and scalable cloud processing
- Integrated with AWS Lambda and S3

## Setup Instructions

### 1. Create and Configure an S3 Bucket
1. Create an S3 bucket on AWS and upload the model file.
2. Note the S3 bucket name and the model file path.

### 2. Set Up AWS Lambda
1. In AWS Lambda, create a new function with Python 3.8 or higher.
2. Upload the Lambda deployment package or use the AWS CLI to upload this project.

### 3. Configure IAM Permissions
Ensure Lambda has access to the S3 bucket by assigning the correct IAM role permissions.

### 4. Test the Deployment
Invoke the Lambda function with sample text input to receive sentiment analysis results.

---

