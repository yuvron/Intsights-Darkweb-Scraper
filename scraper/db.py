import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient()
client = MongoClient(os.getenv("DATABASE_URL"))

db = client.darknet
pastes = db.pastes


# Inserts a paste to the pastes collection
def insert_paste(title: str, content: str, author: str, date: datetime, tags: list[str]):
    paste = {"title": title, "content": content, "author": author, "date": date, "tags": tags}
    pastes.insert_one(paste)


# Finds a paste document by content
def find_paste_by_content(content: str):
    query = {"content": content}
    result = pastes.find_one(query)
    return result
