# %%
import implicit
from pymongo import MongoClient
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix
from decouple import config

MONGODB_API_KEY = config("MONGODB_API_KEY")
client = MongoClient(MONGODB_API_KEY)

db = client.reviews
collection_Overall = db.ratingOverallState
class Recommendation():
    def __init__(self) -> None:
        
        def retrieve_and_preprocess():

            df = pd.DataFrame(list(collection_Overall.find()))
            df_pivot = df.pivot_table(index="id",columns="annictId",values="ratingOverallState").fillna(0)
            annictIdList = list(df_pivot.columns.values)
            reviewData = df_pivot.values
            reviewData = csr_matrix(reviewData)

            return annictIdList, reviewData, df_pivot

        def train(data):
            model = implicit.als.AlternatingLeastSquares(factors=200, iterations=10)
            model.fit(data, show_progress=True)
            return model

        self.annictIdList, self.reviewData, self.df_pivot = retrieve_and_preprocess()
        self.model = train(self.reviewData)

    
    def recommend_animes(self, annictIds):
        user_like = lil_matrix((1, len(self.df_pivot.columns)))
        for i in annictIds:
            if i in self.annictIdList:
                user_like[(0, self.annictIdList.index(i))] = 2.0

        recommend_index, reccomend_scores = self.model.recommend(
            0,
            user_like.tocsr(),
            N=10,
            recalculate_user=True,
            )

        reccomend_ids = [self.annictIdList[i] for i in recommend_index]
        return reccomend_ids, reccomend_scores