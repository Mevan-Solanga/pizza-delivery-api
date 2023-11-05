import requests
import json
from flask import jsonify

url='http://127.0.0.1:8000/pizza-delivery-api/order/025f3b9d-ffc3-41f8-9b2a-21d0007d9266'
data = {
    "order_status" : "Prepared",
    "pizza_size" : 'XXXS',
    "pizza_type" : None
}

json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

response_data = response.json()
with open("retrieve_order_response.json", "w") as json_file:
    json.dump(response_data, json_file, indent=4)