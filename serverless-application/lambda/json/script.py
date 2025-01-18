import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('api_requests')

def lambda_handler(event, context):
    try:
        # Parse input from the event
        body = json.loads(event.get('body', '{}'))
        id = body.get('id')
        name = body.get('name')
        email = body.get('email')

        # Validate input
        if not id or not name or not email:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing required fields: id, name, or email"})
            }

        # Insert item into DynamoDB
        table.put_item(
            Item={
                'id': id,
                'name': name,
                'email': email
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Data inserted successfully"})
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": e.response['Error']['Message']})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

