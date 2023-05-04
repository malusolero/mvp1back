from typing import List, Optional
from pydantic import BaseModel, Field

from schemas.type import TypeSchema

class ItemSearchSchema(BaseModel):
    """ Item will be searched by name
    """
    name: str = "Leite"

class ItemSchema(BaseModel):
    """ Arguments needed for creating an Item
    """

    name: str = 'Leite Integral'
    brand: str = 'Nestlé'
    amount: int = 5
    weight: str = '1L'
    expiry_date: str = "2023-05-03T23:15:24.588Z"
    type_id: int = 2
    cabinet_id: int = 1

class ItemViewSchema(BaseModel):
    """ An item should return the item props and the assosciated type
    """

    name: str = 'Leite Integral'
    brand: str = 'Nestlé'
    amount: int = 5
    weight: str = '1L'
    expiry_date: str = "2023-05-03T23:15:24.588Z"
    type: TypeSchema
    cabinet_id: int = 1

class ListItemSchema(BaseModel):
    """ Defines how the list of items should be returned
    """

    items: List[ItemViewSchema]

class ItemQuery(BaseModel):
    cabinet_id: Optional[int] = Field(description='Id from cabinet.id', example=2)


def return_item(item: ItemViewSchema):
    """ Definition of return item method structure
    """

    return {
        "name": item.name,
        "brand": item.brand,
        "amount": item.amount,
        "weight": item.weight,
        "expiry_date": item.expiry_date,
        "type": {
            "name": item.type.name if not item.type is None else None
        },
        "cabinet_id": item.cabinet_id
    }


def return_items(items: List[ItemViewSchema]):
    """ Definition of return list item method structure
    """
    print(len(items))
    result = []
    for item in items:
        result.append(return_item(item))

    return { "items" : result }