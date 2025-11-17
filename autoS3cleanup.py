import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    # ---- CONFIGURATION ----
    bucket_name = "dj-s3-bucket-cleanup"  
    days_old = 30 # Files older than this number of days will be deleted

    # ---- INITIALIZE S3 CLIENT ----
    s3 = boto3.client('s3')

    # ---- CALCULATE CUTOFF DATE ----
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_old)

    print(f"Deleting objects older than {days_old} days...")
    deleted_files = []

    # ---- LIST OBJECTS IN THE BUCKET ----
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("Bucket is empty. No files to delete.")
        return {"status": "empty"}

    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']

        # ---- CHECK IF FILE IS OLDER THAN 30 DAYS ----
        if last_modified < cutoff_date:
            print(f"Deleting: {key}")
            s3.delete_object(Bucket=bucket_name, Key=key)
            deleted_files.append(key)

    print("Deleted files:", deleted_files)
    return {"deleted_files": deleted_files}
