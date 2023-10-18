import boto3 #aws sdk

ecr_client = boto3.client('ecr')

repository_name = "my_cloud-native_repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)

# makes aws ecr repository
# 948717518254.dkr.ecr.us-east-1.amazonaws.com/my_cloud-native_repo


#Push image to ecr repo
# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 948717518254.dkr.ecr.us-east-1.amazonaws.com
# docker build -t my_cloud-native_repo .
# docker tag my_cloud-native_repo:latest 948717518254.dkr.ecr.us-east-1.amazonaws.com/my_cloud-native_repo:latest
# docker push 948717518254.dkr.ecr.us-east-1.amazonaws.com/my_cloud-native_repo:latest
