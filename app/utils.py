import os
import time

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return {"seconds": uptime_seconds, "minutes": round(uptime_seconds / 60, 2)}
    except Exception as e:
        return {"error": str(e)}
