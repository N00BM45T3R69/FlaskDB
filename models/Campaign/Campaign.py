from datetime import datetime
from sqlalchemy import Column, Boolean, String, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from Flask import BaseModel, Create


class Campaign(BaseModel,Create):
    __tablename__ = "Campaign"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(225), nullable=False, unique=True)
    idx_name = Index('name', unique=True)
    description = Column(String(512), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_approved = Column(Boolean(), default=False)
    created_by = Column(String(256))
    created_on = Column(DateTime(), default=datetime.utcnow())
    modified_by = Column(String(256), nullable=False)
    modified_on = Column(DateTime(), default=datetime.utcnow())