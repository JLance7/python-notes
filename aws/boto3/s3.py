import boto3
from botocore.exceptions import ClientError
import logging


def initialize_logger():
  logger = logging.getLogger(__name__)
  logging.basicConfig(
      format=f'%(asctime)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S'
  )
  logger.setLevel(logging.INFO)
  return logger

logger = initialize_logger()
region = 'us-east-1'
s3_client = boto3.client('s3', region_name = region)

def get_object_name(s3_uri: str):
  """Get the bucket and object name from the s3_uri""" 
  split = s3_uri.replace('s3://', '').split('/')
  bucket = split[0]
  object_name = '/'.join(split[1:])
  return bucket, object_name
    

def upload_file(self, s3_uri: str, upload_file_name: str):
  """Upload a file to an S3 bucket """
  bucket, object_name = self._get_object_name(s3_uri)
  # Upload the file
  try:
    logger.info('Uploading file')
    logger.info(f'bucket: {bucket}, object_name: {object_name}, upload_file_name: {upload_file_name}')
    s3_client.upload_file(upload_file_name, bucket, object_name)
    logger.info(f'Succesfully uploaded file')
  except ClientError as e:
    logger.error(e)
    return False
  return True


def download_file(self, s3_uri: str, download_to_file_name: str):
  """Download a file from an S3 bucket"""
  bucket, object_name = self._get_object_name(s3_uri)
  # Download the file
  try:
    logger.info(f'bucket: {bucket}, object_name: {object_name}, download_to_file_name: {download_to_file_name}')
    logger.info('Downloading file')
    s3_client.download_file(bucket, object_name, download_to_file_name)
    logger.info('Succesfully downloaded file')
    return
  except ClientError as e:
    self.logger.error(e)
    return False
  return True