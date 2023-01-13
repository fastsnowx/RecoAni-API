from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import route_recommend, route_malItems
from schemas import SuccessMsg
from decouple import config
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

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


@cache()
async def get_cache():
    return 1


@app.get("/", response_model=SuccessMsg)
@cache(expire=60)
async def root():
    return {"message": "Welcome to Annict recommend API"}


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        config("REDIS_UPSTASH_TOKEN"), encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
