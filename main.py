from flask import request, json, jsonify
from config import app
from model_manager import User, Offer, Order
from functions import get_all, insert_data_universal, init_db, get_all_by_id, update_universal, delete_universal


@app.route("/")
def greeting_page():
    return "Возможные URL: users, users/id, offers, offers/id, orders, orders/id"


@app.route("/users/", methods=["GET", "POST"])
def get_users():
    if request.method == "GET":
        return jsonify(get_all(User))
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_universal(User, request.json)
        elif isinstance(request.json, dict):
            insert_data_universal(User, [request.json])
        else:
            print("Неподходящий формат данных")

        return jsonify(request.json)


@app.route("/orders/", methods=["GET", "POST"])
def get_orders():
    if request.method == "GET":
        return jsonify(get_all(Order))
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_universal(Order, request.json)
        elif isinstance(request.json, dict):
            insert_data_universal(Order, [request.json])
        else:
            print("Неподходящий формат данных")

        return jsonify(request.json)


@app.route("/offers/", methods=["GET", "POST"])
def get_offers():
    if request.method == "GET":
        return jsonify(get_all(Offer))
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_universal(Offer, request.json)
        elif isinstance(request.json, dict):
            insert_data_universal(Offer, [request.json])
        else:
            print("Неподходящий формат данных")

        return jsonify(request.json)


@app.route("/users/<int:user_id>", methods=["GET", "PUT", 'DELETE'])
def get_user_by_id(user_id):
    if request.method == "GET":
        data = get_all_by_id(User, user_id)
        return jsonify(data)

    elif request.method == "PUT":
        update_universal(User, user_id, request.json)
        return "Данные обновлены"

    elif request.method == "DELETE":
        delete_universal(User, user_id, request.json)
        return "Данные удалены"


@app.route("/orders/<int:user_id>", methods=["GET", "PUT", 'DELETE'])
def get_order_by_id(user_id):
    if request.method == "GET":
        data = get_all_by_id(Order, user_id)
        return jsonify(data)

    elif request.method == "PUT":
        update_universal(Order, user_id, request.json)
        return "Данные обновлены"

    elif request.method == "DELETE":
        delete_universal(Order, user_id, request.json)
        return "Данные удалены"


@app.route("/offers/<int:user_id>", methods=["GET", "PUT", 'DELETE'])
def get_offer_by_id(user_id):
    if request.method == "GET":
        data = get_all_by_id(Offer, user_id)
        return jsonify(data)

    elif request.method == "PUT":
        update_universal(Offer, user_id, request.json)
        return "Данные обновлены"

    elif request.method == "DELETE":
        delete_universal(Offer, user_id, request.json)
        return "Данные удалены"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
