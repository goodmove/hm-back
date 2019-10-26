from typing import Optional, List

from bson.objectid import ObjectId

from src.main.database.common import DB
from src.main.model.subject import Subject


def find_one_subject(subject_id) -> Optional[dict]:
    return DB.subjects.find_one({'_id': ObjectId(subject_id)})


def get_all_subjects() -> List[dict]:
    return list(DB.subjects.find())


def insert_subject(subject_name: str) -> Subject:
    res = DB.subjects.insert_one({'name': subject_name})
    return Subject(str(res.inserted_id), subject_name)
