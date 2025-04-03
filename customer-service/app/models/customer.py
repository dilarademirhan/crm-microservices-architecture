from datetime import datetime
from mongoengine import (
    StringField, EmailField, ListField, DictField, 
    ReferenceField, signals
)
from .base import BaseModel
from .note import Note

class Customer(BaseModel):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    phone = StringField(required=True)
    company = StringField()
    address = StringField()
    notes = ListField(ReferenceField(Note, reverse_delete_rule=2))  # lazy_load=False kaldırıldı
    tags = ListField(StringField())
    metadata = DictField()
    
    meta = {
        'collection': 'customers',
        'indexes': ['company', 'created_at']
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'company': self.company,
            'address': self.address,
            'notes': [note.to_dict() for note in Note.objects(id__in=[n.id for n in self.notes])],  # Daha güvenli erişim
            'tags': self.tags,
            'metadata': self.metadata,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'created_by': self.created_by
        }
    
    def add_note(self, content, created_by):
        note = Note(content=content, created_by=created_by)
        note.save()
        self.notes.append(note)
        self.save()
        return note
    
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.utcnow()

signals.pre_save.connect(Customer.pre_save, sender=Customer)
signals.pre_save.connect(Customer.pre_save, sender=Note)
