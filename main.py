from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():

    mensagem = ""

    numero = 1
    while numero < 100:
        if numero % 2 == 0:
            mensagem += ' - ' + str(numero)
        numero += 1
    return render_template('index.html', mensagem = mensagem)

if __name__ == '__main__':
        app.run(debug=True)
