from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)

@app.route('/new_online_user', methods = ['POST'])
def handle_online():
    content = request.get_json()
    response = ""
    if content['token'] == "1234":
        response = "Acepted"
        socketio.emit('new_online_user', {'data': content['user']})
    else:
        response = "Forbidden"
    return response


@app.route('/new_search', methods = ['POST'])
def handle_search():
    content = request.get_json()
    response = ""
    if content['token'] == "1234":
        response = "Acepted"
        socketio.emit('new_search', {'data': content['search']})
    else:
        response = "Forbidden"
    return response


if __name__ == '__main__':
    socketio.run(app, debug=True)
