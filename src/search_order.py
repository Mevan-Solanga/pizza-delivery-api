from flask import request
from flask_restful import Resource
from database import OrderDatabase

class SearchOrder(Resource):
    def get(self):
        data=request.get_json()

        # Build a query to search for orders based on criteria
        query = OrderDatabase.query

        if "user_name" in data:
            query = query.filter(OrderDatabase.user_name == data["user_name"])

        if "pizza_size" in data:
            query = query.filter(OrderDatabase.pizza_type == data["pizza_size"])

        if "pizza_type" in data:
            query = query.filter(OrderDatabase.pizza_size == data["pizza_type"])
        
        if "phone_number" in data:
            query = query.filter(OrderDatabase.phone_number == data["phone_number"])

        # Execute the query and get the results
        orders = query.all()

        if not orders:
            return {'message': 'No matching orders found'}, 404

        # Serialize the results and return as JSON
        result = [
            {'order_id': order.order_id, 
             'user_name': order.user_name, 
             'pizza_type': order.pizza_type, 
             'pizza_size': order.pizza_size,
             'phone_number': order.phone_number,
             'order_status': order.order_status} 
             for order in orders]
        return {'orders': result}, 200
