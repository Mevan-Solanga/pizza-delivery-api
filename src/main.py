from flask import Flask,request
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from database import OrderDatabase, db
from create_order import CreateOrder
from retrieve_order import RetrieveOrder

#api configuration
app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(app)

# Declaring the API endpoints
api.add_resource(RetrieveOrder,"/pizza-delivery-api/order/<string:order_id>")
api.add_resource(CreateOrder,"/pizza-delivery-api/order/")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)