from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["POST"])
@app.post("/api/latency")
def analyze_latency(body: dict = Body(...)):
    # This is a stub, in reality you'd parse real telemetry
    return {"status": "ok", "email": "24f2001614@ds.study.iitm.ac.in"}
