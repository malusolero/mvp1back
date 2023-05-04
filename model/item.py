from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base, Type

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    brand = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)
    expiry_date = Column(String(100), nullable=False)
    weight = Column(String(50), nullable=False)
    cabinet_id = Column(Integer, ForeignKey("cabinet.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("type.id"), nullable=False)

    type = relationship("Type")

    def __init__(self, name:str, brand:str, amount:int, expiry_date:DateTime, weight:str, cabinet_id:int, type_id:int = None):

        """
        Create a Item model
        Arguments:
            name: item name.
            brand: item brand
            amount: quantity of items in this cabinet
            expiry_date: item expiration date
            weight: item weight (just how it's described in the package)
            cabinet_id: foreign key - cabinet.id
            type_id: foreign key - type.id
        """

        self.name = name
        self.brand = brand
        self.amount = amount
        self.expiry_date = expiry_date
        self.weight = weight
        self.type_id = type_id
        self.cabinet_id = cabinet_id

