from fastapi import FastAPI
from router import metrics
from router import aws_router

app = FastAPI(
    tilte = "Internal DevOps Utilities API",
    description = "This is an Internal API Utilities App fpr monitoring AWS, CPU metrics, log analysis etc",
    version = "1.1.0",
    doc_url = "/docs",
    redoc_url = "/redoc"
)

@app.get("/")
def hello():
    #Hello API for testing
    return {"message" : "hello"}


app.include_router(metrics.router)
app.include_router(aws_router.router, prefix="/aws")
