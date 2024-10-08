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
├── ─── src/                      # Source code for the pipeline
│    ├── ─── __init__.py          # Makes src a package
│    ├── ─── consumer.py           # Kinesis Consumer to write data to DynamoDB
│    ├── ─── create_firehose.py    # Script to create Kinesis Firehose and S3 bucket
│    ├── ─── dynamodb_utils.py      # Helper functions for DynamoDB interactions
│    ├── ─── producer.py           # Kinesis Producer to stream data
│    └── ─── config.py             # Configuration settings for AWS resources
│
├── ─── data/                     # Directory for datasets
│    ├── ─── imdb_1000.csv         # Sample dataset for processing
│
├── ─── tests/                    # Unit tests for the project
│    ├── ─── __init__.py           # Makes tests a package
│    ├── ─── test_consumer.py      # Tests for the Kinesis consumer
│    ├── ─── test_producer.py      # Tests for the Kinesis producer
│    └── └── test_dynamodb_utils.py  # Tests for DynamoDB utility functions
│
├── ─── requirements.txt           # List of project dependencies
├── ─── README.md                  # Project documentation and setup instructions
├── ─── .gitignore                 # Specifies intentionally untracked files
└── └── LICENSE                    # License for the project
