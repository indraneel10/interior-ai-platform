from fastapi import FastAPI

from app.routers.lead_router import router as lead_router
from app.routers.conversation_router import router as conversation_router

app = FastAPI(
    title="Interior AI Platform"
)

app.include_router(lead_router)
app.include_router(conversation_router)


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