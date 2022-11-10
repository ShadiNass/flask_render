import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

arr = [{"name":"me", "age":45},{"name":"aaaa", "age":15},{"name":"bbbbb", "age":50}]


@app.route('/')
def hello():
    return json.dumps(arr)


if __name__ == '__main__':
    app.run(debug=True)
