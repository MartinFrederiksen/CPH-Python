#!flask/bin/python
from flask import Flask, jsonify, abort, request
import datetime
import mysql.connector

app = Flask(__name__)

data = []

@app.route('/')
def index():
    return "Hello, World from flask server!"

@app.route('/setup')
def setup():
    cnx = mysql.connector.connect(user='dev', password='ax2',
                              host='127.0.0.1',
                              port='3307',
                              database='test',
                              use_pure=True) # use_pure is necessary when open_ssl package is from python 3.7 :-( 
    cursor = cnx.cursor()
    query = ("SELECT AAR, BYDEL, ALDER, STATKODE, PERSONER FROM befkbhalderstatkode")
    cursor.execute(query)

    for (aar, bydel, alder, statkode, personer) in cursor:
        data.append({
            'AAR': aar,
            'BYDEL': bydel,
            'ALDER': alder,
            'STATKODE': statkode,
            'PERSONER': personer
        })
    cursor.close()
    cnx.close()
    return "Setup complete!"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True)