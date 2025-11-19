import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Initialize EC2 client
    ec2_client = boto3.client('ec2')

    try:
        # Retrieve the instance ID from the CloudWatch event
        instance_id = event['detail']['instance-id']
        
        # Current date tag
        current_date = datetime.utcnow().strftime('%Y-%m-%d')
        
        # Tag the new instance
        ec2_client.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'LaunchDate', 'Value': current_date},
                {'Key': 'Environment', 'Value': 'Test'}  # Replace with your custom tag
            ]
        )
        
        print(f"Successfully tagged instance {instance_id} with LaunchDate={current_date}")
        
    except Exception as e:
        print(f"Error tagging instance: {str(e)}")
