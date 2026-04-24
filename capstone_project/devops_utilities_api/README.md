# Internal DevOps Utilities API

## Aim
 Internal AWS API surface for common DevOps utilities, intended for internal teams:

    - AWS Resources API
    - Metrics API

## Features
    - Fetch S3 buckets using boto3
    - List EC2 regions
    - FastAPI endpoints for interaction

## Run Locally
uvicorn main:app --reload

## API Endpoints

    -  /aws/s3 ---> To craete and lists buckets
    -  /aws/ec2 ---> Shows all EC2 regions 
    -  /metrics ----> CPU metrics

## Usage

### In Bash

    - clone the repository 
            git clone <repository name>

    - create the virtual environment and activate it 
            python -m venv env
            env/Scripts/activate

    - install the requirements.txt file
            pip install -r requirements.txt

    - run main.py
            py main.py


