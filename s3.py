import boto3

access_key_id = ""
secret_access_key = ""
region = ""

s3 = boto3.client('s3', 
                aws_access_key_id=access_key_id, 
                aws_secret_access_key=secret_access_key, 
                region_name=region
            )

file_path = "sample_file.txt"
bucket_name = "darshan-bucket"  
object_name = 'sample_file.txt'

try:
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
