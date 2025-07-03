import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from core.run_trading_system import run_trading_system

import threading

app = FastAPI()

@app.get("/health", response_class=PlainTextResponse)
def health():
    return "OK"

@app.on_event("startup")
def start_trader():
    threading.Thread(target=run_trading_system, daemon=True).start()
# Triggering commit box
Fixed import path for run_trading_system
