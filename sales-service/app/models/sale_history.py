# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Integer, String, ForeignKey, Column, DateTime, Text
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship, backref
# from .base import db

# class SaleHistory(db.Model, db.BaseModel):
#     __tablename__ = 'sale_histories'

#     sale_id = Column(UUID(as_uuid=True), ForeignKey('sales.id'), nullable=False)
#     old_stage_id = Column(Integer, ForeignKey('sale_stages.id'))
#     new_stage_id = Column(Integer, ForeignKey('sale_stages.id'), nullable=False)
#     notes = Column(Text, nullable=True)
#     changed_at = Column(DateTime, default=datetime.utcnow)
#     changed_by = Column(String(100), nullable=False)

#     sale = relationship('Sale', backref=backref('history', lazy=True))
#     old_stage = relationship('SaleStage', foreign_keys=[old_stage_id])
#     new_stage = relationship('SaleStage', foreign_keys=[new_stage_id])

#     def to_dict(self):
#         return {
#             'id': str(self.id),
#             'sale_id': str(self.sale_id),
#             'old_stage_id': self.old_stage_id,
#             'new_stage_id': self.new_stage_id,
#             'old_stage_name': self.old_stage.name if self.old_stage else None,
#             'new_stage_name': self.new_stage.name if self.new_stage else None,
#             'notes': self.notes,
#             'changed_at': self.changed_at.isoformat(),
#             'changed_by': self.changed_by
#         }
