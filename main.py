import webview
from flask import Flask, render_template

app = Flask(__name__, static_folder='./assets', template_folder='./templates')

window = webview.create_window('Aplicação', app, min_size=(
    800, 600), background_color='#0073ff', confirm_close=True)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    webview.start(debug=True)
