from pymongo import MongoClient
from typing import Optional

__db_name = "hackm"
__uri = "mongodb+srv://admin:admin@mflix-tbs6k.mongodb.net/{}?retryWrites=true&w=majority".format(__db_name)

__client = MongoClient(__uri)
__db = __client[__db_name]


def find_one_subject(subject_id) -> Optional[dict]:
    return __db.subjects.find_one({'id': subject_id})
