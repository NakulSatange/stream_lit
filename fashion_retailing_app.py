from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Sample data for demonstration
products = [
    {'id': 1, 'name': 'Men T-Shirt', 'category': 'men', 'price': 19.99, 'image': 'path_to_image1.jpg'},
    {'id': 2, 'name': 'Women Dress', 'category': 'women', 'price': 49.99, 'image': 'path_to_image2.jpg'},
    {'id': 3, 'name': 'Unisex Hat', 'category': 'unisex', 'price': 15.99, 'image': 'path_to_image3.jpg'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query').lower()
    category = request.form.get('category').lower()

    results = [product for product in products if query in product['name'].lower() and category in product['category']]
    
    return render_template('search_results.html', products=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
