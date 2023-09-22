from flask import Blueprint, request
dashboard = Blueprint("demo", __name__)

@demo.route('/', methods=['POST', 'GET', 'DELETE'])
def main():
    return ('Successful', 500)