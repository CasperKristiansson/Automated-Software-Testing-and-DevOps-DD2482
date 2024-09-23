import json
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
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Max-Age': '3600'
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
                'body': json.dumps('Item not found'),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate',
                    'Expires': '0',
                    'Pragma': 'no-cache',
                },
            }

        return {
            'statusCode': 200,
            'body': json.dumps({k: deserializer.deserialize(v) for k, v in response['Item'].items()}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate',
                'Expires': '0',
                'Pragma': 'no-cache',
            },
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error getting item: {str(e)}'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate',
                'Expires': '0',
                'Pragma': 'no-cache',
            },
        }
