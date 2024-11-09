from flask import Flask, render_template, send_from_directory
import json
import random

app = Flask(__name__)

with open('quote_list.json', 'r') as f:
    file_contents = json.load(f)
    quotes = [item['quote'] for item in file_contents['data']]  

@app.route('/')
def index():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True)