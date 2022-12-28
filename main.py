from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from router import route_recommend, route_malItems
from schemas import CsrfSettings, SuccessMsg
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
