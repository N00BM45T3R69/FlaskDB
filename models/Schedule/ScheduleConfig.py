from datetime import datetime, date
from models.Database_Enums import Frequency
from models.Template.Template import Template
from models.Campaign.Campaign import Campaign
from sqlalchemy import Column, ForeignKey, String, DateTime, Enum, Date, Time
from sqlalchemy.dialects.postgresql import UUID
from Flask import BaseModel


class ScheduleConfig(BaseModel):
    __tablename__ = 'Schedule_config'
    id = Column(UUID(as_uuid=True), primary_key=True)
    campaign_id = Column(UUID(as_uuid=True), ForeignKey(Campaign.id), nullable=False)
    template_id = Column(UUID(as_uuid=True), ForeignKey(Template.id), nullable=False)
    frequency = Column(Enum(Frequency), nullable=False)
    start_date = Column(Date(), nullable=False, default=date.today())
    end_date = Column(Date(), nullable=False, default=date.today())
    trigger_time = Column(Time(), nullable=False, default=datetime.utcnow())
    created_by = Column(String(256), nullable=False)
    created_on = Column(DateTime(), nullable=False, default=datetime.utcnow())
    modified_by = Column(String(256), nullable=False)
    modified_on = Column(DateTime(), default=datetime.utcnow())
