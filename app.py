from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alunos')
def alunos():
    lista_alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
    return render_template('alunos.html', alunos=lista_alunos)

@app.route('/professores')
def professores():
    lista_prof = ["Marcos", "Fernanda", "João", "Patrícia"]
    return render_template('professores.html', professores=lista_prof)

@app.route('/disciplinas')
def disciplinas():
    lista_disc = ["Matemática", "Português", "História", "Ciências", "Geografia"]
    return render_template('disciplinas.html', disciplinas=lista_disc)

if __name__ == '__main__':
    app.run(debug=True)