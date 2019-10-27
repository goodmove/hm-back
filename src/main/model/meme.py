class Meme:

    def __init__(self,
                id: str,
                subject_id: str,
                background_id: str,
                top_text: str,
                bottom_text: str,
                explanation: str,
                link: str,
                shown: int,
                answered_correctly: int,
                answered_incorrectly: int
        ):

        self.id = id
        self.subject_id = subject_id
        self.background_id = background_id
        self.top_text = top_text
        self.bottom_text = bottom_text
        self.explanation = explanation
        self.link = link
        self.shown = shown
        self.answered_correctly = answered_correctly
        self.answered_incorrectly = answered_incorrectly

    def to_json(self):
        return {
            'id': self.id,
            'subject_id': self.subject_id,
            'background_id': self.background_id,
            'top_text': self.top_text,
            'bottom_text': self.bottom_text,
            'explanantion': self.explanation,
            'link': self.link,
            'shown': self.shown,
            'answered_correctly': self.answered_correctly,
            'answered_incorrectly': self.answered_incorrectly 
        }

    @staticmethod
    def from_bson(bson_obj):
        return Meme(
            id=str(bson_obj['_id']),
            subject_id=bson_obj['subject_id'],
            background_id=bson_obj['background_id'],
            top_text=bson_obj['top_text'],
            bottom_text=bson_obj['bottom_text'],
            explanation=bson_obj['explanation'],
            link=bson_obj['link'],
            shown=bson_obj['shown'],
            answered_correctly=bson_obj['answered_correctly'],
            answered_incorrectly=bson_obj['answered_incorrectly']
        )

    @staticmethod
    def from_json(json_obj):
        return Meme(
            id=json_obj['id'],
            subject_id=json_obj['subject_id'],
            background_id=json_obj['background_id'],
            top_text=json_obj['top_text'],
            bottom_text=json_obj['bottom_text'],
            explanation=json_obj['explanation'],
            link=json_obj['link'],
            shown=json_obj['shown'],
            answered_correctly=json_obj['answered_correctly'],
            answered_incorrectly=json_obj['answered_incorrectly']
        )
