import pandas as pd
import boto3
import json
from config import Config

def kinesis_producer():
    kinesis_client = boto3.client('firehose', region_name=Config.AWS_REGION)

    # Load the dataset
    df = pd.read_csv(Config.IMDB_DATASET_PATH)

    for index, row in df.iterrows():
        data = {
            'star_rating': row['star_rating'],
            'title': row['title'],
            'content_rating': row['content_rating'],
            'genre': row['genre'],
            'duration': row['duration'],
            'actors_list': row['actors_list'].split(', ')  # Split into a list
        }
        
        # Send the data to Kinesis Firehose
        kinesis_client.put_record(
            DeliveryStreamName=Config.KINESIS_FIREHOSE_NAME,
            Record={'Data': json.dumps(data)}
        )
        print(f"Sent data to Firehose: {data}")

if __name__ == "__main__":
    kinesis_producer()

