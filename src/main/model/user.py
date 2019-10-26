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
                 school: str
                 ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.interests = interests
        self.school = school

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
        }
