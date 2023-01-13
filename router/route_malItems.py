from fastapi import APIRouter
from fastapi import Request, HTTPException
from schemas import MyAnimeListImageInfo, MyAnimeListPVInfo
from decouple import config
import requests
from fastapi_cache.decorator import cache

router = APIRouter()
MAL_API_TOKEN = config("MAL_API_TOKEN")


@router.get("/api/mal/image", response_model=MyAnimeListImageInfo)
@cache(expire=60 * 60 * 12)
def get_mal_image_url(request: Request, malAnimeId: str):
    header = {
        "X-MAL-CLIENT-ID": MAL_API_TOKEN,
    }
    param = {
        "anime_id": malAnimeId,
        "fields": ["main_picture"],
    }
    url = f"https://api.myanimelist.net/v2/anime/{malAnimeId}"
    response = requests.get(url, headers=header, params=param)
    if "main_picture" in response.json().keys():
        return {"data": [{"url": str(response.json()["main_picture"]["large"])}]}
    else:
        raise HTTPException(status_code=404, detail=f"Image not found")


@router.get("/api/mal/pv", response_model=MyAnimeListPVInfo)
@cache(expire=60 * 60 * 12)
def get_mal_pv_url(request: Request, malAnimeId: str):
    header = {
        "X-MAL-CLIENT-ID": MAL_API_TOKEN,
    }
    param = {
        "anime_id": malAnimeId,
        "fields": ["videos"],
    }
    url = f"https://api.myanimelist.net/v2/anime/{malAnimeId}"
    response = requests.get(url, headers=header, params=param)
    if "videos" in response.json().keys():
        return {
            "data": [
                {"url": str(pvinfo["url"])} for pvinfo in response.json()["videos"]
            ]
        }
    else:
        raise HTTPException(status_code=404, detail=f"PV not found")
