from fastapi import FastAPI
from app.routers.auth_router import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "Welcome to Hair Salon API"}
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
'''