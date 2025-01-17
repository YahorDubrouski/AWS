# Implementation

## Security Group
1. Create a security group for the EC2 instances with the internet access.
   ![Selection_780.png](steps/security-group-internet-access/Selection_780.png)

## AMI (Amazon Machine Image)
1. Create an EC2 instance with t2micro (free tier) type with the `user data` from the [ami.sh](user-data/ami.sh). The bash script will install all necessary dependencies and show some basic information to the EC2 Web Server users. 
![screenshot-1.png](steps/ami/screenshot-1.png)
2. Create AMI from the image.
![screenshot-2.png](steps/ami/screenshot-2.png)

Note - use the previously created security group for the AMI.

## RDS
1. Create an RDS MySQL Database.
2. Fill in the database.
![create_db_schema_and_data.png](steps/rds/create_db_schema_and_data.png).
3. Allow the EC2 security group to connect to the database.
![security_group.png](steps/rds/security_group.png).
4. Create Rds Credentials in the AWS Secrets Manager service for the DB.

## ALB Target group and Launch Template
1. Create an ALB Target Group
![Selection_782.png](steps/alb-tg-and-alb-lt/Selection_782.png)
2. Create a Launch Template. Use the [launch-template.sh](user-data/launch-template.sh) as the `user data` script to show the users table content in the Web Server index page.
![Selection_783.png](steps/alb-tg-and-alb-lt/Selection_783.png)

## Auto Scaling Group
1. Create an Auto Scaling Group that will auto scale the traffic from 1 to 3 instances to automatically controll the EC2 instances amount based on CPU Utilization.
2. Configure the CPU Utilization to > 60%.
[Auto Scaling group details _ EC2 _ us-east-1.pdf](steps/asg/Auto%20Scaling%20group%20details%20_%20EC2%20_%20us-east-1.pdf).
![Selection_778.png](steps/asg/Selection_778.png)
![Selection_784.png](steps/asg/Selection_784.png)

## Application Load Balancer
1. Create an ALB that will route the traffic to the ASG.

## CloudWatch Alarm
1. Create a CloudWatch Alarm to notify an admin by the email in case CPU Utilization is grater then 80%. During the metric creation create an SNS topic with the admin Email.
![Selection_820.png](steps/cloud-watch-alarm/Selection_820.png)
![Selection_821.png](steps/cloud-watch-alarm/Selection_821.png)
2. Confirm the SNS Subscription by the email.
![Selection_822.png](steps/cloud-watch-alarm/Selection_822.png)
3. Use Apache Benchmark to simulate the traffic and see the Email notification. 
![Selection_823.png](steps/cloud-watch-alarm/Selection_823.png)
![Selection_824.png](steps/cloud-watch-alarm/Selection_824.png)

## Diagram
![Diagram.jpg](Diagram.jpg)
