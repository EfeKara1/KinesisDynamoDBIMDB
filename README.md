# Kinesis Firehose IMDB Pipeline

This project demonstrates a data engineering pipeline using **Amazon Kinesis Firehose** to stream an IMDB dataset to an S3 bucket.

## Architecture
1. **Kinesis Producer**: Reads IMDB data and sends it to Kinesis Firehose.
2. **Kinesis Firehose**: Delivers streaming data to an S3 bucket.
3. **Amazon S3**: Stores the streamed data.
4. **Amazon DynamoDB**: A fully managed NoSQL database service where the processed data is stored.
## Setup Instructions

### Prerequisites
- Python 3.x
- AWS Account
- IAM Role with access to Kinesis Firehose and S3
- Boto3 library installed (`pip install boto3`)

### Step-by-Step Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kinesis_imdb_pipeline.git
   cd kinesis_imdb_pipeline

## Project Structure

kinesis_imdb_pipeline/
├── src/                  # Source code
│   ├── consumer.py       # Kinesis Consumer code to write to DynamoDB
│   ├── create_firehose_stream.py   # Script to create Kinesis Firehose and S3 bucket
│   ├── dynamodb_utils.py # Helper functions for DynamoDB setup
│   ├── producer.py       # Kinesis Producer code
│   └── config.py        # Configuration for Kinesis Firehose, S3, and DynamoDB
├── data/                 # Dataset
│   └── imdb_1000.csv     # Sample dataset for local testing
├── tests/                # Unit tests
│   └── test_pipeline.py  # Tests for producer and consumer
├── requirements.txt      # Python dependencies
├── README.md             # Project overview and setup instructions
└── .gitignore            # Ignored files
