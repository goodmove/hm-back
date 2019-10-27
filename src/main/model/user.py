from copy import deepcopy
from typing import List


class User:

    def __init__(self,
                 id: str,
                 first_name: str,
                 last_name: str,
                 location: str,
                 age: int,
                 interests: List[str],
                 school: str,
                 memes_shown: int,
                 correct_answers: int,
                 incorrect_answers: int
                 ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.interests = interests
        self.school = school,
        self.memes_shown = memes_shown,
        self.correct_answers = correct_answers,
        self.incorrect_answers = incorrect_answers

    @staticmethod
    def from_json(json_obj: dict):
        return User(
            id=json_obj['id'],
            first_name=json_obj['first_name'],
            last_name=json_obj['last_name'],
            location=json_obj.get('location'),
            age=json_obj.get('age'),
            interests=json_obj.get('interests'),
            school=json_obj.get('school'),
            memes_shown=json_obj.get('memes_shown'),
            correct_answers=json_obj.get('correct_answers'),
            incorrect_answers=json_obj.get('incorrect_answers')
        )

    @staticmethod
    def from_bson(bson_obj):
        copied = deepcopy(bson_obj)
        copied['id'] = str(copied['_id'])
        return User.from_json(copied)

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'location': self.location,
            'age': self.age,
            'interests': self.interests,
            'school': self.school,
            'memes_shown': self.memes_shown,
            'correct_answers': self.correct_answers,
            'incorrect_answers': self.incorrect_answers,

        }
