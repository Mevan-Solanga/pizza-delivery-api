from flask import request
from flask_restful import Resource
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from database import OrderDatabase, db

class RetrieveOrder(Resource):
    def get(self):
        pass