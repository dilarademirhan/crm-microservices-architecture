from datetime import datetime
from mongoengine import StringField, DateTimeField, signals
from .base import BaseModel

class Note(BaseModel):
    content = StringField(required=True)

    meta = {
        'collection': 'notes',
        'indexes': ['created_at', ]
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'created_by': self.created_by
        }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.utcnow()

signals.pre_save.connect(Note.pre_save, sender=Note)
