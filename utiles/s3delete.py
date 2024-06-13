import boto3

def empty_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    # Delete all objects
    #print(f"Deleting all objects from bucket: {bucket_name}")
    #bucket.objects.all().delete()
    
    versioning = s3.BucketVersioning(bucket_name)
    if versioning.status == 'Enabled':
        print(f"Deleting all versions from bucket: {bucket_name}")
        bucket.object_versions.all().delete()

def delete_bucket(bucket_name):
    s3 = boto3.client('s3')
    empty_bucket(bucket_name)
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted")


if __name__ == '__main__':
    bucket_name = 'bucketname'
    delete_bucket(bucket_name)

