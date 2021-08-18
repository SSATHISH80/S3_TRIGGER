import boto3
s3_user=boto3.client('s3')
output_s3=s3_user.upload_file('hotel_management.py' , 'sathish-kongu-assignment-r32wsa', 'hotel_management.py')