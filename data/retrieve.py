# %%
import collections
from decouple import config
import pymongo
import pandas as pd


MONGODB_API_KEY = config("MONGODB_API_KEY")

# %%
client = pymongo.MongoClient(MONGODB_API_KEY)
db = client.reviews
collection_ratingOverall = db.ratingOverallState


# %%
df = pd.DataFrame(list(collection_ratingOverall.find()))
# %%
df.head()
# %%
