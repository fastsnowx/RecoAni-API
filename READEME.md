# RecoAni-API

## 📗開発環境
- Python
- FastAPI
- MongoDB
- Upstash(redis)
- Docker
## 📫API
access `/docs` to get more infomation.
### /api/recommend/overall
- `GET`: get recommended annictId, scores.

### /api/mal/image
- `GET`: get anime cover image from MyAnimeList API.

### /api/mal/pv
- `GET`: get anime pv links from MyAnimeList API.

## 🔒環境変数
```
ANNICT_API_KEY :Annictのtoken
MONGODB_API_KEY : MongoDBのtoken
MAL_API_KEY : MyAnimeListのtoken
REDIS_UPSTASH_TOKEN : Upstash(redis)のtoken
```
## 🚀実行
`.env`を定義した上で
- MongoDB, Upstashの設定
- `updateDatabase.py`を実行
- `uvicorn main:app --reload`

## 👥 contributor
- fastsnowy
- re-nan6

## 📄ライセンス
MIT