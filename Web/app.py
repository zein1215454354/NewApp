from flask import request, Flask
import os
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! "

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9060))
    app.run(host='0.0.0.0', port=port)

@app.route('/plus_one')
def plus_one():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x + 1})
@app.route('/plus_two')
def plus_two():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x + 2})
@app.route('/square')
def square():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x * x})
