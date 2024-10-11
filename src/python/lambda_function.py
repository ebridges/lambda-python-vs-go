import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    try:
        # Assuming the user_id is passed as a query parameter
        user_id = event['queryStringParameters']['user_id']
        
        # Query the DynamoDB table
        response = table.query(
            KeyConditionExpression=Key('user_id').eq(user_id)
        )
        
        # Extract the items from the response
        items = response['Items']
        
        # Prepare the response
        if items:
            return {
                'statusCode': 200,
                'body': json.dumps(items[0])  # Assuming user_id is unique, return the first (and only) item
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }