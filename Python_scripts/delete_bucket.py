#!/usr/bin/python
# Delete a Cloud Storage bucket.

import os
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
