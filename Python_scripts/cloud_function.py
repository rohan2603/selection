import os
name_of_cloud_function = os.environ['name_of_cloud_function']
region = os.environ['region']

# print("bucket gcp")
# print("Name is  :",name_of_service)
# print("Region is", region)

print("Cloud Function with name",name_of_cloud_function,"is created in region",region)
