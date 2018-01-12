#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)

@app.route('/api/temperature', methods=['GET'])
def get_current_temp():
    '''Local Test Example: curl -i http://localhost:5000/api/temperature'''
    latest_temp_reading = ''
    with open('logfile.txt', 'r') as f:
        latest_temp_reading = f.read(timest + ', ' + temp + ', ' + hum + '\n')
    return latest_temp_reading

@app.route('/api/humidity', methods=['GET'])
def get_current_hum():
    '''Local Test Example: curl -i http://localhost:5000/api/humidity'''
    return None

@app.route('/api/show', methods=['GET'])
def show_env():
    '''Local Test Example: curl -i http://localhost:5000/api/show'''
    return 'Not yet implemented'

if __name__ == '__main__':
    app.run(debug=True)
