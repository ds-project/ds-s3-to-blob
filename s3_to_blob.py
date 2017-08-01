"""
From S3 URL to Azure blob on Azure Function, Python 3.5.2
"""

import os
import json
import platform

import urllib.request
from azure.storage.blob import BlockBlobService, ContentSettings


# Check python version.
message = "Using Python '{0}'".format(platform.python_version())
print(message)

# Get s3 url path and retrive filename.
postreqdata = json.loads(open(os.environ['req']).read())
s3_path = postreqdata['url']
filename = s3_path.split('/')[-1]

# Download File.
print(filename)
urllib.request.urlretrieve(s3_path, filename)

# Add file to azure blob.
account_name = '<Your Account Name>'
account_key = '<Your Account Key>'
container = '<Target Container>'
block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
block_blob_service.create_blob_from_path(
    container,
    filename,
    filename,
    content_settings=ContentSettings(content_type='plain/txt')
    )

response = open(os.environ['res'], 'w')
response.write("Complete Process of url "+postreqdata['url'])
response.close()
