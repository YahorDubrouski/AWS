import json
import boto3
import datetime
import base64

# Initialize the S3 client
s3 = boto3.client('s3')

# Define the S3 bucket name
S3_BUCKET = 'yahor-dubrouski-images'

def lambda_handler(event, context):
    try:
        # Log the event (for debugging purposes)
        print("Event: ", event)
        
        # Extract the binary body and filename from the request
        file_content = base64.b64decode(event['body'])
        original_filename = event['headers'].get('filename', 'default.jpg')
        
        # Generate a datetime prefix
        now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        new_filename = f"{now}-{original_filename}"
        
        # Upload the file to S3
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=new_filename,
            Body=file_content
        )
        
        # Return success response
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "File uploaded successfully!", "filename": new_filename}),
            "headers": {"Content-Type": "application/json"}
        }
    except Exception as e:
        print("Error: ", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Failed to upload file", "error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }

