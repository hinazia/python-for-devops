from fastapi import FastAPI
from sample_log_analyzer import LogAnalyzer
from s3_utilities_prac import AWSUtilsFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Log Analyzer Check"}

@app.get("/health")
def health_check():
    return {"Status" : "Ok"}

@app.get("/log")
def logs(file: str):
    analyze_log = LogAnalyzer(file)
    log_lines = analyze_log.read_logs()
    result = analyze_log.analyze(log_lines)
    return result

@app.get("/buckets")
def list_buckets():
    aws = AWSUtilsFile()
    return aws.show_buckets()



