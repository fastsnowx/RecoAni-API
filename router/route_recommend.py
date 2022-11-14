from fastapi import APIRouter
from fastapi import Response, Request, HTTPException, Depends
from schemas import SuccessMsg
from models.train import Recommendation
router = APIRouter()
recommend = Recommendation()
@router.get("/api/recommend/{id}") # WIP 複数のannictIdを入力したい
def get_recommend_annictId(request: Request, id):
    recommend_annictId, _ = recommend.recommend_animes([6059, 1113])
    return {
        "items": [
            {
                "annictId": float(singleId),
            }
            for singleId in recommend_annictId
        ]
    }

@router.get('/article/{id}')
def get_article(id):
    return {'message': f'article is {id}'}