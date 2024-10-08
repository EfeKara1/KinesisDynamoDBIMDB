import boto3
from botocore.exceptions import ClientError
from config import Config

def create_dynamodb_table():
    dynamodb = boto3.resource('dynamodb', region_name=Config.AWS_REGION)

    try:
        table = dynamodb.create_table(
            TableName=Config.DYNAMODB_TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'title',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'  # String type
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        print(f"DynamoDB table '{Config.DYNAMODB_TABLE_NAME}' created successfully.")
    except ClientError as e:
        print(f"Error creating DynamoDB table: {e}")

def write_to_dynamodb(data):
    dynamodb = boto3.resource('dynamodb', region_name=Config.AWS_REGION)
    table = dynamodb.Table(Config.DYNAMODB_TABLE_NAME)

    # Assume `data` is a dictionary that matches your DynamoDB schema
    table.put_item(Item=data)
    print(f"Inserted {data['title']} into DynamoDB.")

