from typing import List
from fastapi import APIRouter
from fastapi import Request
from schemas import MyAnimeListImage, MyAnimeListPV
from decouple import config
import requests

router = APIRouter()
MAL_API_KEY = config("MAL_API_KEY")

@router.get("/api/mal/image", response_model=MyAnimeListImage)
def get_mal_image_url(request: Request, malAnimeId: str):
    header = {
            "X-MAL-CLIENT-ID":MAL_API_KEY,
            }
    param = {
        "anime_id": malAnimeId,
        "fields": ["main_picture"],
    }
    url = f"https://api.myanimelist.net/v2/anime/{malAnimeId}"
    response = requests.get(url,headers=header,params=param)
    return {
        "data": [
            {
                "url": str(response.json()["main_picture"]["large"])
            }
        ]
    }

@router.get("/api/mal/pv", response_model=MyAnimeListPV)
def get_mal_pv_url(request: Request, malAnimeId: str):
    header = {
            "X-MAL-CLIENT-ID":MAL_API_KEY,
            }
    param = {
        "anime_id": malAnimeId,
        "fields": ["videos"],
    }
    url = f"https://api.myanimelist.net/v2/anime/{malAnimeId}"
    response = requests.get(url,headers=header,params=param)
    return {
        "data": [
            {
                "url": str(pvinfo["url"])
            }
            for pvinfo in response.json()["videos"]
        ]
    }