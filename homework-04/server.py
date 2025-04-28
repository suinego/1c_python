from flask import Flask, jsonify, request
from dotenv import dotenv_values
from controllers import operation

app = Flask(__name__)

@app.route("/")
def server_info():
    return "Sofiia Server"

@app.route("/author")
def author():
    return jsonify({
        "name": "Sofiia",
        "course": 3,
        "age": 20,
    })

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})

def get_port():
    config = dotenv_values(".env")
    if "PORT" in config and config["PORT"].isdigit():
        return int(config["PORT"])
    return 5000

if __name__ == "__main__":
    app.run(debug=True, port=get_port())
