#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route({{ .Values.url_path | quote }})
def hello_world():
    return 'Hello World'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port={{ .Values.py_port }})
