from flask import Flask, render_template, request, redirect
from usuarios import Usuario
app = Flask(__name__)

@app.route("/")
def index():
    return "ola, anda a /registrar o a /lista en el buscador xd"

@app.route("/registrar", methods=["GET"])
def registrar():
    return render_template("registro.html")

@app.route("/lista")
def lista():
    
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("lista.html", todos_los_usuarios = usuarios)

@app.route("/procesar_registro", methods=["POST"])
def procesar_registro():
     datos = {
         "nombre": request.form["nombre"],
         "apellido": request.form["apellido"],
         "edad": request.form["edad"]
     }
     Usuario.save(datos)
     return redirect("/lista")

if __name__ == "__main__":

    app.run(debug=True)