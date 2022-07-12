from datetime import datetime
from uuid import UUID, uuid4
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, DateTime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1289@localhost:5432/Campaign_Planner'

db = SQLAlchemy()
migrate = Migrate(db)


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def set_attributes(self, values):
        for key, value in values.items():
            if hasattr(self, key) and isinstance(value, str) and value:
                setattr(self, key, value)


class Create(db.Model):
    __abstract__ = True

    created_on = Column(DateTime(timezone=True), default=datetime.utcnow)
    # created_by = Column(UUID(as_uuid=True))


class Update(db.Model):
    __abstract__ = True
    modified_on = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    # modified_by = Column(UUID(as_uuid=True))


class Review(db.Model):
    __abstract__ = True
    reviewed_on = Column(DateTime(timezone=True))
    # reviewed_by = Column(UUID(as_uuid=True))

if __name__=='__main__':
    app.run()