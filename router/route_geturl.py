from typing import List
from fastapi import APIRouter
from fastapi import Request
from schemas import AnimeUrl
from decouple import config

router = APIRouter()

@router.get("/api/geturl/image", response_model=AnimeUrl)
def get_url_image(request: Request, malAnimeId: str):
    access_token = config(ACCESS_TOKEN)
    header = {
            "Authorization": "Bearer " + access_token,
            }
    param = {
        "anime_id":malAnimeId,
        "fields": ["main_picture"],
    }
    url = "https://api.myanimelist.net/v2/anime/" + malAnimeId
    r = requests.get(url,headers=header,params=param)
    return {
        "data": [
            {
                "url": str(r.json()["main_picture"]["large"])
            }
        ]
    }

@router.get("/api/geturl/pv", response_model=AnimeUrl)
def get_url_pv(request: Request, malAnimeId: str):
    access_token = config(ACCESS_TOKEN)
    header = {
            "Authorization": "Bearer " + access_token,
            }
    param = {
        "anime_id":malAnimeId,
        "fields": ["videos"],
    }
    url = "https://api.myanimelist.net/v2/anime/" + malAnimeId
    r = requests.get(url,headers=header,params=param)
    return {
        "data": [
            {
                "url": str(pvinfo["url"])
            }
            for pvinfo in r.json()["videos"]
        ]
    }