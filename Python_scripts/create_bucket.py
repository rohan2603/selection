#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create a new Cloud Storage bucket on GCP.

import os
from google.cloud import storage
from google.cloud.exceptions import Conflict

def main():
    name_of_bucket = os.environ['name_of_bucket']
    region = os.environ['region']
    print('Bucket name to be created is : ' + name_of_bucket)
    print('Creating bucket ...')
    # Instantiate the client.
    client = storage.Client()
    try:
        # Instantiate the bucket.
        bucket = client.bucket(name_of_bucket)

        # Create the bucket object.
        bucket.create(location=region)
        print('\nCreated')

    except Conflict:
        print('Error: Bucket already exists!!')
        pass

    return
      
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()