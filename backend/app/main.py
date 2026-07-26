from fastapi import FastAPI

from app.routers.lead_router import router as lead_router

app = FastAPI(
    title="Interior AI Platform"
)

app.include_router(lead_router)


@app.get("/")
def root():

    return {
        "message": "Interior AI Platform Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }