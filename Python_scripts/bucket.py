import os
name_of_bucket = os.environ['name_of_bucket']
region = os.environ['region']

# print("bucket gcp")
# print("Name is  :",name_of_service)
# print("Region is", region)

print("Storage Bucket with name",name_of_bucket,"is created in region",region)