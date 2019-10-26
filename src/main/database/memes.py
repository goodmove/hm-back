from typing import Optional, List

from bson.objectid import ObjectId

from src.main.database.common import DB
from src.main.model.meme import Meme


def find_one_meme(id: str) -> Optional[dict]:
    return DB.memes.find_one({'_id': ObjectId(id)})


def get_all_memes() -> List[Meme]:
    return list([Meme.from_bson(b) for b in DB.memes.find()])


def insert_meme(bg_id: str, text: str, subject_id: str) -> Meme:
    res = DB.memes.insert_one({'background_id': bg_id, 'text': text, 'subject_id': subject_id})
    return Meme(str(res.inserted_id), bg_id, text, subject_id)
