from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"ok": True, "app": "devsecops-demo"}
@app.get("/healthz")
def health():
    return {"status": "ok"}
