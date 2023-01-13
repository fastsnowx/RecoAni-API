from typing import List
from fastapi import APIRouter
from fastapi import Response, Request, HTTPException, Depends, Query
from schemas import RecommendAnimeInfo
from models.train import Recommendation
from fastapi_cache.decorator import cache

router = APIRouter()
recommendOverall = Recommendation(ratingState="ratingOverallState")


@router.get("/api/recommend/overall", response_model=RecommendAnimeInfo)
@cache(expire=60 * 60 * 12)
def get_recommend_overall(request: Request, user_likes: List[int] = Query(None)):
    recommend_annictId, reccomend_scores = recommendOverall.recommend_animes(user_likes)
    return {
        "data": [
            {
                "annictId": int(singleId),
                "score": float(singleScore),
            }
            for singleId, singleScore in zip(recommend_annictId, reccomend_scores)
        ]
    }
