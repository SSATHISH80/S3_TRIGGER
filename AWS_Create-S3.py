import boto3
s3_user=boto3.client('s3')
output = s3_user.create_bucket(ACL='private', Bucket='sathish-kongu-assignment-r32wsa')
print(output)