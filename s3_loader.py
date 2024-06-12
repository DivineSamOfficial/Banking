import boto3
import os

# AWS credentials and S3 configuration
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_PASSOWRD'
bucket_name = 'NAME OF YOUR S3 BUCKET'
base_s3_directory = 'BUCKET_DIRECTORY'

# Default to 'us-east-1' if region is not known
region_name = 'YOUR_REGION'

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Local directory where the CSV files are stored
local_directory = '/Users/divinesam/dbt_redshift_dw/data'

# Check if the local directory exists
if not os.path.exists(local_directory):
    print(f'Local directory {local_directory} does not exist.')
else:
    # Iterate over CSV files in the local directory
    for filename in os.listdir(local_directory):
        if filename.endswith('.csv'):
            local_file_path = os.path.join(local_directory, filename)
            folder_name = filename.split('.')[0]
            s3_file_path = os.path.join(folder_name, filename)
            
            print(f'Uploading {local_file_path} to s3://{bucket_name}/{s3_file_path}')
            
            try:
                # Upload the file to S3
                s3_client.upload_file(local_file_path, bucket_name, s3_file_path)
                print(f'Uploaded {filename} to s3://{bucket_name}/{s3_file_path}')
            except Exception as e:
                print(f'Failed to upload {filename}: {str(e)}')
