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

@app.route("/todo")
def todoList():
    return jsonify(
        {"Tarefa 1": "Estudar Python",
         "Tarefa 2" : "Estudar Java",
         "Tarefa 3 " : "Fazer o CP de Python",
         "Tarefa 4" : "Ir ao NEXT",
         "Tarefa 5" : "Sextou!!!"})

if __name__ == '__main__':
    app.run()

