from config import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(db.Text(100))
    last_name = Column(db.Text(100))
    age = Column(Integer)
    email = Column(db.Text(100))
    role = Column(String(100))
    phone = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Offer(db.Model):
    __tablename__ = "offer"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, db.ForeignKey("order.id"))
    executor_id = Column(Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }


class Order(db.Model):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    name = Column(db.Text(100))
    description = Column(db.Text(1000))
    start_date = Column(Integer)
    end_date = Column(Integer)
    address = Column(db.Text(1000))
    price = Column(Integer)
    customer_id = Column(Integer, db.ForeignKey('user.id'))
    executor_id = Column(Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }
