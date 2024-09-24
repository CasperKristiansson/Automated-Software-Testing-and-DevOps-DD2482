import boto3
import json

dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Max-Age': '3600',
            }
        }

    try:
        dynamodb.put_item(
            TableName='kth-devops-example-db-dev',
            Item={
                'pk': {'S': 'test@example.com'},
                'sk': {'S': 'USER'},
                'name': {'S': 'John Doe'},
                'role': {'S': 'Admin'},
            })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User added successfully',
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
            'body': json.dumps({
                'message': f'Error inserting item: {str(e)}',
            }),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate',
                'Expires': '0',
                'Pragma': 'no-cache',
            },
        }
