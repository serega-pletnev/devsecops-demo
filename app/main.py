from fastapi import FastAPI, Response

app = FastAPI(title="devsecops-demo")

@app.get("/", include_in_schema=False)
def root():
    # корневой эндпоинт для smoke/статуса
    return {"ok": True, "app": "devsecops-demo"}

@app.get("/healthz", include_in_schema=False)
def healthz():
    # основной health для GET
    return {"status": "ok"}

@app.head("/healthz", include_in_schema=False)
def healthz_head():
    # поддержка HEAD, чтобы curl -I/гейты не падали на 405
    return Response(status_code=200)
