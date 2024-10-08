# Kinesis Firehose IMDB Pipeline

This project demonstrates a data engineering pipeline using **Amazon Kinesis Firehose** to stream an IMDB dataset to an S3 bucket.

## Architecture
1. **Kinesis Producer**: Reads IMDB data and sends it to Kinesis Firehose.
2. **Kinesis Firehose**: Delivers streaming data to an S3 bucket.
3. **Amazon S3**: Stores the streamed data.

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

