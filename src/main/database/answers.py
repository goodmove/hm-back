from typing import Optional, List

from bson.objectid import ObjectId

from src.main.database.common import DB
from src.main.model.answer import Answer


def find_one_answer(id: str) -> Optional[dict]:
    return DB.answers.find_one({'_id': ObjectId(id)})

def find_meme_answers(meme_id: str) -> List[Answer]:
    return list([Answer.from_bson(b) for b in DB.answers.find({'meme_id': ObjectId(meme_id)})])

def find_user_answers(user_id: str) -> List[Answer]:
    return list([Answer.from_bson(b) for b in DB.answers.find({'user_id': ObjectId(user_id)})])

def find_all_answers() -> List[Answer]:
    return list([Answer.from_bson(b) for b in DB.answers.find()])

def insert_answer(meme_id: str, user_id: str, subject_id: str, result: str, feedback: str) -> Answer:

    res = DB.answers.insert_one({'meme_id': meme_id,
                                'user_id': user_id,
                                'subject_id': subject_id,
                                'result': result,
                                'feedback': feedback
                                })
    return Answer(str(res.inserted_id), meme_id, user_id, subject_id, result, feedback)
