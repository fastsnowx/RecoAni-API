
from decouple import config
import pandas as pd
import pymongo
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

MONGODB_API_KEY = config("MONGODB_API_KEY")
ANNICT_API_KEY = config("ANNICT_API_KEY")
ANNICT_API_URL = "https://api.annict.com/graphql"

# Select your transport with a defined url endpoint
headers = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {ANNICT_API_KEY}"
    }
transport = AIOHTTPTransport(url=ANNICT_API_URL, headers=headers)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True, execute_timeout=300)

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

# retirive data from AnnictAPI
result = client.execute(query)

# connect to MongoDB
client = pymongo.MongoClient(MONGODB_API_KEY)
db = client.raw_data
collection_reviews = db.reviews

# raw data shaping & insert DB
df = pd.json_normalize(result["searchWorks"]["nodes"], ["reviews", "nodes"], ["annictId", "title", "titleKana", "watchersCount", "reviewsCount"])
collection_reviews.insert_many(df.to_dict("records"))
