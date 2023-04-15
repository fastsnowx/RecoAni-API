import implicit
from pymongo import MongoClient
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix
from decouple import config

MONGODB_API_TOKEN = config("MONGODB_API_TOKEN")
client = MongoClient(MONGODB_API_TOKEN)

db = client.reviews


class Recommendation:
    def __init__(self, ratingState: str) -> None:
        def retrieve_and_preprocess(ratingState):
            if ratingState == "ratingOverallState":
                collection = db.ratingOverallState
            elif ratingState == "ratingStoryState":
                collection = db.ratingStoryState
            elif ratingState == "ratingMusicState":
                collection = db.ratingMusicState
            elif ratingState == "ratingCharacterState":
                collection = db.ratingCharacterState
            elif ratingState == "ratingAnimationState":
                collection = db.ratingAnimationState
            else:
                raise AssertionError

            reviews = list(collection.find())
            user_id_set = set()
            annict_id_set = set()
            for review in reviews:
                user_id_set.add(review['id'])
                annict_id_set.add(review['annictId'])

            user_id_list = sorted(list(user_id_set))
            annict_id_list = sorted(list(annict_id_set))

            row, col, data = [], [], []
            for review in reviews:
                row.append(user_id_list.index(review['id']))
                col.append(annict_id_list.index(review['annictId']))
                data.append(review[ratingState])

            reviewData = csr_matrix((data, (row, col)), shape=(len(user_id_list), len(annict_id_list)))

            columns_size = len(annict_id_list)
            return annict_id_list, reviewData, columns_size

        def train(data):
            print("training models ...")
            model = implicit.als.AlternatingLeastSquares(factors=200, iterations=10)
            model.fit(data, show_progress=True)
            print("training ended.")
            return model

        self.annictIdList, reviewData, self.columns_size = retrieve_and_preprocess(
            ratingState
        )
        self.model = train(reviewData)

    def recommend_animes(self, annictIds):
        user_like = lil_matrix((1, self.columns_size))
        for i in annictIds:
            if i in self.annictIdList:
                user_like[(0, self.annictIdList.index(i))] = 2.0

        recommend_index, recommend_scores = self.model.recommend(
            0,
            user_like.tocsr(),
            N=10,
            recalculate_user=True,
        )

        recommend_ids = [self.annictIdList[i] for i in recommend_index]
        return recommend_ids, recommend_scores
