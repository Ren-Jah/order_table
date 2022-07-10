from model_manager import User, Offer, Order
from config import db
import json


def insert_data_universal(model, input_data):
    """Универсальная функция для добавления данных в зависимости от модели"""
    for row in input_data:
        db.session.add(
            model(
                **row
            )
        )

    db.session.commit()


def get_all(model):
    """Функция для получения всех данных в зависимости от модели"""
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())

    return result


def get_all_by_id(model,user_id):
    """Функция для получения всех данных по id в зависимости от модели"""
    try:
        return db.session.query(model).get(user_id).to_dict()
    except Exception as e:
        print(e)
        return {}


def update_universal(model, user_id, values):
    """Универсальная функция обновлдения данных в БД"""
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_universal(model, user_id):
    """Универсальная функция удаления данных в БД"""
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)


def init_db():
    """Функция для загрузки данных из JSON"""
    db.drop_all()
    db.create_all()
    with open("data/user.json") as file:
        insert_data_universal(User, json.load(file))

    with open("data/offer.json") as file:
        insert_data_universal(Offer, json.load(file))

    with open("data/order.json") as file:
        insert_data_universal(Order, json.load(file))
