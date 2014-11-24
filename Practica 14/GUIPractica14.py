# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Practica 14", pos = wx.DefaultPosition, size = wx.Size( 293,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( wx.MB_DOCKABLE )
		self.m_menu3 = wx.Menu()
		self.menuCrear = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Crear Tablas", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.menuCrear )
		
		self.menuMostrar = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Mostrar Datos", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.menuMostrar )
		
		self.menuInsertar = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Insertar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.menuInsertar )
		
		self.menuModificar = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Modificar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.menuModificar )
		
		self.menuEliminar = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Eliminar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.menuEliminar )
		
		self.m_menubar2.Append( self.m_menu3, u"Operaciones" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.btnMostrar = wx.Button( self, wx.ID_ANY, u"Mostrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnMostrar, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnInsertar = wx.Button( self, wx.ID_ANY, u"Insertar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnInsertar, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnModificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnModificar, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnEliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnEliminar, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.mCrearTablas, id = self.menuCrear.GetId() )
		self.Bind( wx.EVT_MENU, self.mMostrarDatos, id = self.menuMostrar.GetId() )
		self.Bind( wx.EVT_MENU, self.mInsertar, id = self.menuInsertar.GetId() )
		self.Bind( wx.EVT_MENU, self.mModificar, id = self.menuModificar.GetId() )
		self.Bind( wx.EVT_MENU, self.mEliminar, id = self.menuEliminar.GetId() )
		self.btnMostrar.Bind( wx.EVT_BUTTON, self.mMostrarDatos )
		self.btnInsertar.Bind( wx.EVT_BUTTON, self.mInsertar )
		self.btnModificar.Bind( wx.EVT_BUTTON, self.mModificar )
		self.btnEliminar.Bind( wx.EVT_BUTTON, self.mEliminar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def mCrearTablas( self, event ):
		event.Skip()
	
	def mMostrarDatos( self, event ):
		event.Skip()
	
	def mInsertar( self, event ):
		event.Skip()
	
	def mModificar( self, event ):
		event.Skip()
	
	def mEliminar( self, event ):
		event.Skip()
	
	
	
	
	

###########################################################################
## Class dlgMesaje
###########################################################################

class dlgMesaje ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Practica 13", pos = wx.DefaultPosition, size = wx.Size( 417,79 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lblMensaje = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMensaje.Wrap( -1 )
		gSizer2.Add( self.lblMensaje, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DataFrame
###########################################################################

class DataFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Datos", pos = wx.DefaultPosition, size = wx.Size( 500,196 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.gDatos = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gDatos.CreateGrid( 5, 4 )
		self.gDatos.EnableEditing( False )
		self.gDatos.EnableGridLines( True )
		self.gDatos.EnableDragGridSize( False )
		self.gDatos.SetMargins( 1, 1 )
		
		# Columns
		self.gDatos.EnableDragColMove( False )
		self.gDatos.EnableDragColSize( True )
		self.gDatos.SetColLabelSize( 30 )
		self.gDatos.SetColLabelValue( 0, u"Id" )
		self.gDatos.SetColLabelValue( 1, u"Nombre" )
		self.gDatos.SetColLabelValue( 2, u"Direccion" )
		self.gDatos.SetColLabelValue( 3, u"Telefono" )
		self.gDatos.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gDatos.EnableDragRowSize( True )
		self.gDatos.SetRowLabelSize( 80 )
		self.gDatos.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gDatos.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.gDatos, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class InsertFrame
###########################################################################

class InsertFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Insertar", pos = wx.DefaultPosition, size = wx.Size( 319,207 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 319,207 ), wx.Size( 319,207 ) )
		
		fgSizer2 = wx.FlexGridSizer( 4, 2, 10, 20 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txtNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtNombre.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer2.Add( self.txtNombre, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Direccion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.txtDireccion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtDireccion.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer2.Add( self.txtDireccion, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Telefono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txtTelefono = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txtTelefono, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.btnGuardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btnGuardar, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btnCancelar, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnGuardar.Bind( wx.EVT_BUTTON, self.btnGuardarClick )
		self.btnCancelar.Bind( wx.EVT_BUTTON, self.btnCancelarClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnGuardarClick( self, event ):
		event.Skip()
	
	def btnCancelarClick( self, event ):
		event.Skip()
	

###########################################################################
## Class SearchFrame
###########################################################################

class SearchFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Buscar", pos = wx.DefaultPosition, size = wx.Size( 243,113 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 243,113 ), wx.Size( 243,113 ) )
		
		fgSizer3 = wx.FlexGridSizer( 2, 2, 0, 20 )
		fgSizer3.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3.SetMinSize( wx.Size( 200,-1 ) ) 
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Id: ", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer3.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txtId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtId.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer3.Add( self.txtId, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.btnBuscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.btnBuscar, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnBuscar.Bind( wx.EVT_BUTTON, self.btnBuscarClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnBuscarClick( self, event ):
		event.Skip()
	

###########################################################################
## Class EditFrame
###########################################################################

class EditFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editar", pos = wx.DefaultPosition, size = wx.Size( 327,210 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 4, 2, 10, 20 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.txtNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtNombre.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer3.Add( self.txtNombre, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.txtDireccion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtDireccion.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer3.Add( self.txtDireccion, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Telefono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.txtTelefono = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtTelefono.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer3.Add( self.txtTelefono, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btnEditar = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnEditar, 0, wx.ALL, 5 )
		
		self.btnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnCancelar, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnEditar.Bind( wx.EVT_BUTTON, self.btnEditarClick )
		self.btnCancelar.Bind( wx.EVT_BUTTON, self.btnCancelarClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnEditarClick( self, event ):
		event.Skip()
	
	def btnCancelarClick( self, event ):
		event.Skip()
	

