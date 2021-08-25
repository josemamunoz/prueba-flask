from flask import Flask, jsonify, render_template, request
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Test

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config["DEBUG"] = True # con esta opcion el servidor me muestra los errores "Debug mode: on"
app.config["ENV"] = "development" # nos indica el environment "Environment: development"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand) # init (inicia el gestor de migraciones, crea una carpeta migrations), migrate (se encarga de ejecutar o crear las migraciones), upgrade (se encarga de enviar esas migraciones)

CORS(app) #CORS recive como parametro app


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html") #renderiza el index.html

@app.route("/test", methods=["GET", "POST"])
@app.route("/test/<int:id>", methods=["GET", "PUT", "DELETE"])
def test(id= None):
    if request.method == "GET":
        if id is not None:
            return jsonify({"msg": "ingresando por el metodo GET con parametro"}), 200
        else:
            return jsonify({"msg": "ingresando por el metodo GET"}), 200
    if request.method == "POST":
        return jsonify({"msg": "ingresando por el metodo POST"}), 200
    if request.method == "PUT":
        return jsonify({"msg": "ingresando por el metodo PUT"}), 200
    if request.method == "DELETE":
        return jsonify({"msg": "ingresando por el metodo DELETE"}), 200

if __name__ == "__main__":
    manager.run()
