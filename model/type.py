from sqlalchemy import Column, String, Integer
from model import Base

class Type(Base):
    __tablename__ = 'type'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __init__(self, name:str = None):
        """
        Create a Type model
        Arguments:
            name: the name of the item type
        """
        self.name = name