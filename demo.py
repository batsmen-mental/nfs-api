from flask import Blueprint, request
demo = Blueprint("demo", __name__)

@demo.route('/', methods=['POST', 'GET', 'DELETE'])
def main():
    return ('Successful', 500)