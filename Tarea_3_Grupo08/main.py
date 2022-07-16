from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import config
from models import db, Personas, Facturas, Canciones, Reproducciones
import datetime

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
		json['id_cancion'],
		json['cantidad_reproducciones'],
		json['ultima_reproduccion']
	)
	response = jsonify(reproduccion.json())
	return response

@app.route('/api/reproducciones/<id_usuario>/<id_cancion>', methods=['PUT'])
def editar_reproducciones(id_usuario, id_cancion):
	json = request.get_json()
	reproduccion = Reproducciones.query.filter_by(id_usuario=id_usuario, id_cancion=id_cancion).first()
	reproduccion.cantidad_reproducciones = json['cantidad_reproducciones']
	reproduccion.ultima_reproduccion = json['ultima_reproduccion']
	reproduccion.update()
	return jsonify(reproduccion.json())

@app.route('/api/reproducciones/<id_usuario>/<id_cancion>', methods=['DELETE'])
def delete_reproduccion(id_usuario, id_cancion):
    reproduccion = Reproducciones.query.filter_by(id_usuario=id_usuario, id_cancion=id_cancion).first()
    reproduccion.delete()
    return jsonify({'Mensaje':'Reproducción borrada'})

#EndPoint para identificar a morosos
@app.route('/api/facturas/moroso/<id_usuario>', methods=['GET'])
def get_morosos(id_usuario):
	facturas_usuario = [factura.json() for factura in Facturas.query.filter_by(id_usuario=id_usuario)]
	fechas_vencimiento = [(factura['fecha_vencimiento'], factura['id'], factura['monto_facturado'], factura['fecha_facturacion']) for factura in facturas_usuario]
	delta = [((datetime.date.today() - fecha[0]).days, fecha[1], fecha[2], fecha[3], fecha[0]) for fecha in fechas_vencimiento]
	response = {"mensaje": str(), "facturas": []}

	for d in delta:
		if d[0] >= 1:
			response["mensaje"] = "El usuario tiene facturas vencidas"
			response["facturas"].append({"id_factura": d[1], "montofacturado": d[2], "fecha_facturacion": d[3].strftime("%Y/%m/%d"), "fecha_vencimiento": d[4].strftime("%Y/%m/%d")})
		else:
			response["mensaje"] = "El usuario no tiene facturas vencidas"

	return response

#EndPoint para obtener deuda total de todas las personas morosas
@app.route('/api/facturas/deudaTotal')
def get_deudaTotal():
	facturas = [f.json() for f in Facturas.query.all()]
	fechas_vencimiento = [(f['fecha_vencimiento'], f['monto_facturado']) for f in facturas]
	factura_morosa = [((datetime.date.today() - f[0]).days, f[1]) for f in fechas_vencimiento]
	response = {"qty_personas": 0, "qty_dinero": 0}

	for f in factura_morosa:
		if f[0] >= 1:
			response['qty_personas'] = response['qty_personas'] + 1
			response['qty_dinero'] = response['qty_dinero'] + f[1]
	
	return response


if __name__ == '__main__':
	app.run(debug=True)