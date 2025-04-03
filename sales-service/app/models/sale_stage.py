from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from sqlalchemy.orm import relationship

class SaleStage(BaseModel):
    __tablename__ = 'sale_stages'
    
    name = Column(String(50), nullable=False)
    notes = Column(String(255))
    sale_id = Column(UUID(as_uuid=True), ForeignKey('sales.id', ondelete="CASCADE"), nullable=False)

    sale = relationship('Sale', back_populates='stages')

    def to_dict(self):
        return {
            'id': str(self.id),
            'sale_id': str(self.sale_id),
            'name': self.name,
            'notes': self.notes,
            'created_at': self.created_at.isoformat()
        }