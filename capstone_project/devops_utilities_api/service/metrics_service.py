import psutil

def get_system_metrics():

    """
        This API will return the system Metrics (CPU Usage, Memory, disk percentage)
        Based on the CPU Threshold
    """

    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent  # To calculate in percentage
    disk_percent = psutil.disk_usage("/").percent   # / disk usage of root folder or directory

    cpu_threshold = 20

    status = "High CPU" if cpu_percent > cpu_threshold else "Healthy"
    print("System Metrics (CPU Usage, Memory, disk percentage)")

    return {
        "cpu_percentage":cpu_percent,
        "memory_percentage":memory_percent,
        "disk_percentage":disk_percent,
        "cpu_threshold":cpu_threshold,
        "system_status":status
    }
        

