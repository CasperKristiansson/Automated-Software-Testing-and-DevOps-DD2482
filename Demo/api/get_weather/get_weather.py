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
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'The weather is sunny',
                'temperature': 25,
                'humidity': 80,
                'wind_speed': 10,
                'wind_direction': 'N',
            }),
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
