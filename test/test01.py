import requests
import json
from flask import jsonify

url='http://127.0.0.1:8000/pizza-delivery-api/order'
data={
    'user_name':'Karan',
    'pizza_size':'S',
    'pizza_type':'magarita',
    'phone_number' : '6476984210'
}

json_data = json.dumps(data)

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json_data, headers=headers)

