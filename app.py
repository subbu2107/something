from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    fruits = [
        {"name": "Apple", "color": "Red", "quantity": 100, "selled": 30},
        {"name": "Banana", "color": "Yellow", "quantity": 80, "selled": 50},
        {"name": "Grapes", "color": "Green", "quantity": 90, "selled": 40}
    ]
    for fruit in fruits:
        fruit["remaining"] = fruit["quantity"] - fruit["selled"]

    toys = [
        {"name": "Car", "type": "Vehicle", "price": 150.0, "quantity": 60, "selled": 20},
        {"name": "Doll", "type": "Figure", "price": 100.0, "quantity": 40, "selled": 10},
        {"name": "Ball", "type": "Sport", "price": 50.0, "quantity": 70, "selled": 25}
    ]
    for toy in toys:
        toy["remaining"] = toy["quantity"] - toy["selled"]

    vegetables = [
        {"name": "Tomato", "category": "Fruit Vegetable", "stock": 100, "selled": 30},
        {"name": "Carrot", "category": "Root", "stock": 60, "selled": 20},
        {"name": "Spinach", "category": "Leafy", "stock": 80, "selled": 45}
    ]
    for veg in vegetables:
        veg["remaining"] = veg["stock"] - veg["selled"]

    return render_template("index.html", fruits=fruits, toys=toys, vegetables=vegetables)

if __name__ == "__main__":
    app.run(debug=True)
