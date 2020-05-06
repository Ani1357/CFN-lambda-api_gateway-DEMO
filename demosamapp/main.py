import requests
import json
from pprint import pprint
import random

def quotesfunc(event,context):

    response = requests.get("https://type.fit/api/quotes/")

    data = response.json()

    choice = random.choice(data)
    

    


    return {
        "statusCode": 200,
        "body": json.dumps(choice, indent=3)
        }