# backend/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hola', methods=['GET'])
def hola_mundo():
    return jsonify({"mensaje": "Hasta la vista ... BABY"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
