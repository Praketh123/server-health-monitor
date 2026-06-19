# Server Health Monitor

A Python script that monitors real-time server health metrics — CPU usage, memory usage, and disk usage — and logs them to a file at regular intervals.

## What It Does
- Tracks CPU usage percentage
- Tracks memory usage (used/total GB and percentage)
- Tracks disk usage (used/total GB and percentage)
- Logs results to `health_log.txt` every 10 seconds
- Prints live output to the terminal

## Why I Built This
As a Hardware Validation Engineer working on Azure server infrastructure, I wanted to apply Python to something relevant to my domain — basic server health monitoring. This was my first hands-on Python project as I transition toward AI Engineering.

## Tech Used
- Python 3
- psutil library

## How to Run
```bash
pip3 install psutil
python3 server_health.py
```

## Next Steps
- Add threshold-based alerts (warn when CPU/memory crosses a limit)
- Send alerts via email or Slack
- Visualize logged data with a simple chart
