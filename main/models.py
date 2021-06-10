from sqlalchemy import Column, Integer, String,TIMESTAMP
import datetime
from database import Base

class todo_model(Base):
    __tablename__ = "todo1"
    
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )
    
    title = Column(
        String
    )
    
    discription = Column(
        String
    )
    
    status = (
        Integer,
    )
    
    created_at = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow
    )
    
    updated_at = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow

    )
