import MySQLdb 
import os, sys

def mainMenu():
	op = None
	while  op == None or op != '0':
		os.system('clear')
		print 'MENU PRINCIPAL\n'
		print '1. Mostrar datos'
		print '2. Insertar datos'
		print '3. Eliminar datos'
		print '4. Modificar datos'
		print '5. Crear tablas'
		print '0. Salir'
		op = raw_input('Opcion: ')
		realizarAccion(op)
		pass
def pause():
	raw_input('Presione cualquier tecla para continuar')

def realizarAccion(op):
	os.system('clear')
	if op == '1':
		mostrarDatos()
		pass
	if op == '2' :
		insertarDatos()
		pass
	if op == '3' :
		eliminarDatos()
		pass
	if op == '4' :
		modificarDatos()
		pass
	if op == '5' :		
		crearTablas()
		pass
	if op == '6':
		test()
		pass
	pass

def crearTablas():
	print 'Creando tablas'
	res = runSQL("CREATE TABLE Sucursales (Id int NOT NULL AUTO_INCREMENT , Nombre varchar(50), Direccion varchar(200), Telefono varchar(15), PRIMARY KEY (Id))")
	if res != -1:
		print 'Tablas creadas correctamente'
	pause()
	pass

def mostrarDatos():
	print 'Mostrando datos: '
	res =  runSQL("select * from Sucursales")
	if res != None:
		for r in res:
			print r
		pass
	else:
		print 'No hay registros'
	pause()
	pass

def insertarDatos():
	print 'Insertar datos: '
	nombre = raw_input('Ingrese el nombre: ')
	direccion = raw_input('Ingrese la direccion: ')
	telefono = raw_input('Ingrese el telefono: ')
	sql = "insert into Sucursales values(default,'"+nombre+"', '"+direccion+"', '"+telefono+"')"
	res = runSQL(sql)
	if res != -1:
		print 'El registro se inserto correctamente'
	pause()
	pass

def eliminarDatos():
	print 'Eliminar datos: '
	id = raw_input('Ingrese id del registro que desea eliminar: ')
	res = buscarDato(id);
	if res == None or res == -1 or len(res) == 0:
		print 'No hay ningun registro que tenga ese id'
	else:
		print 'Registro a elimnar: '
		print res
		op = raw_input('continuar [s/n]')
		if op == 's' or op == 'S':
			sql = 'delete from Sucursales where id = '+id
			res = runSQL(sql)
			if res != -1:
				print 'El registro se elimino correctamente'
			else:
				print 'Ocurrio un problema eliminado el registro'
	pause()
	pass

def modificarDatos():
	print 'Modificar datos: '
	id = raw_input('Ingrese id del registro que desea modificar ')
	res =  buscarDato(id)
	if res == None or res == -1 or len(res)  == 0:
		print 'No hay ningun registro que tenga ese id'
	else: 
		print 'Registro encontrado: '
		print res
		op = raw_input('Desea modificar el Nombre? [s/n]: ')
		if op == 's' or op == 'S':
			nombre = raw_input('Ingrese el nuevo nombre: ')
			sql = "update Sucursales set nombre = '"+ nombre+ "' where id = "+ id
			res = runSQL(sql)
			if res != -1:
				print 'La modificacion se realizo correctamente'
			else:
				print 'Ocurrio un error modificando el nombre'
			pass
		op = raw_input('Desea modificar la direccion? [s/n]: ')
		if op == 's' or op == 'S':
			direccion = raw_input('Ingrese la nueva direccion: ')
			sql = "Update Sucursales set direccion = '"+direccion+"' where id = "+id
			res = runSQL(sql)
			if res != 1:
				print 'La modificacion se realizo correcamente'
			else:
				print 'Ocurrio un error modificando la direccion'
			pass
		op = raw_input('Desea modificar el telefono? [s/n]: ')
		if op == 's' or op == 'S':
			telefono = raw_input('Ingrese el nuevo telefono: ')
			sql = "Update Sucursales set telefono = '"+telefono+"' where id = "+id
			res = runSQL(sql)
			if res != 1:
				print 'La modificacion se realizo correcamente'
			else:
				print 'Ocurrio un error modificando el telefono'
			pass
	pass



def buscarDato(id):
	if id == None:
		return None
	sql = 'select * from Sucursales where id = '+id
	res = runSQL(sql)
	return res
	pass

def test():
	res = runSQL("select * from test")
	if res != None:
		for r in res:
			print r
		pass
	pause()
	pass

def runSQL(query):
	db = MySQLdb.connect("127.0.0.1","root","","practica13")
	cursor = db.cursor();  
	data = None  
	try:
		cursor.execute(query)
		if query.upper().startswith('SELECT'): 
			data = cursor.fetchall()   
		else: 
			db.commit()              
			#data = None 
		pass
	except Exception, e:
		print e
		data = -1
		pass	
	cursor.close()                 
	db.close() 
	return data  
	pass

def main():
	print "Practica 13"
	mainMenu()


if __name__ == "__main__":
	main()