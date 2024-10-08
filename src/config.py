import os

class Config:
    # AWS Configurations
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')

    # Kinesis Firehose Configurations
    KINESIS_FIREHOSE_NAME = os.getenv('KINESIS_FIREHOSE_NAME', 'imdb-firehose')
    KINESIS_FIREHOSE_ROLE_ARN = os.getenv('KINESIS_FIREHOSE_ROLE_ARN', 'your-iam-role-arn')

    # DynamoDB Configurations
    DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME', 'IMDBMovies')

    # S3 Configurations
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'your-s3-bucket')

    # IMDB Dataset
    IMDB_DATASET_PATH = os.getenv('IMDB_DATASET_PATH', './data/imdb_1000.csv')

