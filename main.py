from fastapi import FastAPI
from router import route_recommend
app = FastAPI()
app.include_router(route_recommend.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}