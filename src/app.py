from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory "database"
items = {}
next_id = 1

# Create (POST /items)
@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    item = {
        "id": next_id,
        "name": data['name']
    }
    items[next_id] = item
    next_id += 1
    return jsonify(item), 201

# Read All (GET /items)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items.values()))

# Read One (GET /items/<int:item_id>)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        abort(404)
    return jsonify(item)

# Update (PUT /items/<int:item_id>)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = items.get(item_id)
    if not item:
        abort(404)
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    item['name'] = data['name']
    return jsonify(item)

# Delete (DELETE /items/<int:item_id>)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = items.pop(item_id, None)
    if not item:
        abort(404)
    return jsonify({"message": "Item deleted"})


if __name__ == '__main__':
    app.run(debug=True)
