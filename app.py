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
