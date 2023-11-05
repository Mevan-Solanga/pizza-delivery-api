from flask import Flask,request
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class OrderDatabase(db.Model):
    order_id : Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
    user_name : Mapped[str] = mapped_column(String, nullable=False)
    pizza_type : Mapped[str] = mapped_column(String, nullable=False)
    pizza_size : Mapped[str] = mapped_column(String, nullable=False)
    phone_number : Mapped[int] = mapped_column(Integer, nullable=False)
    order_status : Mapped[str] = mapped_column(String, nullable=False)