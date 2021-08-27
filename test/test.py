#!/usr/bin/env python
import re
import requests
import os
import sys

from flask import Flask, render_template, request, jsonify
from lxml import etree

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    # return 'hi'
    text = None
    text = type(request.args.get('text'))
    return render_template('index.html',text=text)

@app.route('/json')
def json():
    text = request.args.get('text')
    dic = {'text':text}
    return jsonify(dic)

if __name__ == '__main__':
    app.run()
