from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


# Inicializamos SQLAlchemy
db = SQLAlchemy()


class Task(db.Model):  # Task => hereda de db.Model
    # db.Column(tipo_columna, ...) => clase para definir columnas para tu tabla.
    id = db.Column(db.Integer, primary_key=True)
    # El primer argumento representa el tipo de columna (db.String)
    title = db.Column(db.String(100), nullable=False)
    #
    description = db.Column(db.String(200), nullable=True)
    # Los argumentos adicionales representan la configuración de la columna (nullable=False)
    completed = db.Column(db.Boolean, default=False)
    # 3 levels: NORMAL, URGENT, BLOCKING
    level = db.Column(db.String(20), nullable=False)
    # Usamos func previamente importada para crear la fecha
    created_date = db.Column(db.DateTime(timezone=True),
                             server_default=func.now())

    # Método para representar al modelo
    def __repr__(self):
        return f'<Tasks -> Title: {self.title},' \
               f'Completed: {self.completed},' \
               f'Level: {self.level},' \
               f'Description: {self.description}' \
               f'Created Date: {self.created_date}>'

    # Constructor
    def __init__(self, title, completed, description, level):
        self.title = title
        self.description = description
        self.completed = completed
        self.level = level

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        if self.id:
            db.session.delete(self)
        db.session.commit()
