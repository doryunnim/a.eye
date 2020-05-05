import flask
import werkzeug
from subprocess import call
from flask_socketio import SocketIO, send

app = flask.Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

# with open('my_image_file.jpg', 'rb') as f:
#     image_data = f.read()
# emit('my-image-event', {'image_data': image_data})

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    return "Image Uploaded Successfully"

#@app.route('/')
#def hello_world():
#    return "Hello Gaemigo Project Home Page!!"
    
#@app.route('/chat')
#def chatting():
#    return render_template('chat.html')

#@socket_io.on("message")
#def request(message):
#    print("message : "+ message)
#    to_client = dict()
#    if message == 'new_connect':
#        to_client['message'] = "new user!!!"
#        to_client['type'] = 'connect'
#    else:
#        to_client['message'] = message
#        to_client['type'] = 'normal'
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
#    send(to_client, broadcast=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
