from flask import Flask, render_template
app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/adicionar_tarefa', method=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.form.get('tarefa')
    tasks.append(nova_tarefa)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug==True)