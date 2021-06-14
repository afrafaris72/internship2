import os
from flask import Flask, flash, request, redirect, render_template,jsonify
import mysql.connector
from error_handler import ErrorHandler
from models.model import dashboard
import json
import requests

app=Flask(__name__)

# @app.route('/dashboard')
# def dash():
#     dash=list(dashboard().getTemplates().getResult())
#     return jsonify({'data':dash})

# @app.route('/data')
# def data():
#     data=list(dashboard().getData().getResult())
#     return jsonify({'data':data})

@app.route('/joiner')    
def joiner():
    joiner=list(dashboard().getJoiner().getResult())
    for x in joiner:

        templates=dict(dashboard().getTemplates({'id_templates': x['id_templates']}).getResult())
        data=dict(dashboard().getData({'id_data': x['id_data']}).getResult())

        templates_req = templates['requirements']
        result_key_param = json.loads(data['result_key'])

        data_req = requests.get(data['url'])
        data_req_result = json.loads(data_req.text)
        dump = {}
        params_key = json.loads(x['data_join'])
        for y in params_key.keys():
            keys = params_key[y].split('.')
            print(keys)
            if keys[0] == "$":
                data_result = data_req_result
                for z in keys:
                    if z != "$":
                        print(data_result)
                        data_result = data_result[z]
                dump[y] = data_result
            else:
                dump[y] = params_key[y]
            templates['html'] = templates['html'].replace(y, dump[y])

    return render_template('testing.html', data={"view":templates['html']})


@app.route('/')
def read():
    return render_template('testing.html')    

@app.errorhandler(404)
def page_not_found(error):
    return 'Not Found', 404

@app.errorhandler(500)
def error_server(error):
    return jsonify({
        "message":"Error pada server"
    }), 500

@app.errorhandler(ErrorHandler)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response