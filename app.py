from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Produce data
produce_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/produce', methods=['GET'])
def get_produce_data():
    return jsonify(produce_data)

@app.route('/api/produce', methods=['POST'])
def add_produce():
    produce_name = request.form.get('produce_name')
    produce_quantity = request.form.get('produce_quantity')

    if produce_name and produce_quantity:
        item = {'name': produce_name, 'quantity': produce_quantity}
        produce_data.append(item)
        return jsonify({'message': 'Produce added successfully'})
    else:
        return jsonify({'error': 'Produce name and quantity are required'})

@app.route('/api/produce/search', methods=['POST'])
def search_produce():
    search_term = request.form.get('search_term').lower()
    search_results = [item for item in produce_data if item['name'].lower().includes(search_term)]

    if search_results:
        return jsonify(search_results)
    else:
        return jsonify({'message': 'Product not available in stock'})

if __name__ == '__main__':
    app.run()

