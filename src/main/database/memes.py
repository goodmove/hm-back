from typing import Optional, List

from bson.objectid import ObjectId

from src.main.database.common import DB
from src.main.model.meme import Meme


def find_one_meme(id: str) -> Optional[dict]:
    return DB.memes.find_one({'_id': ObjectId(id)})


def find_subject_memes(subject_id: str) -> List[Meme]:
    return list([Meme.from_bson(b) for b in DB.memes.find({'subject_id': ObjectId(subject_id)})])


def find_all_memes() -> List[Meme]:
    return list([Meme.from_bson(b) for b in DB.memes.find()])


def insert_meme(url: str,
                subject_id: str,
                explanation: str,
                shown: int = 0,
                answered_correctly: int = 0,
                answered_incorrectly: int = 0
    ) -> Meme:

    res = DB.memes.insert_one({'url': url,
                                'subject_id': subject_id,
                                'explanation': explanation,
                                'shown': shown,
                                'answered_correctly': answered_correctly,
                                'answered_incorrectly':  answered_incorrectly
            })

    return Meme(str(res.inserted_id),
            url,
            subject_id,
            explanation,
            shown,
            answered_correctly,
            answered_incorrectly
    )


def update_meme(id: str, patch_object: dict) -> Meme:
    res = DB.memes.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': patch_object},
        return_document=ReturnDocument.AFTER
    )
