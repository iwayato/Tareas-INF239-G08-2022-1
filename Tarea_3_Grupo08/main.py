from flask import Flask, jsonify, request
from flask_cors import CORS
from config import config
from models import db, Usuarios

def create_app(enviroment):
	app = Flask(__name__)
	app.config['JSON_AS_ASCII'] = False
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app

# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)
CORS(app)

# CRUD para las personas
@app.route('/api/personas', methods=['GET'])
def get_personas():
    personas = [persona.json() for persona in Personas.query.all()]
    response = jsonify(personas)
    return response

@app.route('/api/personas/<nombre>/<apellido>/<email>/<password>/<usuario_suscripcion_activa>/<artista_nombre_artistico>/<artista_verificado>/<tipo_de_persona>', methods = ['POST'])
def put_personas():
    json = request.get_json()
    persona = Personas.create(
		nombre = nombre, 
		apellido = apellido, 
		email = email, 
		password = password, 
		usuario_suscripcion_activa = usuario_suscripcion_activa, 
		artista_nombre_artistico = artista_nombre_artistico,
		artista_verificado = artista_verificado,
		tipo_de_persona = tipo_de_persona
	)
    response = jsonify(persona.json())
    return response

@app.route('/api/personas/<nombre>/<apellido>/<email>/<password>/<usuario_suscripcion_activa>/<artista_nombre_artistico>/<artista_verificado>/<tipo_de_persona>', methods=['PUT'])
def editar_persona(id):
    json = request.get_json()
    persona = Personas.query.filter_by(id=id).first()
	# Aca VSCode tirra error
    persona.nombre = nombre
	persona.apellido = apellido
	persona.email = email
	persona.password = password
	persona.usuario_suscripcion_activa = usuario_suscripcion_activa
	persona.artista_nombre_artistico = artista_nombre_artistico
	persona.artista_verificado = artista_verificado
	persona.tipo_de_persona = tipo_de_persona
    persona.update()
	# hasta aca, averiguar porque (revisar documentacion)
    return jsonify(persona.json())

@app.route('/api/personas/<id>', methods=['DELETE'])
def delete_persona(id):
    persona = Personas.query.filter_by(id=id).first()
    persona.delete()
    return jsonify({'Mensaje':'Persona borrado'})

if __name__ == '__main__':
	app.run(debug=True)