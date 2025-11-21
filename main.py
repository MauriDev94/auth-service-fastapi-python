from fastapi import FastAPI
from src.features.auth.interface.routers.auth_router import router as auth_router

app = FastAPI(title="User Registration API", version="1.0.0")

# routers
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
