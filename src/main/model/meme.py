class Meme:

    def __init__(self, id: str, background_id: str, text: str, subject_id: str):
        self.id = id
        self.background_id = background_id
        self.text = text
        self.subject_id = subject_id

    def to_json(self):
        return {
            'id': self.id,
            'background_id': self.background_id,
            'text': self.text,
            'subject_id': self.subject_id
        }

    @staticmethod
    def from_bson(bson_obj):
        return Meme(
            id=str(bson_obj['_id']),
            background_id=bson_obj['background_id'],
            text=bson_obj['text'],
            subject_id=bson_obj['subject_id']
        )

    @staticmethod
    def from_json(json_obj):
        return Meme(
            id=json_obj['id'],
            background_id=json_obj['background_id'],
            text=json_obj['text'],
            subject_id=json_obj['subject_id']
        )
