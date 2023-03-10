# RecoAni-API
<p>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
    </a>
</p>

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
ANNICT_API_TOKEN :Annictのtoken
MONGODB_API_TOKEN : MongoDBのtoken
MAL_API_TOKEN : MyAnimeListのtoken
REDIS_UPSTASH_TOKEN : Upstash(redis)のtoken
```
## 🚀実行
`.env`を定義した上で
- MongoDB, Upstashの設定
- `poetry install` ※poetry required.
- `python updateDatabase.py`
- `uvicorn main:app --reload`

## 👥 contributors
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/re-nan6"><img src="https://avatars.githubusercontent.com/u/67001442?v=4" width="100px;" alt="re-nan6"/><br /><sub><b>re-nan6</b></sub></a><br /><a href="https://github.com/re-nan6/RecoAni/commits?author=re-nan6" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/fastsnowy"><img src="https://avatars.githubusercontent.com/u/61731151?v=4" width="100px;" alt="fastsnowy"/><br /><sub><b>fastsnowy</b></sub></a><br /><a href="https://github.com/re-nan6/RecoAni/commits?author=fastsnowy" title="Code">💻</a></td>
    </tr>
   </tbody>
</table>

## 📄ライセンス
[MIT](LICENSE)
