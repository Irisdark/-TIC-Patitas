from .models import Rol, Mascota, ImagenMascota

def insertarDatosIniciales():
	# ROLES
	rol_auxiliar = Rol('Administrador')
	db.session.add(rol_auxiliar)
	db.session.commit()