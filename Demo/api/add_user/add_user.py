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
                'Access-Control-Allow-Headers': 'Content-Type'
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
            'body': json.dumps('Item inserted successfully'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error inserting item: {str(e)}'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
        }
