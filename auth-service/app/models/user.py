from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, UUID
import uuid
from app.extensions import db, pwd_context

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128))
    role = Column(String(20), nullable=False, default='user')  # admin, sales_rep, user
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def set_password(self, raw_password):
        self.password = pwd_context.hash(raw_password)
    
    def check_password(self, raw_password):
        try:
            return pwd_context.verify(raw_password, self.password)
        except Exception:
            return False
    
    
    def has_role(self, role):
        return self.role == role or self.role == 'admin'
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'role': self.role,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }