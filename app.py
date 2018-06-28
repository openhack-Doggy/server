import os
from flask import Flask, request 

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route("/", methods=['POST'])
    def index():
        if not 'image' in request.files:
            content = {'error': 'please send an image'}
            return content, 400 
       
        file = request.files['image']
        file.save(file.filename)
        return 'OK'

    return app