from fastapi import APIRouter, HTTPException
from service.metrics_service import get_system_metrics

router = APIRouter()

@router.get("/metrics",status_code = 200)

def get_metrics():
    try:
        print("System Metrics (CPU Usage, Memory, disk percentage)")
        metrics = get_system_metrics()
        return metrics

    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
        

