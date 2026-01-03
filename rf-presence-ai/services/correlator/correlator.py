from fastapi import FastAPI, Request
from prometheus_client import Counter, Gauge, generate_latest
from datetime import datetime

app = FastAPI()

rf_events = Counter("rf_events_total", "RF events")
unknown_devices_nearby = Gauge("unknown_devices_nearby", "Unknown nearby devices")
correlations_total = Counter("correlations_total", "Correlations")

@app.post("/rf-events")
async def rf_event(ev: dict):
    rf_events.inc()
    if not ev.get("known"):
        unknown_devices_nearby.inc()
    return {"ok": True}

@app.get("/metrics")
def metrics():
    return generate_latest()

@app.post("/alerts/webhook")
async def alert(req: Request):
    return {"received": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
