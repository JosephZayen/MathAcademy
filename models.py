from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped, Session


# Base model and user class

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ =  "user"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    pwd_hash: Mapped[str]
    custom_id: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]

# modules

class Event(Base):
    __tablename__ = "event"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    timestamp: Mapped[int]
    description: Mapped[str]
    local_date: Mapped[str]
    
"""
# for storing files stuff
class WorkSpace(Base):   
    pass

class SM2(Base):
    pass

class RegSM2(Base):
    pass

class ErrorSM2(Base):
    pass
"""

engine = create_engine("sqlite:///instance.sqlite")
Base.metadata.create_all(engine)
db_session = Session(engine)