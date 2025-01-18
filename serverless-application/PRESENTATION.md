# Implementation Guide

---

## DynamoDB
1. **Create a DynamoDB Table**  
   Follow these steps to create a DynamoDB table:  
   ![DynamoDB - Step 1](dynamo-db/Selection_001.png)  
   ![DynamoDB - Step 2](dynamo-db/Selection_002.png)

---

## S3
1. **Create an S3 Bucket**  
   Create an S3 bucket for storing files:  
   ![S3 Bucket Creation](s3/Selection_001.png)

2. **Configure Lifecycle Rules**  
   Set up lifecycle policies to optimize storage costs:  
   ![Lifecycle - Step 1](s3/lifecycle/Selection_001.png)  
   ![Lifecycle - Step 2](s3/lifecycle/Selection_002.png)  
   ![Lifecycle - Step 3](s3/lifecycle/Selection_003.png)

---

## Lambda - Images to S3

1. **Create an IAM Role with Required Policies**
    - Define a policy for Lambda to store images to S3:  
      Policy File: [policy.json](lambda/image/iam-policy/policy.json)  
      ![IAM Policy - Step 1](lambda/image/iam-policy/Selection_002.png)  
      ![IAM Policy - Step 2](lambda/image/iam-policy/Selection_003.png)  
      ![IAM Policy - Step 3](lambda/image/iam-policy/Selection_004.png)

    - Create the IAM Role:  
      ![IAM Role - Step 1](lambda/image/iam-role/Selection_001.png)  
      ![IAM Role - Step 2](lambda/image/iam-role/Selection_002.png)  
      ![IAM Role - Step 3](lambda/image/iam-role/Selection_003.png)

2. **Create the Lambda Function**
    - Create a Lambda function to handle image uploads:  
      ![Create Lambda - Step 1](lambda/image/create_lambda_1.png)  
      ![Create Lambda - Step 2](lambda/image/create_lambda_2.png)

    - Lambda Code: [script.py](lambda/image/script.py)

---

## Lambda - API Requests to DynamoDB

1. **Create an IAM Role**
    - Create a role that allows Lambda to write data to DynamoDB:  
      ![IAM Role for JSON - Step 1](lambda/json/permissions/Selection_001.png)

2. **Create the Lambda Function**
    - Set up the Lambda function for API requests:  
      ![Lambda Creation - Step 1](lambda/json/lambda_creation.png)  
      ![Lambda Creation - Step 2](lambda/json/Selection_001.png)

    - Lambda Code: [script.py](lambda/json/script.py)

---

## API Gateway

1. **Create API Gateway Endpoints**
    - Create two endpoints to route requests to Lambda functions:  
      ![API Gateway - Step 1](api-gateway/Selection_840.png)  
      ![API Gateway - Step 2](api-gateway/Selection_841.png)  
      ![API Gateway for Image - Step 1](api-gateway/image/Selection_001.png)  
      ![API Gateway for Image - Step 2](api-gateway/image/Selection_002.png)  
      ![API Gateway for JSON - Step 1](lambda/json/api-gateway/Selection_001.png)

---

## Results

1. **Send Test Requests**
    - Test the endpoints by sending images and JSON requests:

      **Images:**  
      ![Image Upload Test](lambda/image/test.png)  
      ![Image Upload Result](lambda/image/result.png)

      **JSON Requests:**  
      ![JSON Request Test](lambda/json/testing.png)  
      ![JSON Result](lambda/json/result.png)

---

## Architecture Diagram
Visual representation of the architecture:  
![Architecture Diagram](Diagram.jpg)
