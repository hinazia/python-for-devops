import boto3

class AWSUtilsFile:

    def __init__(self):
        self.s3_client = self.get_service("s3")
        self.ec2_client = self.get_service("ec2")
        
    def get_service(self, service):
        return boto3.client(service)


    def show_buckets(self):
        bucket_list = []
        response = self.s3_client.list_buckets()["Buckets"]
        for bucket in response:
            #print(bucket)
            bucket_list.append({
                "Name" : bucket["Name"],
                "CreationDate" : bucket["CreationDate"]
                })
        print(bucket_list)
        return (bucket_list)

    def create_bucket(self, bucket_name):
        try:
            response = self.s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                'LocationConstraint': 'eu-central-1',
            },
            )
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print("Bucket created Successfully")
            else:
                print("Bucket not created Successfully")

        except:
            print("Error occured")

    def show_regions(self):
        response = self.ec2_client.describe_regions()
        return response
