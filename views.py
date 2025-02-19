from flask import render_template

from main import app

#rotas

@app.route("/" )
def homepage():
    return render_template("homepage.html")

@app.route("/login" )
def login():
    return render_template("index.html")

@app.route("/verdade")
def verdade():
    return render_template("verdade.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
