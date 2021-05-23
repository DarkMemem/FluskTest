from flask import Flask, request, Response
import datetime
import random
import string

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello!</p>"


@app.route("/now")
def now():
    return str(datetime.datetime.now())


@app.route("/rand")
def get_rand():
    # print(request.args)
    # print(request.args['var'])
    length = request.args.get('length', '10 ')

    if length.isdigit():
        length = int(length)
    else:
        return Response("Error: length is not number!", status=400)

    length = int(request.args['length'])

    return "".join(random.choices(string.ascii_lowercase, k=length))


app.run(debug="Thue", port=5002)  #http://127.0.0.1:5002/rand?param_name1=param_value&var=42&length=10
