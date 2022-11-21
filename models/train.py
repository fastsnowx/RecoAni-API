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
            print("fetching")
            df = pd.DataFrame(list(collection_Overall.find()))
            print("comp")
            user_id_categorical = pd.api.types.CategoricalDtype(categories=sorted(df.id.unique()), ordered=True)
            annictId_categorical = pd.api.types.CategoricalDtype(categories=sorted(df.annictId.unique()), ordered=True)
            row = df.id.astype(user_id_categorical).cat.codes
            col = df.annictId.astype(annictId_categorical).cat.codes
            annictIdList = list(sorted(df.annictId.unique()))
            reviewData = csr_matrix(
                                (df["ratingOverallState"],
                                (row, col)),
                                shape=(user_id_categorical.categories.size, annictId_categorical.categories.size))
            columns_size = len(annictIdList)
            print("pleted")
            return annictIdList, reviewData, columns_size

        def train(data):
            model = implicit.als.AlternatingLeastSquares(factors=200, iterations=10)
            model.fit(data, show_progress=True)
            return model

        self.annictIdList, reviewData, self.columns_size = retrieve_and_preprocess()
        self.model = train(reviewData)

    
    def recommend_animes(self, annictIds):
        user_like = lil_matrix((1, self.columns_size))
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