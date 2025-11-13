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

<img width="1918" height="890" alt="image" src="https://github.com/user-attachments/assets/9bb204e0-1b85-4e46-ad13-c5d52bd00347" />

## 5. Test the Function

In the Lambda console, click Test.
Choose “Create a new test event” → leave the default JSON (no input required).
Click Test to manually trigger.
Check the Execution results and CloudWatch logs to confirm instance IDs are printed.

<img width="1918" height="818" alt="image" src="https://github.com/user-attachments/assets/1e73de79-521c-48b1-b9f0-a2fb66b4a728" />

<img width="1918" height="688" alt="image" src="https://github.com/user-attachments/assets/f53c3904-bcd3-45dc-aecb-6dd76d5b0c7f" />







