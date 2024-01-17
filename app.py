#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
    
@app.route("/")
def hello():
    return app.send_static_file("index.html")
    
@app.route("/Saludo")
def Saludo():
    return "Hola mundo"
