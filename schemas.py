from pydantic import BaseModel
from typing import Optional, List
from decouple import config

class SuccessMsg(BaseModel):
    message: str

class RecommendWorks(BaseModel):
    annictId: int
    score: float
class AnimeInfo(BaseModel):
    data: list[RecommendWorks]
