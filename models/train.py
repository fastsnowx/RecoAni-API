# %%
import implicit
import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import implicit
from scipy.sparse import lil_matrix,coo_matrix
from decouple import config

def retrieve_and_preprocess():
    # data持ってくるところ別のファイルでやりたい
    MONGODB_API_KEY = config("MONGODB_API_KEY")
    client = MongoClient(MONGODB_API_KEY)

    db = client.reviews
    collection_Overall = db.ratingOverallState

    # 前処理を別でやる？
    df = pd.DataFrame(list(collection_Overall.find()))

    df_pivot = df.pivot_table(index="id",columns="annictId",values="ratingOverallState").fillna(0)
    annictIdList = list(df_pivot.columns.values)
    reviewData = df_pivot.values
    reviewData = csr_matrix(reviewData)
    return annictIdList, reviewData

def train(data):
    model = implicit.als.AlternatingLeastSquares(factors=200, iterations=10)
    model.fit(data, show_progress=True)
    return model

def recommend_animes(annictIds: list, models, annictIdList, df_pivot) -> list:
    user_like = lil_matrix((1, len(df_pivot.columns)))
    for i in annictIds:
        if i in annictIdList:
            user_like[(0, annictIdList.index(i))] = 2.0
    recommend_index, reccomend_scores = models.recommend(
    0,
    user_like.tocsr(),
    N=10,
    recalculate_user=True,
    )
    reccomend_ids = [annictIdList[i] for i in recommend_index]
    return reccomend_ids, reccomend_scores

