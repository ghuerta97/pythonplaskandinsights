from db_connection import db
from flask import current_app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

def create_user(username, email):
    current_app.logger.debug("creando el usuario")
    current_app.logger.warning("advertencia se esta creando el usuario")
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

def read_user(user_id):
    current_app.logger.debug("leer usuario")
    current_app.logger.warning("advertencia se esta leyendo el usuario")
    return User.query.get(user_id)

def update_user(user_id, username=None, email=None):
    user = read_user(user_id)
    if username:
        user.username = username
    if email:
        user.email = email
    db.session.commit()

def delete_user(user_id):
    user = read_user(user_id)
    db.session.delete(user)
    db.session.commit()