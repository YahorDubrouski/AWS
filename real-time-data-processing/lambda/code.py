import json
import base64
import boto3
import os

# Initialize S3 client
s3_client = boto3.client('s3')

# Get the S3 bucket name from environment variables
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']

def lambda_handler(event, context):
    """
    Process data from Kinesis and store processed results in S3.

    Args:
        event (dict): The incoming event data from Kinesis.
        context: Lambda runtime context (unused here).

    Returns:
        dict: Response status.
    """
    try:
        # List to hold processed records
        processed_records = []
        
        # Loop through Kinesis records
        for record in event['Records']:
            # Decode the Kinesis data (base64 encoded)
            payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            
            # Convert payload to JSON
            data = json.loads(payload)
            
            # Add additional processing if needed
            processed_data = {
                "user_id": data.get("user_id"),
                "action": data.get("action"),
                "timestamp": data.get("timestamp"),
                "processed_at": context.aws_request_id  # Unique request ID for tracking
            }
            processed_records.append(processed_data)
        
        # Prepare file for S3 upload
        file_key = f"processed_data_{context.aws_request_id}.json"
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=file_key,
            Body=json.dumps(processed_records),
            ContentType='application/json'
        )
        
        print(f"Successfully processed and uploaded data to S3: {file_key}")
        
        return {
            "statusCode": 200,
            "body": f"Processed {len(processed_records)} records and uploaded to S3."
        }
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Error processing data: {str(e)}"
        }
