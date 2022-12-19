from fastapi import APIRouter
from fastapi import Request, HTTPException
from schemas import MyAnimeListImageInfo, MyAnimeListPVInfo
from decouple import config
import requests

router = APIRouter()
MAL_API_KEY = config("MAL_API_KEY")


@router.get("/api/mal/image", response_model=MyAnimeListImageInfo)
def get_mal_image_url(request: Request, malAnimeId: str):
    header = {
        "X-MAL-CLIENT-ID": MAL_API_KEY,
    }
    param = {
        "anime_id": malAnimeId,
        "fields": ["main_picture"],
    }
    url = f"https://api.myanimelist.net/v2/anime/{malAnimeId}"
    response = requests.get(url, headers=header, params=param)
    if response.json()["main_picture"]["large"]:
        return {"data": [{"url": str(response.json()["main_picture"]["large"])}]}
    else:
        raise HTTPException(
            status_code=404, detail=f"Image id={malAnimeId} is not found"
        )


@router.get("/api/mal/pv", response_model=MyAnimeListPVInfo)
def get_mal_pv_url(request: Request, malAnimeId: str):
    header = {
        "X-MAL-CLIENT-ID": MAL_API_KEY,
    }
    param = {
        "anime_id": malAnimeId,
        "fields": ["videos"],
    }
    url = f"https://api.myanimelist.net/v2/anime/{malAnimeId}"
    response = requests.get(url, headers=header, params=param)
    if response.json()["videos"]:
        return {
            "data": [
                {"url": str(pvinfo["url"])} for pvinfo in response.json()["videos"]
            ]
        }
    else:
        raise HTTPException(status_code=404, detail=f"PV id={malAnimeId} is not found")
