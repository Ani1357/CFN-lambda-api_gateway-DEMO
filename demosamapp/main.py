import requests
import json
import random

response = requests.get("https://type.fit/api/quotes/")

data = response.json()

def quotesfunc(event,context):
    
    choice = random.choice(data)

    return {
        "statusCode": 200,
        "body": json.dumps(choice, indent=3)
        }