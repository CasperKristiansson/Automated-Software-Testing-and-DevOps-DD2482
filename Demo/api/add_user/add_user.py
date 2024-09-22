import boto3
import json

dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
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
            'body': json.dumps('Item inserted successfully')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error inserting item: {str(e)}')
        }
