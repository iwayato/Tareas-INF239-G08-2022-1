from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Creamos tablas
class Personas(db.Model):
    __tablename__ = 'personas'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = True)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(50), nullable=False)
    usuario_suscripcion_activa = db.Column(db.Boolean, nullable = True)
    artista_nombre_artistico = db.Column(db.String(100), nullable = True)
    artista_verificado = db.Column(db.Boolean, nullable = True)
    tipo_de_persona = db.Column(db.Boolean, nullable = True)

    @classmethod
    def create(cls, nombre, apellido, email, password, usuario_suscripcion_activa, artista_nombre_artistico, artista_verificado, tipo_de_persona):

        persona = Personas(
            nombre = nombre,
            apellido = apellido,
            email = email,
            password = password,
            usuario_suscripcion_activa = usuario_suscripcion_activa,
            artista_nombre_artistico = artista_nombre_artistico,
            artista_verificado = artista_verificado,
            tipo_de_persona = tipo_de_persona
        )
        return persona.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False
    
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'password': self.password,
            'usuario_suscripcion_activa': self.usuario_suscripcion_activa,
            'artista_nombre_artistico': self.artista_nombre_artistico,
            'artista_verificado': self.artista_verificado,
            'tipo_de_persona': self.tipo_de_persona
        }