from flask import Flask, jsonify, request, render_template
import json

from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    # Servir la page d'accueil
    return render_template('index.html')

@app.route('/ws/topics', methods=['GET'])
def get_topics():
    data = load_data()
    return jsonify(list(data.keys()))

@app.route('/ws/topic/<topic_name>', methods=['GET'])
def get_topic_items(topic_name):
    data = load_data()
    topic = data.get(topic_name, {})
    return jsonify(topic)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

