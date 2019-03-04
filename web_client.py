from flask import Flask, render_template, request, Response, jsonify, url_for
import requests
import json
from insert_data import insert_movie

app = Flask(__name__)


@app.route('/')
def root():
    index = "Hello New World!"
    return index


@app.route('/insert_movie_data/', methods=['POST'])
def insert_movie_data():
    entry_data = request.json
    sts = insert_movie(entry_data['moviename'],entry_data['thumb'],entry_data['trailor'])
    return sts



if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5001
    app.run(debug=True, host=HOST, port=PORT, threaded=True)

