import boto3
import json
import os
from config import Config
from dynamodb_utils import write_to_dynamodb  # Importing the helper function

def kinesis_consumer():
    kinesis_client = boto3.client('kinesis', region_name=Config.AWS_REGION)

    # Start a Kinesis stream reader
    shard_iterator = kinesis_client.get_shard_iterator(
        StreamName=Config.KINESIS_FIREHOSE_NAME,
        ShardId='shardId-000000000000',  # Adjust according to your shard ID
        ShardIteratorType='LATEST'  # Or TRIM_HORIZON based on your use case
    )['ShardIterator']

    while True:
        response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=10)
        records = response['Records']
        
        for record in records:
            data = json.loads(record['Data'])
            write_to_dynamodb(data)

        shard_iterator = response['NextShardIterator']

if __name__ == "__main__":
    kinesis_consumer()

