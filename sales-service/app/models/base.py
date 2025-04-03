import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, UUID
from app.extensions import db

class BaseModel(db.Model):
    __abstract__ = True 
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # created_by = Column(UUID(as_uuid=True), nullable=False)