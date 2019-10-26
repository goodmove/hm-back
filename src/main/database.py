from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import Optional, List

from src.main.model.subject import Subject

__db_name = "hackm"
__uri = "mongodb+srv://admin:admin@mflix-tbs6k.mongodb.net/{}?retryWrites=true&w=majority".format(__db_name)

__client = MongoClient(__uri)
__db = __client[__db_name]


def find_one_subject(subject_id) -> Optional[dict]:
    return __db.subjects.find_one({'_id': ObjectId(subject_id)})


def get_all_subjects() -> List[dict]:
    return list(__db.subjects.find())


def insert_subject(subject_name: str) -> Subject:
    res = __db.subjects.insert_one({'name': subject_name})
    return Subject(str(res.inserted_id), subject_name)
