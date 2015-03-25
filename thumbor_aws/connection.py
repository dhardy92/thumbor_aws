# coding: utf-8

from botornado.s3.connection import AsyncS3Connection

connection = None

def get_connection(context):
    conn = connection
    if conn is None:
        if context.config.AWS_ROLE_BASED_CONNECTION:
            conn = AsyncS3Connection()
        else:
            conn = AsyncS3Connection(
                context.config.AWS_ACCESS_KEY,
                context.config.AWS_SECRET_KEY
            )

    return conn
