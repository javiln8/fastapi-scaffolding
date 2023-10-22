from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    tax: Optional[float] = None


class ItemInDB(Item):
    id: str
