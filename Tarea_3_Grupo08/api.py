import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:iwayato@localhost/tarea3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ORM
# Se crea la tabla personas
class Personas(db.Model):
    __tablename__ = 'personas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    usuario_suscripcion = db.Column(db.Boolean, nullable=False)
    artista_nombre_artistico = db.Column(db.String(50), nullable=False)
    artista_verirficado = db.Column(db.Boolean, nullable=True)
    tipo_de_persona = db.Column(db.Boolean, nullable=False)
    facturas = db.relationship("Facturas")
    reproducciones = db.relationship("Reproducciones")

class Facturas(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True)
    monto_facturado = db.Column(db.Integer, primary_key=True)
    fecha_facturacion = db.Column(db.DateTime, primary_key=True)
    fecha_vencimiento = db.Column(db.DateTime, primary_key=True)
    estado = db.Column(db.Boolean, primary_key=True)
    metodo_de_pago = db.Column(db.String(100), nullable=False)
    fecha_hora_pago = db.Column(db.DateTime, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('personas.id'))

class Reproducciones(db.Model):
    __tablename__ = 'reproducciones'
    id_usuario = db.Column(db.Integer, db.ForeignKey('personas.id'))
    id_cancion = db.Column(db.Integer, db.ForeignKey('canciones.id'))

class Canciones(db.Model):
    __tablename__ = 'canciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(1000), nullable=False)
    fecha_hora_pago = db.Column(db.DateTime, primary_key=True)
    reproducciones = db.relationship("Reproducciones")



