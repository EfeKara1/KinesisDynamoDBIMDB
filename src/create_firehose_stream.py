import boto3
import json
import os
from botocore.exceptions import ClientError
from config import Config

def create_firehose():
    firehose_client = boto3.client('firehose', region_name=Config.AWS_REGION)

    try:
        response = firehose_client.create_delivery_stream(
            DeliveryStreamName=Config.KINESIS_FIREHOSE_NAME,
            S3DestinationConfiguration={
                'BucketARN': f'arn:aws:s3:::{Config.S3_BUCKET_NAME}',
                'RoleARN': Config.KINESIS_FIREHOSE_ROLE_ARN,
                'Prefix': 'imdb/',
                'BufferingHints': {
                    'SizeInMBs': 5,
                    'IntervalInSeconds': 300
                },
                'CompressionFormat': 'UNCOMPRESSED',
            }
        )
        print(f"Created Kinesis Firehose Delivery Stream: {response['DeliveryStreamARN']}")
    except ClientError as e:
        print(f"Error creating Firehose: {e}")

if __name__ == "__main__":
    create_firehose()

