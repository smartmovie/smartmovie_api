from flask import Flask, render_template, request, Response, jsonify, url_for
import requests
import json
from insertdata import InsertData

app = Flask(__name__)


@app.route('/')
def root():
    index = "Hello New World!"
    return index


@app.route('/insert_movie_data/', methods=['POST'])
def insert_movie_data():
    entry_data = request.json
    insert_movie_obj = InsertData()
    sts = insert_movie_obj.insert_movie(entry_data['moviename'],entry_data['thumb'],entry_data['trailor'],entry_data['status'],entry_data['type'])
    return sts

@app.route('/user_register/', methods=['POST'])
def user_register():
    entry_data = request.json
    user_register_obj = InsertData()
    sts = user_register_obj.insert_users(entry_data['username'],entry_data['email'],entry_data['phone'],entry_data['password'])
    return sts

@app.route('/user_login/',methods=['POST'])
def user_login():
    entry_data = request.json
    user_login_obj = InsertData()
    sts = user_login_obj.user_login_check(entry_data['username'],entry_data['password'])
    result = {'value':sts}
    return jsonify(result)







if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5001
    app.run(debug=True, host=HOST, port=PORT, threaded=True)

