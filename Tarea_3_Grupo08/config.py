class Config:
	pass

# Definimos una clase de configuración, heredamos de la clase Config
class DevelopmentConfig(Config):
	DEBUG = True
	# Ingresamos credenciales para conexión a base de datos
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:iwayato@localhost/tarea3'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
	'development': DevelopmentConfig,
}