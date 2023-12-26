import json
import os
import logging
import boto3


def initialize_logger():
  logger = logging.getLogger(__name__)
  logging.basicConfig(
      format=f'%(asctime)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S'
  )
  logger.setLevel(logging.INFO)
  return logger


def generate_respone(status, message):
  response_object = {}
  response_object.status = status
  try:
    response_object.message = json.dumps(message)
  except: 
    response_object.message = message
  return response_object


def handler(event, context): 
  logger = initialize_logger()
  key = event.key
  logger.info(key)
  method = event['httpMethod']
  path = event['resource']
  query = event['queryStringParameters']
  logger.info(f'method: {method} - path: {path} - query: {query}')
  
  status = 200
  message = 'success'
  response_object = generate_respone(status, message)
  return response_object


# for testing
if __name__ == '__main__':
  event = {
    'key': 'val',
    'httpMethod': 'GET',
    'resource': 'get_nice_messagge',
    'query': ''
  }
  context = 'test'
  handler(event, context)