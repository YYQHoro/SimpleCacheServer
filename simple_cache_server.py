import argparse

import flask
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

app = Flask(__name__)

dict_pool = {}


@app.route('/dict/<keyname>', methods=['POST'])
def write_dict(keyname: str):
    if not keyname:
        return flask.Response(status=400)
    value = request.stream.read().decode('utf-8')
    dict_pool[keyname] = value
    return make_response(dict_pool.get(keyname))


@app.route('/dict/<keyname>', methods=['GET'])
def read_dict(keyname: str):
    if not keyname:
        return flask.Response(status=400)
    if keyname not in dict_pool:
        return flask.Response(status=404)
    return make_response(dict_pool.get(keyname))


@app.route('/all/dict', methods=['GET'])
def read_dict_all():
    return make_response(jsonify(dict_pool))


@app.route('/clear/dict', methods=['POST'])
def clear_dict():
    dict_pool.clear()
    return make_response(jsonify(dict_pool))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default='127.0.0.1', type=str, help='the server listening host')
    parser.add_argument("--port", required=True, type=int, help='the server listening port')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)
