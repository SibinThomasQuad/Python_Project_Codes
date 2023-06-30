from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_swagger import swagger

app = Flask(__name__)

# Example data
items = [
    {"id": 1, "name": "Item 1", "price": 10.0},
    {"id": 2, "name": "Item 2", "price": 20.0},
]

# GET /items - Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# GET /items/{item_id} - Get item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"})

# POST /items - Create a new item
@app.route("/items", methods=["POST"])
def create_item():
    item = request.get_json()
    items.append(item)
    return jsonify({"message": "Item created successfully"})

# PUT /items/{item_id} - Update an item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_item = request.get_json()
    for item in items:
        if item["id"] == item_id:
            item.update(updated_item)
            return jsonify({"message": "Item updated successfully"})
    return jsonify({"error": "Item not found"})

# DELETE /items/{item_id} - Delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return jsonify({"message": "Item deleted successfully"})
    return jsonify({"error": "Item not found"})

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask Swagger"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Swagger JSON specification
@app.route('/swagger.json')
def swagger_spec():
    swag = swagger(app)
    swag['info']['title'] = "Flask Swagger"
    swag['info']['version'] = "1.0"
    return jsonify(swag)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
