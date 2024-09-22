import boto3
from boto3.dynamodb.types import TypeDeserializer

dynamodb = boto3.client('dynamodb')
deserializer = TypeDeserializer()


def lambda_handler(event, context):
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
                'body': 'Item not found'
            }

        return {
            'statusCode': 200,
            'body': {k: deserializer.deserialize(v) for k, v in response['Item'].items()}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
