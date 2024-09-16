from fastapi import FastAPI
from app.routers import items

app = FastAPI()

# Include routers for different modules
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Movies Recommender System!"}
