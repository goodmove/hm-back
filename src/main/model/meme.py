class Meme:

    def __init__(self,
                id: str,
                url: str,
                subject_id: str,
                explanation: str,
                shown: int,
                answered_correctly: int,
                answered_incorrectly: int
        ):

        self.id = id
        self.url = url
        self.subject_id = subject_id
        self.explanation = explanation
        self.shown = shown
        self.answered_correctly = answered_correctly
        self.answered_incorrectly = answered_incorrectly

    def to_json(self):
        return {
            'id': self.id,
            'url': self.url,
            'subject_id': self.subject_id,
            'explanation': self.explanation,
            'shown': self.shown,
            'answered_correctly': self.answered_correctly,
            'answered_incorrectly': self.answered_incorrectly 
        }

    @staticmethod
    def from_bson(bson_obj):
        return Meme(
            id=str(bson_obj['_id']),
            subject_id=bson_obj['subject_id'],
            url=bson_obj['url'],
            explanation=bson_obj['explanation'],
            shown=bson_obj['shown'],
            answered_correctly=bson_obj['answered_correctly'],
            answered_incorrectly=bson_obj['answered_incorrectly']
        )

    @staticmethod
    def from_json(json_obj):
        return Meme(
            id=json_obj['id'],
            subject_id=json_obj['subject_id'],
            url=json_obj['url'],
            explanation=json_obj['explanation'],
            shown=json_obj['shown'],
            answered_correctly=json_obj['answered_correctly'],
            answered_incorrectly=json_obj['answered_incorrectly']
        )
