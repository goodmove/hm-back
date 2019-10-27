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


def insert_meme(bg_id: str,
                subject_id: str,
                top_text: str,
                bottom_text: str,
                explanation: str,
                link: str,
                shown: int,
                answered_correctly: int,
                answered_incorrectly: int
    ) -> Meme:

    res = DB.memes.insert_one({'background_id': bg_id,
                                'subject_id': subject_id,
                                'top_text': top_text,
                                'bottom_text': bottom_text,
                                'explanation': explanation,
                                'link': link,
                                'shown': shown,
                                'answered_correctly': answered_correctly,
                                'answered_incorrectly':  answered_incorrectly
            })

    return Meme(str(res.inserted_id),
            bg_id,
            subject_id,
            top_text,
            bottom_text,
            explanation,
            link,
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
