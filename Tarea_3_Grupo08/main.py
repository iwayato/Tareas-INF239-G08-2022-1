from flask import Flask, jsonify, request
from flask_cors import CORS
from config import config
from models import db, Personas, Facturas, Canciones, Reproducciones

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

#CRUD para las facturas
@app.route('/api/facturas', methods=['GET'])
def get_facturas():
    facturas = [factura.json() for factura in Facturas.query.all()]
    response = jsonify(facturas)
    return response

@app.route('/api/facturas', methods = ['POST'])
def put_facturas():
    json = request.get_json()
    factura = Facturas.create(
		json['monto_facturado'], 
		json['fecha_facturacion'], 
		json['fecha_vencimiento'], 
		json['estado'], 
		json['metodo_de_pago'], 
		json['fecha_hora_pago'],
		json['id_usuario']
	)
    response = jsonify(factura.json())
    return response

@app.route('/api/facturas/<id>', methods=['PUT'])
def editar_facturas(id):
	json = request.get_json()
	factura = Facturas.query.filter_by(id=id).first()
	factura.monto_facturado = json['monto_facturado']
	factura.fecha_facturacion = json['fecha_facturacion']
	factura.vencimiento = json['fecha_vencimiento']
	factura.estado = json['estado']
	factura.metodo_de_pago = json['metodo_de_pago']
	factura.fecha_hora_pago = json['fecha_hora_pago']
	factura.id_usuario = json['id_usuario']
	factura.update()
	return jsonify(factura.json())

@app.route('/api/facturas/<id>', methods=['DELETE'])
def delete_factura(id):
    factura = Facturas.query.filter_by(id=id).first()
    factura.delete()
    return jsonify({'Mensaje':'Factura borrada'})

#CRUD para las canciones
@app.route('/api/canciones', methods=['GET'])
def get_canciones():
    canciones = [cancion.json() for cancion in Canciones.query.all()]
    response = jsonify(canciones)
    return response

@app.route('/api/canciones', methods = ['POST'])
def put_canciones():
    json = request.get_json()
    cancion = Canciones.create(
		json['nombre'], 
		json['letra'], 
		json['fecha_composicion']
	)
    response = jsonify(cancion.json())
    return response

@app.route('/api/canciones/<id>', methods=['PUT'])
def editar_canciones(id):
	json = request.get_json()
	cancion = Canciones.query.filter_by(id=id).first()
	cancion.nombre = json['nombre']
	cancion.letra = json['letra']
	cancion.fecha_composicion = json['fecha_composicion']
	cancion.update()
	return jsonify(cancion.json())

@app.route('/api/canciones/<id>', methods=['DELETE'])
def delete_cancion(id):
    cancion = Canciones.query.filter_by(id=id).first()
    cancion.delete()
    return jsonify({'Mensaje':'Canción borrada'})

#CRUD para las reproducciones
@app.route('/api/reproducciones', methods=['GET'])
def get_reproducciones():
	reproducciones = [reproduccion.json() for reproduccion in Reproducciones.query.all()]
	response = jsonify(reproducciones)
	return response

@app.route('/api/reproducciones', methods = ['POST'])
def put_reproducciones():
	json = request.get_json()
	reproduccion = Reproducciones.create(
		json['id_usuario'], 
		json['id_cancion']
	)
	response = jsonify(reproduccion)
	return response

@app.route('/api/reproducciones/<id>', methods=['PUT'])
def editar_reproducciones(id):
	json = request.get_json()
	reproduccion = Reproducciones.query.filter_by(id=id).first()
	reproduccion.id_usuario = json['id_usuario']
	reproduccion.id_cancion = json['id_cancion']
	reproduccion.update()
	return jsonify(reproduccion.json())

@app.route('/api/reproducciones/<id>', methods=['DELETE'])
def delete_reproduccion(id):
    reproduccion = Reproducciones.query.filter_by(id=id).first()
    reproduccion.delete()
    return jsonify({'Mensaje':'Reproducción borrada'})

if __name__ == '__main__':
	app.run(debug=True)