from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import route_recommend, route_malItems
from schemas import SuccessMsg
from decouple import config

RECOANI_WEB_URL = config("RECOANI_WEB_URL")
app = FastAPI()
app.include_router(route_recommend.router)
app.include_router(route_malItems.router)

origins = ["http://localhost:3000", RECOANI_WEB_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=SuccessMsg)
async def root():
    return {"message": "Welcome to Annict recommend API"}
