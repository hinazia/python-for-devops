from fastapi import APIRouter
from service.aws_service import AWSUtilsFile

router = APIRouter()
aws = AWSUtilsFile()

@router.get("/s3")
def get_s3_buckets():
    try:
        aws.create_bucket("hina-098765-bucket")
        list_bucket = aws.show_buckets()
        return list_bucket
        

    except Exception as e:
        print(e)

@router.get("/ec2")
def get_region():
    return aws.show_regions() #will not work because user is not given permission in aws

# def create_bucket():
#     aws.create_bucket("hina-123455-bucket")
    

