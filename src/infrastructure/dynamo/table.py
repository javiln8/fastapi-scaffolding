import boto3

dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-2',
                          endpoint_url='http://dynamodb-local:8000')


def create_table_if_not_exists():
    table_name = 'items'
    existing_tables = dynamodb.meta.client.list_tables()['TableNames']

    if table_name not in existing_tables:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)


create_table_if_not_exists()

table = dynamodb.Table('items')
