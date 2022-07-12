from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from Flask import BaseModel, Create
from models.Database_Enums import Status
from models.Schedule import ScheduleConfig


class Schedule(BaseModel, Create):
    __tablename__ = 'Schedule'
    id = Column(UUID(as_uuid=True), primary_key=True)
    config_id = Column(UUID(as_uuid=True), ForeignKey(ScheduleConfig.id), nullable=False)
    trigger_time = Column(DateTime(), nullable=False, default=datetime.utcnow())
    status = Column(Enum(Status), nullable=False)
    created_on = Column(DateTime(), nullable=False, default=datetime.utcnow())
    modified_by = Column(String(256), nullable=False)
