import boto3

access_key_id = ""
secret_access_key = ""
region = ""

ec2 = boto3.client('ec2', 
                aws_access_key_id=access_key_id, 
                aws_secret_access_key=secret_access_key, 
                region_name=region
            )

instance_id = ""

# start instances
try:
    response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
except Exception as e:
    print(e)

# stop instances
try:
    response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
except Exception as e:
    print(e)

# reboot instances
try:
    response = ec2.reboot_instances(InstanceIds=[instance_id], DryRun=False)
    print('Success', response)
except Exception as e:
    print('Error', e)
