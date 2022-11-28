from typing import List
from fastapi import APIRouter
from fastapi import Response, Request, HTTPException, Depends, Query
from schemas import AnimeInfo
from models.train import Recommendation
router = APIRouter()
recommendOverall = Recommendation("ratingOverallState")
recommendStory = Recommendation("ratingStoryState")
recommendMusic = Recommendation("ratingMusicState")

@router.get("/api/recommend/overall", response_model=AnimeInfo)
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

@router.get("/api/recommend/story", response_model=AnimeInfo)
def get_recommend_story(request: Request, user_likes: List[int] = Query(None)):
    recommend_annictId, reccomend_scores = recommendStory.recommend_animes(user_likes)
    return {
        "data": [
            {
                "annictId": int(singleId),
                "score": float(singleScore),
            }
            for singleId, singleScore in zip(recommend_annictId, reccomend_scores)
        ]
    }

@router.get("/api/recommend/music", response_model=AnimeInfo)
def get_recommend_music(request: Request, user_likes: List[int] = Query(None)):
    recommend_annictId, reccomend_scores = recommendMusic.recommend_animes(user_likes)
    return {
        "data": [
            {
                "annictId": int(singleId),
                "score": float(singleScore),
            }
            for singleId, singleScore in zip(recommend_annictId, reccomend_scores)
        ]
    }

