class Answer:

    def __init__(self,
                id: str,
                meme_id: str,
                user_id: str,
                subject_id: str,
                result: str,
                feedback: str
        ):

        self.id = id
        self.meme_id = meme_id
        self.user_id = user_id
        self.subject_id = subject_id
        self.result = result
        self.feedback = feedback

    def to_json(self):
        return {
            'id': self.id,
            'meme_id': self.meme_id,
            'user_id': self.user_id,
            'subject_id': self.subject_id,
            'result': self.result,
            'feedback': self.feedback
        }

    @staticmethod
    def from_bson(bson_obj):
        return Answer(
            id=str(bson_obj['_id']),
            meme_id=bson_obj['meme_id'],
            user_id=bson_obj['user_id'],
            subject_id=bson_obj['subject_id'],
            result=bson_obj['result'],
            feedback=bson_obj['feedback']
        )

    @staticmethod
    def from_json(json_obj):
        return Answer(
            id=str(json_obj['id']),
            meme_id=json_obj['meme_id'],
            user_id=json_obj['user_id'],
            subject_id=json_obj['subject_id'],
            result=json_obj['result'],
            feedback=json_obj['feedback']
        )
