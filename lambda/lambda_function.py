import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('saying hello from the world in vscode!')
    }