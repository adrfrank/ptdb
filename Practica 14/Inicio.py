import wx
from GUIPractica14 import *
import Db

class Dialog (dlgMesaje):
	def __init__ (self,parent):
		dlgMesaje.__init__(self,parent)
		pass
	def setText(self,text):
		self.lblMensaje.SetLabel(text)
		pass

class Datos(DataFrame):
	def __init__(self, parent):
		DataFrame.__init__(self,parent)
		pass
	def showData(self):
		sql = "select * from Sucursales"
		res = Db.runSQL(sql)
		if res != None and res != -1 :
			self.gDatos.ClearGrid()
			for i in range(len(res)):
				self.gDatos.AppendRows(1)
				self.gDatos.SetCellValue(i,0, str( res[i][0]))
				self.gDatos.SetCellValue(i,1, str(res[i][1]))
				self.gDatos.SetCellValue(i,2, str(res[i][2]))
				self.gDatos.SetCellValue(i,3, str(res[i][3]))
		pass

class InsertF(InsertFrame):
	def __init__(self,parent):
		InsertFrame.__init__(self,parent)
		self.parent = parent
		self.limpiar()
		pass
	def limpiar(self):
		self.txtNombre.SetValue("")
		self.txtDireccion.SetValue("")
		self.txtTelefono.SetValue("")	
		pass
	def btnGuardarClick(self,event):
		nombre = self.txtNombre.GetValue()
		direccion = self.txtDireccion.GetValue()
		telefono = self.txtTelefono.GetValue()
		
		sql = "insert into Sucursales values(default,'{0}', '{1}', '{2}')".format(nombre,direccion,telefono)
		res = Db.runSQL(sql)
		if res != -1:
			self.parent.dlg.setText("Datos insertados correctamente")
		else:
			self.parent.dlg.setText("Ocurrio un problema insertando los datos")
		self.parent.dlg.ShowModal()
		self.Show(False)
		pass

	def btnCancelarClick(self,event):
		self.txtNombre.SetValue("")
		self.txtDireccion.SetValue("")
		self.txtTelefono.SetValue("")	
		self.Show(False)	
		pass

class BuscarF(SearchFrame):
	editarFrame = None
	def __init__ (self,parent, operation="Eliminar"):
		SearchFrame.__init__(self,parent)
		self.parent = parent
		self.Operation = operation
		self.btnBuscar.SetLabel(operation)
		pass
	def limpiar(self):
		self.txtId.SetValue("")
		pass
	def btnBuscarClick(self,event):
		id = self.txtId.GetValue()
		if id == "":
			id = "0"
		sql = "select * from Sucursales where Id = {0}".format(id)
		res = Db.runSQL(sql)
		if res != None and res != -1 and len(res) > 0:
			if(self.Operation == "Eliminar"):
				sql = "delete from Sucursales where Id = {0}".format(id)
				res = Db.runSQL(sql)
				if res != -1:
					self.parent.dlg.setText('El registro se elimino correctamente')
				else:
					self.parent.dlg.setText('Ocurrio un problema eliminado el registro')
				self.parent.dlg.ShowModal()
				self.Show(False)
				pass
			else: #Modificar
				self.Show(False)
				if self.editarFrame == None:
					self.editarFrame = EditF(self,res[0])
				try:
					self.editarFrame.Show(True)
					self.editarFrame.Item = res[0]
					pass
				except Exception, e:
					self.editarFrame = EditF(self,res[0])
					self.editarFrame.Show(True)
				pass
			pass
		else:
			self.parent.dlg.setText('No hay registro con ese Id')
			self.parent.dlg.ShowModal()
			self.Show(False)
		pass

class EditF(EditFrame):
	Item = None
	def __init__(self,parent,item):
		EditFrame.__init__(self,parent)
		self.Item = item
		self.asignarValores()
		self.parent = parent
		pass

	def limpiar(self):
		self.txtTelefono.SetValue("")
		self.txtNombre.SetValue("")
		self.txtDireccion.SetValue("")
		pass
	def asignarValores(self):
		self.txtNombre.SetValue(self.Item[1])
		self.txtDireccion.SetValue(self.Item[2])
		self.txtTelefono.SetValue(self.Item[3])
		pass
	def btnEditarClick(self,event):
		nombre = self.txtNombre.GetValue()
		direccion = self.txtDireccion.GetValue()
		telefono = self.txtTelefono.GetValue()
		print self.Item
		sql = "update Sucursales set Nombre = '{0}', Direccion = '{1}', Telefono = '{2}' where Id = {3} ".format(nombre,direccion,telefono, self.Item[0])
		res = Db.runSQL(sql)
		if res != -1:
			self.parent.parent.dlg.setText("Datos modificados correctamente")
		else:
			self.parent.parent.dlg.setText("Ocurrio un problema modificando los datos")
		self.parent.parent.dlg.ShowModal()
		pass
	def btnCancelarClick(self,event):
		self.limpiar()
		self.Show(False)
		self.parent.Show(False)
		self.parent.limpiar()
		pass

class InitFrame (MainFrame):
	dlg = None
	dataFrame = None
	insertFrame = None
	buscarFrame = None
	def __init__(self,parent):
		MainFrame.__init__(self,parent)
		self.dlg  = Dialog(self)		
		pass
	def MainFrameOnActivate(self, event):
		print 'Aplicacion iniciada'
		pass
	def mCrearTablas(self, event):
		print 'Crear tablas!!'
		res = Db.runSQL("CREATE TABLE Sucursales (Id int NOT NULL AUTO_INCREMENT , Nombre varchar(50), Direccion varchar(200), Telefono varchar(15), PRIMARY KEY (Id))")
		if res != -1:
			print 'Tablas Creadas'
			self.dlg.setText("Tablas creadas")
			self.dlg.ShowModal()
		else:
			self.dlg.setText("Ocurrio un error o las tablas ya existian")
			self.dlg.ShowModal()
		pass

	def mMostrarDatos(self,event):
		if self.dataFrame == None:
			self.dataFrame = Datos(self)
			pass
		try:
			self.dataFrame.Show(True)
			self.dataFrame.showData()
			pass
		except Exception, e:
			self.dataFrame = Datos(self)
			self.dataFrame.Show(True)
			self.dataFrame.showData()	
		pass
	def mInsertar(self,event):
		if self.insertFrame == None:
			self.insertFrame = InsertF(self)
			pass
		try:
			self.insertFrame.Show(True)
			pass
		except Exception, e:
			self.insertFrame = InsertF(self)
			self.insertFrame.Show(True)
		self.insertFrame.limpiar()
		pass
	def mEliminar(self,event):
		if self.buscarFrame == None:
			self.buscarFrame = BuscarF(self,"Eliminar")
			pass
		try:
			self.buscarFrame.Show(True)
			pass
		except Exception, e:
			self.buscarFrame = BuscarF(self,"Eliminar")
			self.buscarFrame.Show(True)
		pass
	def mModificar(self, event):
		if self.buscarFrame == None:
			self.buscarFrame = BuscarF(self,"Modificar")
			pass
		try:
			self.buscarFrame.Show(True)
			pass
		except Exception, e:
			self.buscarFrame = BuscarF(self,"Modificar")
			self.buscarFrame.Show(True)
		pass
		pass

def main():
	print 'Practica 13'
	app = wx.App(False)
	frame = InitFrame(None)
	frame.Show(True)
	app.MainLoop()
	pass

if __name__ == "__main__":
	main()





