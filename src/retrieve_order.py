from flask import request
from flask_restful import Resource
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from flask import jsonify
from database import OrderDatabase, db

class RetrieveOrder(Resource):
    def get(self, order_id):
        order = OrderDatabase.query.filter_by(order_id=order_id).first()
        if order:
            message = {
                "data" : {
                    'order_id': order.order_id,
                    'user_name': order.user_name,
                    'pizza_type': order.pizza_type,
                    'pizza_size': order.pizza_size,
                    "order_status" : order.order_status
                }
            }, 200
            return message
        else:
            message = {
                "data" : "Error! The requested order_id was not found"
            }, 400
            return message
    def put(self, order_id):
        order = OrderDatabase.query.filter_by(order_id=order_id).first()
        if order:
            data = request.get_json()
            if (data['order_status'] is not None):
                order.order_status = data.get('order_status', order.order_status)
            if (data['pizza_size'] is not None):
                order.pizza_size = data.get('pizza_size', order.pizza_size)
            if (data['pizza_type'] is not None):
                order.pizza_type = data.get('pizza_type', order.pizza_type)
            message = {
                "data" : {
                    'order_id': order.order_id,
                    'user_name': order.user_name,
                    'pizza_type': order.pizza_type,
                    'pizza_size': order.pizza_size,
                    "order_status" : order.order_status
                }
            }, 200
            return message
        else:
            message = {
                "data" : "Error! The requested order_id was not found"
            }, 400
            return message