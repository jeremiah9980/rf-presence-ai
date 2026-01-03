import requests, yaml, time
from datetime import datetime
cfg = yaml.safe_load(open("config.yaml"))
while True:
    requests.post(cfg["upload_url"], json={
        "timestamp": datetime.utcnow().isoformat(),
        "known": False,
        "rssi": -45
    })
    time.sleep(5)
