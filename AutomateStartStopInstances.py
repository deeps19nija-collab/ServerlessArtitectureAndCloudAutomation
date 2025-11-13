import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # --- Find instances with Action=Auto-Stop ---
    stop_response = ec2.describe_instances(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop']}]
    )
    
    stop_instances = []
    for reservation in stop_response['Reservations']:
        for instance in reservation['Instances']:
            stop_instances.append(instance['InstanceId'])
    
    if stop_instances:
        print(f"Stopping instances: {stop_instances}")
        ec2.stop_instances(InstanceIds=stop_instances)
    else:
        print("No instances found with Action=Auto-Stop")
    
    # --- Find instances with Action=Auto-Start ---
    start_response = ec2.describe_instances(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Start']}]
    )
    
    start_instances = []
    for reservation in start_response['Reservations']:
        for instance in reservation['Instances']:
            start_instances.append(instance['InstanceId'])
    
    if start_instances:
        print(f"Starting instances: {start_instances}")
        ec2.start_instances(InstanceIds=start_instances)
    else:
        print("No instances found with Action=Auto-Start")
    
    return {
        'StoppedInstances': stop_instances,
        'StartedInstances': start_instances
    }
