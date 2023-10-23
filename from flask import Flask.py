from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'

@app.route('/status/')
def get_status():
    return ({"status" : "OK"})

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1,n2):
    return f'A soma de {n1} com {n2} é {n1+n2}'

if __name__ == '__main__':
    app.run()

