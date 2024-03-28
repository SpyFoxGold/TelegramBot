from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class User(Base):
    __tablename__ = "my_database"
    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String(50), index=True)
    request: str = Column(String(50), unique=True, index=True)