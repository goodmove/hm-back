import boto3
from botocore.exceptions import ClientError

bucket = 'hack-moscow-bucket'


def upload_file(file_path, object_name):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, bucket, object_name)
    boto3.resource('s3').ObjectAcl(bucket, object_name).put(ACL='public-read')

