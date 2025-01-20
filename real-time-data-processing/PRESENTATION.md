# Real-Time Data Processing

This project demonstrates how to implement a real-time data processing system using AWS services. It covers steps from data ingestion to visualization.

---

## Architecture Overview

![Diagram.jpg](Diagram.jpg)

The architecture includes:
- **Amazon Kinesis Data Streams** for real-time data ingestion.
- **AWS Lambda** for data processing (from Kinesis to S3).
- **Amazon S3** for data storage.
- **AWS Glue** for schema discovery.
- **Amazon Athena** for querying data.
- **Amazon QuickSight** for visualization.

---

## Steps to Implement

### 1. Amazon Kinesis
- Create a Kinesis stream to collect user data.
![Selection_001.png](kinesis/Selection_001.png)
![Selection_004.png](kinesis/Selection_004.png)
- Example of data to send to Kinesis - [data-format.json](kinesis/data-format.json)

### 2. Amazon S3
- Configure S3 bucket where the data sent to Kinesis will be stored.
![Selection_001.png](s3/Selection_001.png)
![bucket_policy.png](s3/bucket_policy.png)
[bucket_policy.json](s3/bucket_policy.json)
- Configure S3 bucket where the Athena queries will be stored.
![query-results-bucket.png](s3/query-results-bucket.png)

### 3. AWS Lambda
- Configure a Lambda function to process data from Kinesis and store it in S3.
1. Create the function and set up permissions
![Selection_001.png](lambda/Selection_001.png)
![Selection_001.png](lambda/permissions/Selection_001.png)
2. Paste the Lambda code - [code.py](lambda/code.py)
![code.png](lambda/code.png)
3. Add ENV variable of the bucket name.
![env_variables_1.png](lambda/env_variables_1.png)
![env_variables_2.png](lambda/env_variables_2.png)
4. Add Kinesis as a Lambda trigger.
![LambdaTrigger.png](lambda/LambdaTrigger.png)

### 4. AWS Glue
- Set up a Glue crawler to discover the schema of the data in S3 and register it in the Glue Data Catalog to query the data in Athena in the future.
1. Set up permissions.
![Selection_001.png](glue/permissions/Selection_001.png)
![Selection_002.png](glue/permissions/Selection_002.png)
2. Add the schema database and set up glue crawler to register the S3 schema.
![Selection_000.png](glue/Selection_000.png)
![Selection_001.png](glue/Selection_001.png)
![Selection_002.png](glue/Selection_002.png)
![Selection_003.png](glue/Selection_003.png)
![Selection_006.png](glue/Selection_006.png)
![Selection_007.png](glue/Selection_007.png)

### 5. Send test data to Kinesis
- Open CloudShell and execute the python script - [generate_sample_data.py](testing/generate_sample_data.py) to send sample data to Kinesis.
  ![s3_generated_files.png](testing/s3_generated_files.png)

### 6. Amazon Athena
- Query the processed data in S3 using Athena.
[query.sql](athena/query.sql)
![query.png](athena/query.png)
![Selection_001.png](athena/Selection_001.png)
![Selection_002.png](athena/Selection_002.png)
![Selection_003.png](athena/Selection_003.png)
![Selection_004.png](athena/Selection_004.png)

### 7. Amazon QuickSight
- Use QuickSight to visualize the query results.
![Selection_015.png](quick-sight/Selection_015.png)
![Selection_020.png](quick-sight/Selection_020.png)

---

## Cleanup

1. Delete the Kinesis Data Stream.
2. Remove the Lambda function.
3. Empty and delete the S3 bucket.
4. Delete the Glue crawler and its output.
5. Delete the QuickSight analysis.

---

## Conclusion

This project demonstrates the use of AWS services for real-time data processing. The same approach can be extended to handle more complex use cases.
