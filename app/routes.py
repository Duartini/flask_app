from flask import Blueprint, jsonify

main = Blueprint('main', name )

@main.route('/')

def index():
  return jsonify({'message': 'Hello, World '})
