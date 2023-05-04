from typing import List
from pydantic import BaseModel, Field

class TypePathSchema(BaseModel):
    type_id: int = Field(description="Type id")

class TypeSchema(BaseModel):
    """ Describes the arguments needed for creating a type
    """

    name: str = "Diary"

class TypeViewSchema(BaseModel):
    """ Describes how the type is returned when viewing one type
    """

    id: int = 1
    type: str = "Diary"


class ListTypesSchema(BaseModel):
    """ Describes how the list of type should be returned
    """

    types:List[TypeViewSchema]

def return_types(types: ListTypesSchema):
    """ Function for returning an object contaning a list of types
    """

    result = []
    for type in types:
        result.append({
            "id": type.id,
            "name": type.name
        })

    return { "types": result}