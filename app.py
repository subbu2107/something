from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    data_type = request.args.get("type")

    if data_type == "fruits":
        fruits = [
            {"name": "Apple", "color": "Red", "quantity": 100, "selled": 30},
            {"name": "Banana", "color": "Yellow", "quantity": 80, "selled": 50},
            {"name": "Grapes", "color": "Green", "quantity": 90, "selled": 40},
            {"name": "Orange", "color": "Orange", "quantity": 120, "selled": 60},
            {"name": "Strawberry", "color": "Red", "quantity": 70, "selled": 25},
            {"name": "Pineapple", "color": "Brown", "quantity": 60, "selled": 15},
            {"name": "Mango", "color": "Yellow", "quantity": 110, "selled": 70}
        ]
        for f in fruits:
            f["remaining"] = f["quantity"] - f["selled"]
        return jsonify(fruits)

    elif data_type == "toys":
        toys = [
            {"name": "Car", "type": "Vehicle", "price": 150.0, "quantity": 60, "selled": 20},
            {"name": "Doll", "type": "Figure", "price": 100.0, "quantity": 40, "selled": 10},
            {"name": "Ball", "type": "Sport", "price": 50.0, "quantity": 70, "selled": 25},
            {"name": "Puzzle", "type": "Brain", "price": 80.0, "quantity": 30, "selled": 5},
            {"name": "Train", "type": "Vehicle", "price": 200.0, "quantity": 50, "selled": 18},
            {"name": "Robot", "type": "Electronic", "price": 300.0, "quantity": 20, "selled": 8}
        ]
        for t in toys:
            t["remaining"] = t["quantity"] - t["selled"]
        return jsonify(toys)

    elif data_type == "vegetables":
        vegetables = [
            {"name": "Tomato", "category": "Fruit Vegetable", "stock": 100, "selled": 30},
            {"name": "Carrot", "category": "Root", "stock": 60, "selled": 20},
            {"name": "Spinach", "category": "Leafy", "stock": 80, "selled": 45},
            {"name": "Potato", "category": "Tuber", "stock": 150, "selled": 70},
            {"name": "Onion", "category": "Bulb", "stock": 130, "selled": 50},
            {"name": "Cabbage", "category": "Leafy", "stock": 90, "selled": 30},
            {"name": "Brinjal", "category": "Fruit Vegetable", "stock": 75, "selled": 40}
        ]
        for v in vegetables:
            v["remaining"] = v["stock"] - v["selled"]
        return jsonify(vegetables)

    # Default → return UI
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
