""" EXPLICACIÓN DE LAS IMPORTACIONES:
- OS ≥ Lo uso para construir una ruta de archivo para su database.db ≥ archivo de base de datos.
- Flask ≥ Para crear una instancia de la aplicación Flask.
- render_template() ≥ Función para representar plantillas.
- request ≥ para manejar solicitudes HTTP.
- url_for() ≥ función para construir URL para rutas.
- redirect() ≥ función para redirigir usuarios.
################################
- SQLAlchemy ≥ le brinda acceso a todas las funciones y clases de SQLAlchemy,
  además de ayudantes y funcionalidades que integran Flask con SQLAlchemy.
  Lo usará para crear un objeto de base de datos que se conecta a su aplicación Flask,
  lo que le permite crear y manipular tablas usando clases, objetos y funciones de Python sin necesidad de usar el lenguaje SQL
- func ayudante para acceder a las funciones de SQL.
"""

from flask import Flask, render_template, request, redirect, url_for
from task import Task, db

# 1. Creamos aplicación
# El parámetro template_folder es para ubicar la carpeta que tiene las plantillas
app = Flask(__name__, template_folder='../../templates')


# 2. Rutas
@app.route("/")
def home():
    task_list = Task.query.all()
    return render_template("index.html", task_list=task_list)


@app.route("/add", methods=["POST"])
def add():
    # Recogiendo los datos del form
    title = request.form.get("title")
    description = request.form.get("description")
    completed = request.form.get("completed")
    level = request.form.get("level")
    # Inicialización del objeto Task con los parámetros pasados del form
    new_task = Task(title=title, completed=completed, description=description, level=level)
    # Añadimos
    new_task.save()
    return redirect(url_for("home"))


@app.route("/update/<int:task_id>")
def update(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task.completed = not task.completed
    task.save()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    task = Task.query.filter_by(id=todo_id).first()
    task.delete()
    return redirect(url_for("home"))


# Si el nombre de este archivo es main entonces...
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Accedemos al método config de app, y al método from_object() para configurar la aplicación con la clase Config
    app.config.from_object('config.Config')
    # Inicializamos la aplicación
    db.init_app(app)
    # Usamos el contexto de la aplicación para crear todas las tablas
    with app.app_context():
        db.create_all()
    # Arrancamos la aplicación
    app.run()
