# coding: utf-8

from botornado.s3.connection import AsyncS3Connection
from botornado.s3.bucket import AsyncBucket
import urllib2

import thumbor_aws.connection
import thumbor.loaders.http_loader as http_loader

def _get_bucket(url):
    """
    Returns a tuple containing bucket name and bucket path.
    url: A string of the format /bucket.name/file/path/in/bucket
    """

    url_by_piece = url.lstrip("/").split("/")
    bucket_name = url_by_piece[0]
    bucket_path = "/".join(url_by_piece[1:])
    return bucket_name, bucket_path

def _validate_bucket(context,bucket):
    if not context.config.S3_ALLOWED_BUCKETS:
        return True

    for allowed in context.config.S3_ALLOWED_BUCKETS:
        #s3 is case sensitive
        if allowed == bucket:
            return True

    return False


def _establish_connection(context_config):
    conn = connection
    if conn is None:
        # Store connection not bucket
        conn = AsyncS3Connection(
            context_config.AWS_ACCESS_KEY,
            context_config.AWS_SECRET_KEY
        )

    return conn

def load(context, url, callback):
    
    enable_http_loader = context.config.get('AWS_ENABLE_HTTP_LOADER', default=False)

    if enable_http_loader and 'http' in url:
        return http_loader.load(context, url, callback)
      
    url = urllib2.unquote(url)
    
    if context.config.S3_LOADER_BUCKET:
        bucket = context.config.S3_LOADER_BUCKET
    else:
        bucket, url = _get_bucket(url)
        if not _validate_bucket(context, bucket):
            return callback(None)

    conn = _establish_connection(context.config)

    bucket_loader = AsyncBucket(
        connection=conn,
        name=bucket
    )

    def key_callback(file_key):
        if file_key:
            file_key.read(callback=callback)
        else:
            callback(None)

    bucket_loader.get_key(url, callback=key_callback)
