import requests
import json
from flask import jsonify

#test case 1

url='http://127.0.0.1:8000/pizza-delivery-api/order/search'
data={
    'user_name': "Shevan"
}

json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}
response = requests.get(url, data=json_data, headers=headers)

response_data = response.json()
with open("search_order_response.json", "w") as json_file:
    json.dump(response_data, json_file, indent=4)