from typing import List
from fastapi import APIRouter
from fastapi import Request
from schemas import AnimeUrl
from decouple import config
import requests

router = APIRouter()

@router.get("/api/geturl/image", response_model=AnimeUrl)
def get_url_image(request: Request, malAnimeId: str):
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImMzZTQ4MjkyYjk2ZDgxYzUxYTFlMDI1NjYzMjI5ZmZiM2FmNmYxYmNjY2ZkNjQ1OTE0MTFhNzhhMTRjODQzOWFiZWQ5YTNjNGU0N2VmODhlIn0.eyJhdWQiOiI4M2I3NGJkZDBlMzdmMDViZjU5MjJmMWYwODkyMWI3ZCIsImp0aSI6ImMzZTQ4MjkyYjk2ZDgxYzUxYTFlMDI1NjYzMjI5ZmZiM2FmNmYxYmNjY2ZkNjQ1OTE0MTFhNzhhMTRjODQzOWFiZWQ5YTNjNGU0N2VmODhlIiwiaWF0IjoxNjY5NjQ1NTgzLCJuYmYiOjE2Njk2NDU1ODMsImV4cCI6MTY3MjIzNzU4Mywic3ViIjoiMTU5MTEzOTkiLCJzY29wZXMiOltdfQ.ax5VgGTk7Vd4xBEz7iLtXETh5x4kynfAVn49JfRcLWL6foiy1zxKjzp0ShJEhkuxXbL3U7m1o6sR2-5gM43gy9MWf9mCmO3u1M4zR0rn7133IoWIFBWb28x20qdL38l_7JgFhXUjcMHj61asKeVPgWS-TSpKEDubYheJAUrJQIDNn-ctKtX7s10oEa9G6uBhWft7NFX4u8PFg7fBeU8nwGxMJfCATm4Lfj4vZFJb4cT05SyJ53DWsziL25M2ouLiD01gvxwAlZ5Hpcg5y9DR-t533uBKjnnIXwAjyHVR3VG0KmE-tXUfx89fjIpTVqARoW5Lwk-udryBxMlXfe_0_g"
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
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImMzZTQ4MjkyYjk2ZDgxYzUxYTFlMDI1NjYzMjI5ZmZiM2FmNmYxYmNjY2ZkNjQ1OTE0MTFhNzhhMTRjODQzOWFiZWQ5YTNjNGU0N2VmODhlIn0.eyJhdWQiOiI4M2I3NGJkZDBlMzdmMDViZjU5MjJmMWYwODkyMWI3ZCIsImp0aSI6ImMzZTQ4MjkyYjk2ZDgxYzUxYTFlMDI1NjYzMjI5ZmZiM2FmNmYxYmNjY2ZkNjQ1OTE0MTFhNzhhMTRjODQzOWFiZWQ5YTNjNGU0N2VmODhlIiwiaWF0IjoxNjY5NjQ1NTgzLCJuYmYiOjE2Njk2NDU1ODMsImV4cCI6MTY3MjIzNzU4Mywic3ViIjoiMTU5MTEzOTkiLCJzY29wZXMiOltdfQ.ax5VgGTk7Vd4xBEz7iLtXETh5x4kynfAVn49JfRcLWL6foiy1zxKjzp0ShJEhkuxXbL3U7m1o6sR2-5gM43gy9MWf9mCmO3u1M4zR0rn7133IoWIFBWb28x20qdL38l_7JgFhXUjcMHj61asKeVPgWS-TSpKEDubYheJAUrJQIDNn-ctKtX7s10oEa9G6uBhWft7NFX4u8PFg7fBeU8nwGxMJfCATm4Lfj4vZFJb4cT05SyJ53DWsziL25M2ouLiD01gvxwAlZ5Hpcg5y9DR-t533uBKjnnIXwAjyHVR3VG0KmE-tXUfx89fjIpTVqARoW5Lwk-udryBxMlXfe_0_g"
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