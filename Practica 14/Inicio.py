import wx
import GUIPractica14
import Db

class Dialog (GUIPractica14.dlgMesaje):
	def __init__ (self,parent):
		GUIPractica14.dlgMesaje.__init__(self,parent)
		pass
	def setText(self,text):
		self.lblMensaje.SetLabel(text)
		pass

class InitFrame (GUIPractica14.MainFrame):
	dlg = None
	def __init__(self,parent):
		GUIPractica14.MainFrame.__init__(self,parent)
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
		sql = "select * from Sucursales"
		res = Db.runSQL(sql)
		if res != None and res != -1 :
			for i in range(len(res)):
				self.gDatos.SetCellValue(i,0,str( res[i][0]))
				self.gDatos.SetCellValue(i,1, str(res[i][1]))
				self.gDatos.SetCellValue(i,2, str(res[i][2]))
				self.gDatos.SetCellValue(i,3, str(res[i][3]))
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




