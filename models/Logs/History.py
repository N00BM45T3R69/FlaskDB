from datetime import datetime
from Flask import BaseModel, Create
from models.Database_Enums import Trigger
from sqlalchemy import Column, String, DateTime, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class History(BaseModel, Create):
    __tablename__ = 'History'
    id = Column(UUID(as_uuid=True), primary_key=True)
    campaign_id = Column(UUID(as_uuid=True), nullable=False)
    success = Column(Integer())
    failure = Column(Integer())
    remarks = Column(String(4096))
    trigger = Column(Enum(Trigger), nullable=False)
    created_on = Column(DateTime(), nullable=False, default=datetime.utcnow())