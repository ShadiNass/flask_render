from flask import Flask
import json

app = Flask(__name__)


arr = [{"name":"me", "age":45},{"name":"aaaa", "age":15},{"name":"bbbbb", "age":50}]


@app.route('/')
def hello():
    return json.dumps(arr)


if __name__ == '__main__':
    app.run(debug=True)
