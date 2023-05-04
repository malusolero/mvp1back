from typing import List
from pydantic import BaseModel, Field


class CabinetPathSchema(BaseModel):
    cabinet_id: int = Field(description="Cabinet id")

class CabinetSchema(BaseModel):
    """ Describes the arguments needed for creating a cabinet
    """
    position: str = "Upper Cabinet"

class CabinetViewSchema(BaseModel):
    """ Default response of view cabinet
    """

    id: int = 1
    position: str = "Upper Cabinet"

class ListCabinetsSchema(BaseModel):
    """ Describes the arguments needed for returning a list if cabinets
    """

    cabinets: List[CabinetViewSchema]

def return_cabinets(cabinets: List[CabinetViewSchema]):
    """ Method that specifies the return of a list of cabinets
    """

    result = []
    for cabinet in cabinets:
        result.append({
            "id": cabinet.id,
            "position": cabinet.position
        })

    return { "cabinets": result}