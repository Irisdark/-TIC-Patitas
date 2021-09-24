from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from flask_login import UserMixin
import datetime
import json
import enum
from patitas import app
from .enums import Especie, Sexo, Edad, Tamanio, Pelaje, Orejas, EstadoMascota, EstadoPublicacion

db = SQLAlchemy(app)

class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}


class Usuario(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40), unique=True)
	email = db.Column(db.String(200), unique=True)
	password = db.Column(db.String(32))
	rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
	@property
	def serialize(self):
		rol = Rol.query.filter_by(id=self.rol_id).first()
		return {
				'username': self.username,
				'rol': rol.tipo_rol
			}


class Rol(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tipo_rol = db.Column(db.String(40), unique=True)
	usuariorol = db.relationship('Usuario', backref='rol', lazy='dynamic')





class Mascota(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.Unicode(40))
	especie = db.Column(db.Enum(Especie), nullable=False)
	sexo = db.Column(db.Enum(Sexo))
	color = db.Column(db.Unicode(60))
	edad = db.Column(db.Enum(Edad), nullable=False)
	tamanio = db.Column(db.Enum(Tamanio))
	oreja = db.Column(db.Enum(Orejas))
	pelaje = db.Column(db.Enum(Pelaje))
	otra_informacion_mascota = db.Column(db.Unicode(240))
	departamento = db.Column(db.String(1), nullable=False)
	localidad = db.Column(db.Integer, nullable=False)
	calle = db.Column(db.Unicode(120))
	fecha_encuentro = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	mas_informacion_encuentro = db.Column(db.Unicode(240))
	nombre_contacto = db.Column(db.Unicode(100))
	celular_contacto = db.Column(db.Integer, nullable=False)
	telefono_contacto = db.Column(db.Integer)
	estado_mascota = db.Column(db.Enum(EstadoMascota), nullable=False)
	estado_publicacion = db.Column(db.Enum(EstadoPublicacion))
	fecha_publicacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	
	@property
	def serialize(self):
		return {
				'id': self.id,
				'nombre': self.nombre,
				'especie': self.especie.value,
				'sexo': self.sexo.value,
				'color': self.color,
				'edad': self.edad.value,
				'tamanio': self.tamanio.value,
				'oreja': self.oreja.value,
				'pelaje': self.pelaje.value,
				'otra_informacion_mascota': self.otra_informacion_mascota,
				'departamento': self.departamento,
				'localidad': self.localidad,
				'calle': self.calle,
				'fecha_encuentro': self.fecha_encuentro,
				'mas_informacion_encuentro': self.mas_informacion_encuentro,
				'nombre_contacto': self.nombre_contacto,
				'celular_contacto': self.celular_contacto,
				'telefono_contacto': self.telefono_contacto,
				'estado_mascota': self.estado_mascota.value,
				'estado_publicacion': self.estado_publicacion.value,
				'fecha_publicacion': self.fecha_publicacion
			}


class ImagenMascota(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	img = db.Column(db.Text, unique=True, nullable=False)
	nombre = db.Column(db.Text, nullable=False)
	mimetype = db.Column(db.Text, nullable=False)



db.create_all()
