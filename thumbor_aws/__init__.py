# coding: utf-8
from thumbor.config import Config
Config.define('STORAGE_BUCKET', 'thumbor-images','S3 bucket for Storage', 'S3 Storage')
Config.define('RESULT_STORAGE_BUCKET', 'thumbor-result', 'S3 bucket for result Storage', 'S3 Result Storage')
Config.define('S3_LOADER_BUCKET','thumbor-images','S3 bucket for loader', 'S3 Loader')
Config.define('RESULT_STORAGE_AWS_STORAGE_ROOT_PATH','', 'S3 path prefix', 'S3 Storage')
Config.define('STORAGE_EXPIRATION_SECONDS', 3600, 'S3 expiration', 'S3 Storage')
Config.define('S3_STORAGE_SSE', False, 'S3 encriptipon key', 'S3 Storage')
Config.define('S3_STORAGE_RRS', False, 'S3 redundency', 'S3 Storage')
Config.define('S3_ALLOWED_BUCKETS', False, 'List of allowed bucket to be requeted', 'S3 Loader')

Config.define('AWS_ACCESS_KEY', None, 'AWS Access key, if None use environment AWS_ACCESS_KEY_ID', 'AWS')
Config.define('AWS_SECRET_KEY', None, 'AWS Secret key, if None use environment AWS_SECRET_ACCESS_KEY', 'AWS')

