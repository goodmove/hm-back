from typing import Optional, List

from bson.objectid import ObjectId
from pymongo import ReturnDocument

from src.main.database.common import DB
from src.main.model.user import User


def find_one_user(user_id) -> Optional[dict]:
    return DB.users.find_one({'_id': ObjectId(user_id)})


def find_all_users() -> List[User]:
    return list([User.from_bson(b) for b in DB.users.find()])


def insert_user(first_name: str,
                last_name: str,
                location: str,
                age: int,
                interests: List[str],
                school: Optional[str],
                memes_shown: int,
                correct_answers: int,
                incorrect_answers: int
                ) -> User:
    res = DB.users.insert_one({
        'first_name': first_name,
        'last_name': last_name,
        'location': location,
        'age': age,
        'interests': interests,
        'school': school,
        'memes_shown': memes_shown,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers
    })

    return User(str(res.inserted_id),
                first_name,
                last_name,
                location,
                age,
                interests,
                school,
                memes_shown,
                correct_answers,
                incorrect_answers)


def update_user(id: str, patch_object: dict) -> User:
    res = DB.users.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': patch_object},
        return_document=ReturnDocument.AFTER
    )
    return User.from_bson(res)
