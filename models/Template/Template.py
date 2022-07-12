from datetime import datetime
from sqlalchemy import Column, ARRAY, Boolean, ForeignKey, String, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from Flask import BaseModel, Update, Create
from models.Campaign.Campaign import Campaign


class Template(BaseModel, Create, Update):
    __tablename__ = 'Template'
    id = Column(UUID(as_uuid=True), primary_key=True)
    campaign_id = Column(UUID(as_uuid=True), ForeignKey(Campaign.id), nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    idx_name = Index('name', unique=True)
    email_template = Column(String(8195), nullable=False)
    recipients = Column(ARRAY(String(50)), nullable=False)
    cc = Column(ARRAY(String(50)))
    send_as_group = Column(Boolean(), nullable=False, default=False)
    mark_rm = Column(Boolean(), nullable=False, default=False)
    mark_pm = Column(Boolean(), nullable=False, default=False)
    created_by = Column(String(256), nullable=False)
    created_on = Column(DateTime(), nullable=False, default=datetime.utcnow())
    modified_by = Column(String(256), nullable=False)
    modified_on = Column(DateTime(), default=datetime.utcnow())
