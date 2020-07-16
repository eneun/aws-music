from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    aws_region = ''
    bucket_name = ''
    custom_domain = ''