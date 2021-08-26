from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    nome = "Maria Eduarda"
    return render_template('index.html', title = 'Página Inicial', nome=nome)


@app.route('/contato')
def contato():
	return render_template('contato.html', title='Entre em Contato')