from flask import request
from flask_restful import Resource
import uuid
from database import OrderDatabase, db

class CreateOrder(Resource):
    def post(self):
        data =request.get_json()

        # TODO : extract data from request | DONE
        order_id=str(uuid.uuid4())
        user_name=str(data["user_name"])
        pizza_size=str(data["pizza_size"])
        pizza_type=str(data["pizza_type"])
        phone_number=int(data["phone_number"])

        # TODO: add data to the data base | DONE
        user = OrderDatabase(
            order_id = order_id,
            user_name = user_name,
            pizza_size = pizza_size,
            pizza_type = pizza_type,
            phone_number = phone_number
        )
        db.session.add(user)
        db.session.commit()
        message = {
            "data" : "Your order has been successfully processed!"
        }
        return message