from pydantic import BaseModel
from typing import Optional, List
from decouple import config

CSRF_KEY = config("CSRF_KEY")


class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY


class SuccessMsg(BaseModel):
    message: str


class RecommendWorks(BaseModel):
    annictId: int
    score: float


class RecommendAnimeInfo(BaseModel):
    data: List[RecommendWorks]


class MyAnimeListWorks(BaseModel):
    url: str


class MyAnimeListImageInfo(BaseModel):
    data: List[MyAnimeListWorks]


class MyAnimeListPVInfo(BaseModel):
    data: List[MyAnimeListWorks]
