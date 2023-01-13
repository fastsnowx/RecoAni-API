from pydantic import BaseModel
from typing import List

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
