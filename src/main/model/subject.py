class Subject:

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    @staticmethod
    def from_json(json_obj: dict):
        return Subject(json_obj['id'], json_obj['name'])

    @staticmethod
    def from_bson(bson_obj):
        return Subject(str(bson_obj['_id']), bson_obj['name'])

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
