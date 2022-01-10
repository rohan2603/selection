#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragedelete.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Delete a Cloud Storage bucket.
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket

from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.cloud.exceptions import Forbidden

def main():
    name_of_bucket = os.environ['name_of_bucket']
    print('Bucket name: ' + name_of_bucket)
    print('Deleting bucket ...')
    
    # Instantiate the client.
    client = storage.Client()

    try:
        # Instantiate the bucket.
        bucket = client.bucket(name_of_bucket)
        # Delete the bucket.
        bucket.delete()
        print('\nDeleted')
    except NotFound:
        print('Error: Bucket does NOT exists!!')
        pass
    except Forbidden:
        print('Error: Forbidden, you do not have access to it!!')
        pass
  
    return
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
