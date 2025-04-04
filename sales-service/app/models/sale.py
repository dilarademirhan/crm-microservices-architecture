from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.extensions import db
from .base import BaseModel

class Sale(BaseModel):
    __tablename__ = 'sales'

    customer_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(100), nullable=False)
    product = Column(String(100), nullable=False)
    amount = Column(String(50), nullable=False)

    stages = relationship('SaleStage', back_populates='sale', cascade="all, delete-orphan", lazy=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'customer_id': str(self.customer_id),
            'name': self.name,
            'stages': [stage.to_dict() for stage in self.stages] 
        }
