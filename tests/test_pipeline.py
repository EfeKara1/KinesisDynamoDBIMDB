import unittest
from unittest.mock import patch, MagicMock
import json
from src.producer import kinesis_producer
from src.consumer import kinesis_consumer
from src.config import Config

class TestKinesisPipeline(unittest.TestCase):
    @patch('src.producer.boto3.client')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='star_rating,title,content_rating,genre,duration,actors_list\n8.5,Inception,PG-13,Sci-Fi,148,"Leonardo DiCaprio, Joseph Gordon-Levitt"\n7.9,The Shawshank Redemption,R,Drama,142,"Tim Robbins, Morgan Freeman"')
    def test_kinesis_producer(self, mock_open, mock_boto_client):
        # Mock the Firehose client
        mock_firehose_client = MagicMock()
        mock_boto_client.return_value = mock_firehose_client

        kinesis_producer()

        # Check that put_record was called for each line in the CSV
        self.assertEqual(mock_firehose_client.put_record.call_count, 2)

        # Verify the data sent to Firehose
        calls = mock_firehose_client.put_record.call_args_list
        expected_calls = [
            unittest.mock.call(
                DeliveryStreamName=Config.KINESIS_FIREHOSE_NAME,
                Record={'Data': json.dumps({
                    'star_rating': 8.5,
                    'title': 'Inception',
                    'content_rating': 'PG-13',
                    'genre': 'Sci-Fi',
                    'duration': 148,
                    'actors_list': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt']
                })}
            ),
            unittest.mock.call(
                DeliveryStreamName=Config.KINESIS_FIREHOSE_NAME,
                Record={'Data': json.dumps({
                    'star_rating': 7.9,
                    'title': 'The Shawshank Redemption',
                    'content_rating': 'R',
                    'genre': 'Drama',
                    'duration': 142,
                    'actors_list': ['Tim Robbins', 'Morgan Freeman']
                })}
            )
        ]

        for i, call in enumerate(calls):
            self.assertEqual(call, expected_calls[i])

    @patch('src.consumer.boto3.client')
    @patch('src.dynamodb_utils.write_to_dynamodb')
    def test_kinesis_consumer(self, mock_write_to_dynamodb, mock_boto_client):
        mock_kinesis_client = MagicMock()
        mock_boto_client.return_value = mock_kinesis_client

        # Mock the get_shard_iterator and get_records methods
        mock_kinesis_client.get_shard_iterator.return_value = {
            'ShardIterator': 'iterator'
        }
        mock_kinesis_client.get_records.return_value = {
            'Records': [{'Data': json.dumps({
                'star_rating': 8.5,
                'title': 'Inception',
                'content_rating': 'PG-13',
                'genre': 'Sci-Fi',
                'duration': 148,
                'actors_list': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt']
            })}]
        }

        # Call the consumer function
        kinesis_consumer()

        # Verify that write_to_dynamodb was called with the correct data
        mock_write_to_dynamodb.assert_called_once_with({
            'star_rating': 8.5,
            'title': 'Inception',
            'content_rating': 'PG-13',
            'genre': 'Sci-Fi',
            'duration': 148,
            'actors_list': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt']
        })

if __name__ == '__main__':
    unittest.main()

