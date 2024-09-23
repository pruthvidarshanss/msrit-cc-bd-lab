import boto3

access_key_id = ""
secret_access_key = ""
region = ""
table_name = ""

dynamodb = boto3.resource('dynamodb', 
                      aws_access_key_id=access_key_id, 
                      aws_secret_access_key=secret_access_key, 
                      region_name=region
                    )

data_item = {
    "code": "MCSL26",
    "course": "Cloud Computing and Big Data Laboratory",
    "credits": 1,
}

try:
    table = dynamodb.Table(table_name)
    table.put_item(Item=data_item)
    print(f"Item added to table '{table_name}': {data_item}")
except Exception as e:
    print(f"An error occurred: {e}")
