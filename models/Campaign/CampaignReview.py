from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from Flask import BaseModel, Update, Create, Review
from models.Campaign.Campaign import Campaign
from models.Database_Enums import ReviewStatus


class CampaignReview(BaseModel, Update, Create, Review):
    __tablename__ = 'Campaign_review'
    id = Column(UUID(as_uuid=True), primary_key=True)
    campaign_id = Column(UUID(as_uuid=True), ForeignKey(Campaign.id), nullable=False)
    reviewed_by = Column(String(256))
    reviewed_on = Column(DateTime(), default=datetime.utcnow())
    status = Column(Enum(ReviewStatus), nullable=False)
    comment = Column(String(102))
    created_by = Column(String(256), nullable=False)
    created_on = Column(DateTime(), nullable=False, default=datetime.utcnow())
    modified_by = Column(String(256), nullable=False)
    modified_on = Column(DateTime(), default=datetime.utcnow())
