from datetime import datetime
from sqlalchemy import Column, ARRAY, ForeignKey, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID, JSON
import History
from models.Database_Enums import HistoryStatus
from Flask import BaseModel, Create


class HistoryDetails(BaseModel, Create):
    __tablename__ = 'History_detail'
    id = Column(UUID(as_uuid=True), primary_key=True)
    history_id = Column(UUID(as_uuid=True), ForeignKey(History.id), nullable=False)
    recipient = Column(JSON(), nullable=False)
    cc = Column(ARRAY(String(50)), nullable=True)
    attachments = Column(ARRAY(String(50)), nullable=True)
    remarks = Column(String(4096), nullable=True)
    status = Column(Enum(HistoryStatus), nullable=False)
    created_on = Column(DateTime(), nullable=False, default=datetime.utcnow())
