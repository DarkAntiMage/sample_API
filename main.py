from flask import Flask
app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/yahahaha/', methods=['GET'])
def lah():
    return "yha gituuu"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=105)