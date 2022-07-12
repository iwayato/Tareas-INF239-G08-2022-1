from flask import Flask, jsonify, request
from flask_cors import CORS
from config import config
from models import db, Personas

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

@app.route('/api/personas', methods = ['POST'])
def put_personas():
    json = request.get_json()
    persona = Personas.create(
		json['nombre'], 
		json['apellido'], 
		json['email'], 
		json['password'], 
		json['usuario_suscripcion_activa'], 
		json['artista_nombre_artistico'],
		json['artista_verificado'],
		json['tipo_de_persona']
	)
    response = jsonify(persona.json())
    return response

@app.route('/api/personas/<id>', methods=['PUT'])
def editar_personas(id):
	json = request.get_json()
	persona = Personas.query.filter_by(id=id).first()
	persona.nombre = json['nombre']
	persona.apellido = json['apellido']
	persona.email = json['email']
	persona.password = json['password']
	persona.usuario_suscripcion_activa = json['usuario_suscripcion_activa']
	persona.artista_nombre_artistico = json['artista_nombre_artistico']
	persona.artista_verificado = json['artista_verificado']
	persona.tipo_de_persona = json['tipo_de_persona']
	persona.update()
	return jsonify(persona.json())

@app.route('/api/personas/<id>', methods=['DELETE'])
def delete_persona(id):
    persona = Personas.query.filter_by(id=id).first()
    persona.delete()
    return jsonify({'Mensaje':'Persona borrado'})

if __name__ == '__main__':
	app.run(debug=True)