import boto3
from boto3.dynamodb.types import TypeDeserializer

dynamodb = boto3.client('dynamodb')
deserializer = TypeDeserializer()


def lambda_handler(event, context):
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

    try:
        response = dynamodb.get_item(
            TableName='kth-devops-example-db-dev',
            Key={
                'pk': {'S': 'test@example.com'},
                'sk': {'S': 'USER'}
            }
        )

        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': 'Item not found',
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                },
            }

        return {
            'statusCode': 200,
            'body': {k: deserializer.deserialize(v) for k, v in response['Item'].items()},
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
        }
