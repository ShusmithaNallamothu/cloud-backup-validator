import boto3

s3 = boto3.client('s3')

def upload_file(file_path, bucket_name):
    filename = file_path.split("/")[-1]
    s3.upload_file(file_path, bucket_name, filename)
    print("Upload successful")

def restore_file(bucket_name, filename):
    s3.download_file(bucket_name, filename, "restored_files/" + filename)
    print("File restored")