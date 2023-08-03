from flask import Flask, jsonify, request
from flasgger import Swagger
from configure_insights import configure_insights
import user_crud

app = Flask(__name__)
swagger = Swagger(app)

instrumentation_key = '<tu-instrumentation-key>'
# Configura Azure Insights utilizando la aplicación actual
logger = configure_insights(app, instrumentation_key)

# Adjunta el logger a la aplicación de Flask
app.logger = logger

@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.json
    username = user_data.get('username')
    email = user_data.get('email')
    """
    Endpoint para crear un usuario
    ---
    responses:
        200:
            description: Usuario creado
    """
    return user_crud.create_user(username,email)

@app.route('/user/<user_id>', methods=['GET'])
def read_user(user_id):
    """
    Endpoint para obtener un usuario
    ---
    responses:
        200:
            description: Detalle del usuario
    """
    return user_crud.read_user(user_id)

@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Endpoint para actualizar un usuario
    ---
    responses:
        200:
            description: Usuario actualizado
    """
    return user_crud.update_user(user_id)

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Endpoint para eliminar un usuario
    ---
    responses:
        200:
            description: Usuario eliminado
    """
    return user_crud.delete_user(user_id)

@app.route('/')
def hello():
    logger.debug('metodo principal')
    logger.warning('Esta es una advertencia!')
    return 'Hola, mundo!'

if __name__ == '__main__':
    app.run()
