import boto3
import json
import random
import time

# AWS configuration
REGION = "us-east-1" 
STREAM_NAME = "UserActivityStream"

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

# Helper function to generate random user data
def generate_random_data():
    user_id = random.randint(1, 10)  # Random user IDs from 1 to 1000
    actions = ["click", "login", "logout", "purchase", "signup"]
    data = {
        "user_id": str(user_id),
        "action": random.choice(actions),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    return data

# Send data to Kinesis
def send_test_data_to_kinesis(total_records=100, batch_size=10):
    print(f"Sending {total_records} records to Kinesis...")
    
    for i in range(0, total_records, batch_size):
        records = []
        for _ in range(batch_size):
            data = generate_random_data()
            records.append({
                "Data": json.dumps(data),
                "PartitionKey": str(data["user_id"])  # Ensure balanced partitioning
            })
        
        # Send batch of records
        response = kinesis_client.put_records(
            StreamName='UserActivityStream',
            Records=records
        )
        
        print(f"Batch {i // batch_size + 1}: Sent {len(records)} records, Failed: {response['FailedRecordCount']}")
        
        # Pause briefly to avoid overwhelming the stream
        time.sleep(0.5)

    print("All records sent.")

# Run the script
if __name__ == "__main__":
    send_test_data_to_kinesis(total_records=10000, batch_size=50)  # Adjust total records and batch size as needed

