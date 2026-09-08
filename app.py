from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "ola, anda a /registrar o a /lista en el buscador xd"

@app.route("/registrar")
def registrar():
    return render_template("registro.html")

@app.route("/lista")

def lista():
    return render_template("lista.html")

if __name__ == "__main__":

    app.run(debug=True)