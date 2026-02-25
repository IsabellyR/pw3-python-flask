
from flask import Flask, render_template 

app = Flask(__name__, template_folder='views')


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/lista')
def lista():
    return render_template('lista.html')
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')
# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True)