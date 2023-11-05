from flask import request
from flask_restful import Resource
import uuid
from database import OrderDatabase, db

class CreateOrder(Resource):
    def post(self):
        data =request.get_json()

        # TODO : extract data from request | DONE
        try:
            order_id=str(uuid.uuid4())
            user_name=str(data["user_name"])
            pizza_size=str(data["pizza_size"])
            pizza_type=str(data["pizza_type"])
            phone_number=int(data["phone_number"])
        except:
            message = {
                "data" : "Error! The message is not formatted correctly",
                "order_id" : None
            }, 400
            return message
        try:
            order_status = "Order Received" 
            user = OrderDatabase(
                order_id = order_id,
                user_name = user_name,
                pizza_size = pizza_size,
                pizza_type = pizza_type,
                phone_number = phone_number,
                order_status = order_status
            )
            db.session.add(user)
            db.session.commit()
        except:
           message = {
                "data" : "Internal Server Error",
                "order_id" : None
            }, 500
           return message
        
        message = {
            "data" : "Success! Your order has been added to the database",
            "order_id" : str(order_id)
        }, 200
        return message