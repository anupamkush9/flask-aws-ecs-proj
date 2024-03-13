# app.py

from flask import Flask

app = Flask(__name__)

# Route to the root URL
@app.route('/')
def hello():
    return 'hello, Welcome to home page!'

# Route to a custom endpoint
@app.route('/health')
def health():
    return f'Health is Okay....'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)