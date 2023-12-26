from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
import pyspark
from pyspark.sql import SparkSession
import logging
import boto3
import pandas as pd
import sys


def initialize_logger():
  logger = logging.getLogger('Incremental insert to odf.ecsr')
  logger.setLevel(logging.INFO)
  handler = logging.StreamHandler(sys.stdout)
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)  
  logger.addHandler(handler)
  

def main():
  app_name = ''
  sc = SparkContext().getOrCreate()
  glueContext = GlueContext(sc)
  job = Job(glueContext)
  spark = SparkSession.builder.appName(app_name).getOrCreate()
  args = getResolvedOptions(sys.argv, ['JOB_NAME', ''])
  job.init(args['JOB_NAME'])
  run()


def run():
  logger.info('Starting')


if __name__ == '__main__':
  logger = initialize_logger()
  main()