from datetime import datetime
from Flask import BaseModel, Update, Create
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from models.Template.Template import Template


class Attachment(BaseModel, Create, Update):
    __tablename__ = 'Attachment'

    id = Column(UUID(as_uuid=True), primary_key=True)
    template_id = Column(UUID(as_uuid=True), ForeignKey(Template.id), nullable=False)
    url = Column(String(102), nullable=False)
    pattern = Column(String(512), nullable=False)
    created_by = Column(String(256), nullable=False)
    created_on = Column(DateTime(), default=datetime.utcnow())
    modified_by = Column(String(256), nullable=False)
    modified_on = Column(DateTime(), default=datetime.utcnow())

