from datetime import datetime
from flask import Flask, jsonify, request
# from flask_cors import CORS
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
# CORS(app)

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
	fechas_vencimiento = [(f['fecha_vencimiento'], f['monto_facturado'], f['id_usuario']) for f in facturas]
	factura_morosa = [((datetime.date.today() - f[0]).days, f[1], f[2]) for f in fechas_vencimiento]
	response = {"qty_personas": 0, "qty_dinero": 0}
	id_morosos = []

	for f in factura_morosa:
		if f[0] >= 1:
			if f[2] not in id_morosos:
				id_morosos.append(f[2])
			response['qty_dinero'] = response['qty_dinero'] + f[1]

	response['qty_personas'] = len(id_morosos)
	return response

#EndPoint que retorna los ingresos de la compañia en los últimos 31 días
@app.route('/api/facturas/ingresos')
def get_ingresos():
	fecha_consulta = datetime.date.today()
	response = {"qty_dinero": 0}

	facturas = [f.json() for f in Facturas.query.all()]
	info = [(f['monto_facturado'], f['fecha_hora_pago'], f['estado']) for f in facturas]

	for i in info:
		if (fecha_consulta - i[1].date()).days <= 31 and i[2] == True:
			response["qty_dinero"] = response["qty_dinero"] + i[0]

	return response 

#EndPoint que retorna las 10 canciones más escuchadas por un usuario
@app.route('/api/reproducciones/topSongs/<id_usuario>')
def get_top_canciones(id_usuario):
	reproducciones = [r.json() for r in Reproducciones.query.filter_by(id_usuario=id_usuario)]
	datos_reproduccion = [(r['id_cancion'], r['cantidad_reproducciones']) for r in reproducciones]
	pre_reponse = []
	response = {"top_ten": []}

	for d in datos_reproduccion:
		cancion_fil = [c.json() for c in Canciones.query.filter_by(id = d[0])]
		nombre_cancion = cancion_fil[0]['nombre']
		pre_reponse.append((d[0], nombre_cancion, d[1]))

	pre_reponse.sort(key = lambda i:i[2], reverse = True)

	for n in range(10):
		try:
			response["top_ten"].append({
			"id_cancion" : pre_reponse[n][0], 
			"nombre_cancion" : pre_reponse[n][1],
			"reproducciones" : pre_reponse[n][2]
			})
		except:
			break
		
	return response

#EndPoint que retorna las 10 canciones más escuchadas globalmente
@app.route('/api/reproducciones/topSongsGlobal')
def get_top_canciones_global():
	reproducciones = [r.json() for r in Reproducciones.query.all()]
	datos_reproduccion = [(r['id_cancion'], r['cantidad_reproducciones']) for r in reproducciones]
	pre_reponse = []
	response = {"top_ten_global": []}
	songs = []

	for d in datos_reproduccion:
		cancion_fil = [c.json() for c in Canciones.query.filter_by(id = d[0])]
		nombre_cancion = cancion_fil[0]['nombre']
		if nombre_cancion not in songs:
			songs.append(nombre_cancion)
			pre_reponse.append( {"nombre":nombre_cancion,"id": d[0],"#reproducciones": d[1]})
		else:
			for cancion in pre_reponse:
				if nombre_cancion == cancion:
					cancion["#reproducciones"] = cancion["#reproducciones"] + d[1]
		
	
	pre_reponse.sort(key = lambda i:i["#reproducciones"], reverse = True)


	for n in range(10):
		try:
			response["top_ten_global"].append({
			"id_cancion" : pre_reponse[n]["id"], 
			"nombre_cancion" : pre_reponse[n]["nombre"],
			"reproducciones" : pre_reponse[n]["#reproducciones"]
		})
		except:
			break

	return response

if __name__ == '__main__':
	app.run(debug=True)