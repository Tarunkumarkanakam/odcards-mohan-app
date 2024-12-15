from app.db.database import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Text
)
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')


def get_ist_time():
    return datetime.now(IST)

# Accounts Table


class Account(Base):
    __tablename__ = 'accounts'

    gmail_id = Column(String(20), primary_key=True)
    access_token = Column(String(255), nullable=False)
    refresh_token = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=get_ist_time)
    updated_at = Column(DateTime, default=get_ist_time, onupdate=get_ist_time)

    user = relationship('User', back_populates='accounts')

# Users Table


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)

    # Relationships
    accounts = relationship('Account', back_populates='user')
    customers = relationship('Customer', back_populates='user')
    # Fixed relationship to orders
    orders = relationship('Order', back_populates='user')

# Customers Table


class Customer(Base):
    __tablename__ = 'customers'

    email_id = Column(String(30), primary_key=True)  # Primary key
    name = Column(String(50), nullable=False)
    phone_number = Column(String(10), nullable=False)
    city = Column(String(50), nullable=False)
    address = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=get_ist_time)
    updated_at = Column(DateTime, default=get_ist_time, onupdate=get_ist_time)

    # Relationship to User
    user = relationship('User', back_populates='customers')

# Order Types Table


class OrderType(Base):
    __tablename__ = 'order_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)

    # Relationship to Orders
    orders = relationship('Order', back_populates='order_type')

# Orders Table


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer = Column(String(30), ForeignKey(
        'customers.email_id'), nullable=False)
    type = Column(Integer, ForeignKey('order_types.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    to_email = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    # Added user_id for foreign key
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=get_ist_time)
    updated_at = Column(DateTime, default=get_ist_time, onupdate=get_ist_time)

    # Relationships
    # No back_populates as not bidirectional
    customer_rel = relationship('Customer')
    order_type = relationship('OrderType', back_populates='orders')
    user = relationship('User', back_populates='orders')
