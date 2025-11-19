# Assignment1 Automated Instance Management Using AWS Lambda and Boto3

## 1. EC2 Setup

Go to the AWS Management Console → EC2 → Instances → Launch Instance.

Launch two t2.micro instances (free-tier eligible).

In Tag section:

Instance 1:
Key: Action
Value: Auto-Stop

Instance 2:
Key: Action
Value: Auto-Start

<img width="1907" height="552" alt="image" src="https://github.com/user-attachments/assets/9543142e-635b-46d2-83f1-4401c1d01937" />
<img width="1918" height="577" alt="image" src="https://github.com/user-attachments/assets/9cb58816-cbd3-44f9-ae09-50409fef5ac0" />

## Create IAM Role for Lambda

Go to IAM → Roles → Create Role.

Select AWS Service → Lambda.

Attach the following policies:
AmazonEC2FullAccess
AWSLambdaBasicExecutionRole (for CloudWatch logging)

Name it: DJ-LambdaEC2AutomationRole.

<img width="1912" height="791" alt="image" src="https://github.com/user-attachments/assets/af5fdf70-cab3-47fd-ad97-1e76cd7bf64f" />

## Create the Lambda Function

Go to Lambda → Create Function.

Choose:
Author from scratch
Runtime: Python 3.x (e.g., Python 3.12)
Execution Role: Use existing role → DJ-LambdaEC2AutomationRole
Click Create Function.

Add below code snipping in code section of your lambda function
https://github.com/deeps19nija-collab/ServerlessArtitectureAndCloudAutomation/blob/main/AutomateStartStopInstances.py
<img width="1918" height="890" alt="image" src="https://github.com/user-attachments/assets/9bb204e0-1b85-4e46-ad13-c5d52bd00347" />


## 5. Test the Function

In the Lambda console, click Test.
Choose “Create a new test event” → leave the default JSON (no input required).
Click Test to manually trigger.
Check the Execution results and CloudWatch logs to confirm instance IDs are printed.

<img width="1918" height="818" alt="image" src="https://github.com/user-attachments/assets/1e73de79-521c-48b1-b9f0-a2fb66b4a728" />

<img width="1918" height="688" alt="image" src="https://github.com/user-attachments/assets/f53c3904-bcd3-45dc-aecb-6dd76d5b0c7f" />

# Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Step 1: S3 Bucket Setup

Go to AWS Console → S3 → Create bucket
Give it a unique name (e.g. my-lambda-cleanup-bucket)
Leave defaults and click Create bucket
<img width="1875" height="726" alt="image" src="https://github.com/user-attachments/assets/7fc2aa79-7e32-44ef-a5ea-1899a55b1d9c" />

Upload multiple files
Add test files (some “old” and some “new”)
To simulate old files, you can:
Just assume some files are old for testing.

<img width="1518" height="805" alt="image" src="https://github.com/user-attachments/assets/aff9ca11-aae8-40cb-b9aa-1d157413cac6" />


## Step 2: Create IAM Role for Lambda

Go to IAM → Roles → Create role
Choose AWS Service → Lambda
Attach the following policy:
AmazonS3FullAccess
Name it
Create the role.
<img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/18ad1ee3-be68-4a43-936c-8a5a52b9be0c" />

## Step 3: Create AWS Lambda Function

Go to Lambda → Create function
Choose:
Author from scratch
Name: s3_cleanup_function
Runtime: Python 3.12 (or any 3.x)
Role: Use existing role → choose LambdaS3CleanupRole
Click Create function
<img width="1911" height="677" alt="image" src="https://github.com/user-attachments/assets/d0bafd4e-bc65-4808-ad3b-0ee42936877d" />


## Step 4: Add the Python Code as below

https://github.com/deeps19nija-collab/ServerlessArtitectureAndCloudAutomation/blob/main/autoS3cleanup.py

## Step 5: Test the Lambda Manually

In the Lambda console, click Test → Configure test event
Choose "Hello World" template (or empty JSON)
Save it.
Click Test
Check CloudWatch Logs (link appears under "Monitor" tab):
You’ll see which files were deleted and which were kept.
Go back to the S3 console — confirm only newer files remain.
<img width="1877" height="846" alt="image" src="https://github.com/user-attachments/assets/48b3c650-5430-497e-9d73-04f46455a14f" />

<img width="1568" height="588" alt="image" src="https://github.com/user-attachments/assets/331cb050-88fa-4dfb-b730-5aef7400115c" />

# Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

## Step 1: EC2 Setup

Create an EC2 instance without tag.
<img width="1918" height="932" alt="image" src="https://github.com/user-attachments/assets/e1e23458-cd9e-4c31-bb94-97abb56b7d14" />

## Step 2: Lambda IAM Role

Go to IAM → Roles → Create role.

Select Lambda as the trusted entity.

Attach the following policy:

AmazonEC2FullAccess

Name the role.
<img width="1917" height="820" alt="image" src="https://github.com/user-attachments/assets/bae0b0c0-00e1-4578-adb0-39189f1e4110" />

# Step 3: Lambda Function

Go to Lambda → Create function → Author from scratch.

Runtime: Python 3.x

Assign the IAM role created in Step 2.
<img width="1898" height="878" alt="image" src="https://github.com/user-attachments/assets/573d39f1-56ac-4da7-94b0-f2f02b0c7b1f" />

Copy the following Python script into the Lambda function:
https://github.com/deeps19nija-collab/ServerlessArtitectureAndCloudAutomation/blob/main/AutoTagEC2Instances.py













