import boto3
s3 = boto3.client('s3')
s3.upload_file('C:/Gowshi/Pics/CVP courses/1.png', 'boto3buck', 'hello.png')
s3.delete_object(Bucket='boto3buck',Key= 'hello.txt')