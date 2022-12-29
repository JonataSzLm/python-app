import webview
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='./assets', template_folder='./templates')

window = webview.create_window('Aplicação', app, min_size=(
    800, 600), background_color='#000000', confirm_close=True)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result='Resultado')

@app.route('/somar', methods=['POST'])
def somar():
    value1 = request.form['value1']
    value2 = request.form['value2']
    result = value1 + value2
    return render_template('index.html', result=result)


@app.route('/subtrair', methods=['POST'])
def subtrair():
    value1 = request.form['value1']
    value2 = request.form['value2']
    result = value1 - value2
    return render_template('index.html', result=result)


@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    value1 = request.form['value1']
    value2 = request.form['value2']
    result = value1 * value2
    return render_template('index.html', result=result)


@app.route('/dividir', methods=['POST'])
def dividir():
    value1 = request.form['value1']
    value2 = request.form['value2']
    result = value1 / value2
    return render_template('index.html', result=result)


if __name__ == '__main__':
    webview.start(debug=True)
