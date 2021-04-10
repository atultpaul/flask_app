"""
Flask app Which takes the relation and
return parent-child relation as response
Author : Atul T Paul(atultpaul@gmail.com)
"""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/find_path', methods=['POST'])
def find_parents():
    if request.method == 'POST':
        payload = request.json
        relation = payload["relation"]
        node_id = payload["node_ids"]
        child_nodes = {}
        final_resp = {}
        for i in range(len(relation)):
            child_vsr = relation[i]["child"]
            child_nodes[child_vsr] = []
        for i in range(len(relation)):
            if relation[i]["child"] in child_nodes.keys():
                child_nodes[relation[i]["child"]].append(relation[i]["parent"])
        for item in child_nodes:
            for i in child_nodes[item]:
                if i in child_nodes:
                    child_nodes[item].extend(child_nodes[i])
        for item in child_nodes:
            child_nodes[item].sort()
            child_nodes[item].append(item)
        print(child_nodes)
        for element in node_id:
            if element in child_nodes:
                final_resp[element] = child_nodes[element]
            else:
                pass
        return final_resp
    else:
        return "Error 405 Method Not Allowed"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
