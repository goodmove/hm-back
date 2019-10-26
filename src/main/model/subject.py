class Subject:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @staticmethod
    def from_json(json_obj: dict):
        return Subject(json_obj['id'], json_obj['name'])
