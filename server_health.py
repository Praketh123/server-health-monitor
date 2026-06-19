# Server Health Check Logger
# Praketh Bachu - AI Learning Journey Day 1

import psutil
import datetime
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "total_gb": round(memory.total / (1024**3), 2),
        "used_gb": round(memory.used / (1024**3), 2),
        "percent": memory.percent
    }

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "total_gb": round(disk.total / (1024**3), 2),
        "used_gb": round(disk.used / (1024**3), 2),
        "percent": disk.percent
    }

def log_health_check():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    report = f"""
============================
SERVER HEALTH CHECK REPORT
============================
Timestamp : {timestamp}
CPU Usage : {cpu}%
Memory    : {memory['used_gb']} GB used of {memory['total_gb']} GB ({memory['percent']}%)
Disk      : {disk['used_gb']} GB used of {disk['total_gb']} GB ({disk['percent']}%)
============================
"""

    # Check for warnings
    alerts = []
    if cpu > 80:
        alerts.append(f"⚠️ HIGH CPU USAGE: {cpu}%")
    if memory['percent'] > 80:
        alerts.append(f"⚠️ HIGH MEMORY USAGE: {memory['percent']}%")
    if disk['percent'] > 80:
        alerts.append(f"⚠️ HIGH DISK USAGE: {disk['percent']}%")

    if alerts:
        report += "\n".join(alerts) + "\n"

    print(report)

    # Save to a log file
    with open("health_log.txt", "a") as f:
        f.write(report)
    print("✅ Log saved to health_log.txt")

    while True:
        time.sleep(10)  # Wait for 10 seconds before the next check
        log_health_check()