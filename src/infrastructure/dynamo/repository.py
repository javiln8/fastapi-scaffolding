from boto3.dynamodb.conditions import Key
from typing import List
from uuid import uuid4
from src.infrastructure.dynamo.table import table


def create_item(item):
    item = item.dict()

    if 'id' not in item or not item['id']:
        item['id'] = str(uuid4())

    response = table.put_item(Item=item)
    return response


def read_item(item_id):
    response = table.query(
        KeyConditionExpression=Key('id').eq(item_id)
    )
    return response.get('Items')


def read_all_items() -> List:
    response = table.scan()
    return response.get('Items', [])
