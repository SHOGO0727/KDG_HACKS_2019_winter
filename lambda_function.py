import json
import requests
import boto3

def lambda_handler(event, context):
    
    ## DynamoDB
    table_name = 'sensor'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    response = table.scan() # dynamodbから取得した情報  服の外側
    
    ##
    print(float(response['Items'][0]['payload']['hum']))
    
    ##
    print(float(event['humidity'])) # AWS IoTに届いた湿度の情報 or test
    
    #######
    outer = response['Items'][0]['payload']['hum']
    inner = event['humidity']
    sa = inner + outer
    
    print(sa)
    
    #######
    
   
    
    #api
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer AV_VzVzEHPEP7m4WMYLYzfxiHkbVq5WEkXTEmhjdIQhEMrnsAcYg_-Bni7hcQpG3a76MB4uVJhh9LZZ7EPMZH4AsuyO485ePnkZvJWBEc5yf',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    data = '[ "aircon_off" ]'
    print("off!!!")
    
    if(float(sa)<=10): response = requests.post('https://api-google.gh.auhome.au.com/smarthome/execute/commands', headers=headers, data=data)


    # TODO implement
    return {
        'statusCode': 200
    }

