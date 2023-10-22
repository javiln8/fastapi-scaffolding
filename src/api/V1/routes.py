from fastapi import APIRouter, HTTPException
from uuid import uuid4
from src.api.V1.models import Item, ItemInDB
from src.infrastructure.dynamo import repository

router = APIRouter()


@router.post("/items/", response_model=ItemInDB)
async def create_item_endpoint(item: Item):
    item_data = item.dict()
    if 'id' not in item_data or not item_data['id']:
        item_data['id'] = str(uuid4())

    response = repository.create_item(ItemInDB(**item_data))
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise HTTPException(status_code=500, detail="Failed to insert item")
    return ItemInDB(**item_data)  # ensure the returned item includes the id


@router.get("/items/{item_id}", response_model=ItemInDB)
async def read_item_endpoint(item_id: str):
    items = repository.read_item(item_id)
    if not items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[0]


@router.get("/items", response_model=list[ItemInDB])
async def read_items_endpoint():
    items = repository.read_all_items()
    if not items:
        raise HTTPException(status_code=404, detail="Items not found")
    return items
