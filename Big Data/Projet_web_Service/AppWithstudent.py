
from flask import Flask, jsonify, request
import json
import requests
app = Flask(__name__)


with open('servers.json', 'r') as server:
        servers = json.load(server)
def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)
def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
@app.route('/ws', methods=['GET'])
def Hello():
    return "Hello World" 

@app.route('/ws/topics', methods=['GET'])
def get_topics():
    update_local_database()
    data =load_data()
    return jsonify(list(data.keys()))

@app.route('/ws/topic/<topic_name>', methods=['GET'])
def get_topic(topic_name):
    data = load_data()
    topic = data.get(topic_name)
    if topic:
        return jsonify(topic)
    return jsonify({"message": "Topic non trouvé"}), 404


@app.route('/ws/annuaire', methods=['GET', 'POST'])
def annuaire():
    return jsonify(servers['servers'])

def update_local_database():
    with open('servers.json', 'r') as server:
        servers = json.load(server)
    for server in servers["servers"]:
            with open('data.json', 'r') as file:
                data = json.load(file)
            for topic in list(data.keys()):
                response1 = requests.get(f'{server}/ws/topics')
                topics = response1.json()
                if topic in topics:
                    response = requests.get(f'{server}/ws/topic/{topic}')
                    if response.status_code == 200:
                       known_topics = response.json() 
                       clemabase = list(data[topic].keys())
                       cles = list(known_topics.keys())
                       for cle1 in cles:
                           if cle1 in clemabase:
                               for lien in known_topics[cle1]:
                                   if lien not in  data[topic][cle1]:
                                       data[topic][cle1].append(lien)
                           else:
                                data[topic][cle1] = known_topics[cle1]                
                else:
                       for t in topics:
                            if t not in list(data.keys()):
                              response = requests.get(f'{server}/ws/topic/{t}')
                              if response.status_code == 200:
                                  known_topics = response.json()
                                  data[t]=known_topics 

            with open('data.json', 'w') as file:
                 json.dump(data, file, indent=4)

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)

