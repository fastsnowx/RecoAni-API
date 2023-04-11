from pprint import pprint

import pandas as pd
import pymongo
from decouple import config
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

MONGODB_API_TOKEN = config("MONGODB_API_TOKEN")
ANNICT_API_TOKEN = config("ANNICT_API_TOKEN")
ANNICT_API_URL = "https://api.annict.com/graphql"

# connect MongoDB
client = pymongo.MongoClient(MONGODB_API_TOKEN)
db = client.reviews

# Select your transport with a defined url endpoint
headers = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {ANNICT_API_TOKEN}",
}
transport = AIOHTTPTransport(url=ANNICT_API_URL, headers=headers)

# Create a GraphQL client using the defined transport
gqlclient = Client(
    transport=transport, fetch_schema_from_transport=True, execute_timeout=300
)

# Provide a GraphQL query
query = gql(
    """
query {
  searchWorks(
    orderBy: {field: WATCHERS_COUNT, direction: DESC},
  ) {
    nodes {
      annictId
      title
      titleKana
      watchersCount
      reviewsCount
      reviews {
        nodes {
          id
          ratingOverallState
          ratingMusicState
          ratingStoryState
          ratingAnimationState
          ratingCharacterState
        }
      }
    }
  }
}
"""
)

# fetching data
print(f"fetching AnnictDB...")
result = gqlclient.execute(query)


# preprocessing
print(f"preprocessing dataframe...")
df = pd.json_normalize(
    result["searchWorks"]["nodes"],
    ["reviews", "nodes"],
    ["annictId", "title", "titleKana", "watchersCount", "reviewsCount"],
)

df = df.replace({"BAD": -1, "AVERAGE": 1, "GOOD": 2, "GREAT": 4})
df = df[df["reviewsCount"] > 0]

df_Overall = df[
    [
        "annictId",
        "id",
        "ratingOverallState",
        "title",
        "titleKana",
        "watchersCount",
        "reviewsCount",
    ]
]
df_Overall = df_Overall.dropna()
df_Music = df[
    [
        "annictId",
        "id",
        "ratingMusicState",
        "title",
        "titleKana",
        "watchersCount",
        "reviewsCount",
    ]
]
df_Music = df_Music.dropna()
df_Story = df[
    [
        "annictId",
        "id",
        "ratingStoryState",
        "title",
        "titleKana",
        "watchersCount",
        "reviewsCount",
    ]
]
df_Story = df_Story.dropna()
df_Animation = df[
    [
        "annictId",
        "id",
        "ratingAnimationState",
        "title",
        "titleKana",
        "watchersCount",
        "reviewsCount",
    ]
]
df_Animation = df_Animation.dropna()
df_Character = df[
    [
        "annictId",
        "id",
        "ratingCharacterState",
        "title",
        "titleKana",
        "watchersCount",
        "reviewsCount",
    ]
]
df_Character = df_Character.dropna()

collection_Overall = db.ratingOverallState
collection_Music = db.ratingMusicState
collection_Story = db.ratingStoryState
collection_Animation = db.ratingAnimationState
collection_Character = db.ratingCharacterState


def delete_and_insert_collections(collection, data):
    res = collection.delete_many({})
    ins = collection.insert_many(data.to_dict("records"))
    print(f"deleted records: {res.deleted_count}")
    print(f"inserted records: {len(ins.inserted_ids)}")


if __name__ == "__main__":
    print("start update collections🍗")
    delete_and_insert_collections(collection_Overall, df_Overall)
    delete_and_insert_collections(collection_Music, df_Music)
    delete_and_insert_collections(collection_Story, df_Story)
    delete_and_insert_collections(collection_Animation, df_Animation)
    delete_and_insert_collections(collection_Character, df_Character)
    print("successfully updated!🍩")
