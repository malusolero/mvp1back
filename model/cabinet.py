
from sqlalchemy import Column, String, Integer
from model import Base
from sqlalchemy.orm import relationship

class Cabinet(Base):
    __tablename__ = 'cabinet'

    id = Column(Integer, primary_key=True)
    position = Column(String(50), unique=True, nullable=False)


    def __init__(self, position:str = None):
        """
        Create a Cabinet model
        Arguments:
            position: where the cabinet is placed vertically
        """
        self.position = position
