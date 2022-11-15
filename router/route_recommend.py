from typing import List
from fastapi import APIRouter
from fastapi import Response, Request, HTTPException, Depends, Query
from schemas import AnimeInfo
from models.train import Recommendation
router = APIRouter()
recommend = Recommendation()
@router.get("/api/recommend/", response_model=AnimeInfo)
def get_recommend_annictId(request: Request, user_likes: List[int] = Query(None)):
    recommend_annictId, reccomend_scores = recommend.recommend_animes(user_likes)
    return {
        "data": [
            {
                "annictId": int(singleId),
                "score": float(singleScore),
            }
            for singleId, singleScore in zip(recommend_annictId, reccomend_scores)
        ]
    }
