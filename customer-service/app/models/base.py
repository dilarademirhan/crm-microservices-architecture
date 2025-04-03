from datetime import datetime
import uuid
from mongoengine import Document, DateTimeField, StringField, signals

class BaseModel(Document):
    id = StringField(default=lambda: str(uuid.uuid4()), primary_key=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    created_by = StringField(required=True)

    meta = {'abstract': True} 

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow() 
        return super().save(*args, **kwargs)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.utcnow()

signals.pre_save.connect(BaseModel.pre_save, sender=BaseModel) 