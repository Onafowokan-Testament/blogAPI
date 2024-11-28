import os

import dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

dotenv.load_dotenv()


client = MongoClient(os.getenv("MONGO_URL"), server_api=ServerApi("1"))
""

db = client.blogging
blog_collections = db["blogs"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
except Exception as e:
    print(e)
