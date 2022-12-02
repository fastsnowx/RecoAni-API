from typing import List
from fastapi import APIRouter
from fastapi import Response, Request, HTTPException, Depends, Query
from schemas import RecommendAnimeInfo
from models.train import Recommendation
router = APIRouter()
recommendOverall = Recommendation(ratingState="ratingOverallState")
# recommendStory = Recommendation(ratingState="ratingStoryState")
# recommendMusic = Recommendation(ratingState="ratingMusicState")
# recommendCharacter = Recommendation(ratingState="ratingCharacterState")
# recommendAnimation = Recommendation(ratingState="ratingAnimationState")

@router.get("/api/recommend/overall", response_model=RecommendAnimeInfo)
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

@router.get("/api/recommend/story", response_model=RecommendAnimeInfo)
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

@router.get("/api/recommend/music", response_model=RecommendAnimeInfo)
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

@router.get("/api/recommend/character", response_model=RecommendAnimeInfo)
def get_recommend_character(request: Request, user_likes: List[int] = Query(None)):
    recommend_annictId, reccomend_scores = recommendCharacter.recommend_animes(user_likes)
    return {
        "data": [
            {
                "annictId": int(singleId),
                "score": float(singleScore),
            }
            for singleId, singleScore in zip(recommend_annictId, reccomend_scores)
        ]
    }

@router.get("/api/recommend/animation", response_model=RecommendAnimeInfo)
def get_recommend_animation(request: Request, user_likes: List[int] = Query(None)):
    recommend_annictId, reccomend_scores = recommendAnimation.recommend_animes(user_likes)
    return {
        "data": [
            {
                "annictId": int(singleId),
                "score": float(singleScore),
            }
            for singleId, singleScore in zip(recommend_annictId, reccomend_scores)
        ]
    }
