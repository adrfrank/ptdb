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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Practica 14", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( 0 )
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
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.gDatos = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gDatos.CreateGrid( 5, 4 )
		self.gDatos.EnableEditing( True )
		self.gDatos.EnableGridLines( True )
		self.gDatos.EnableDragGridSize( False )
		self.gDatos.SetMargins( 0, 0 )
		
		# Columns
		self.gDatos.EnableDragColMove( False )
		self.gDatos.EnableDragColSize( True )
		self.gDatos.SetColLabelSize( 30 )
		self.gDatos.SetColLabelValue( 0, u"Id" )
		self.gDatos.SetColLabelValue( 1, u"Nombre" )
		self.gDatos.SetColLabelValue( 2, u"Dirección" )
		self.gDatos.SetColLabelValue( 3, u"Telefono" )
		self.gDatos.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gDatos.EnableDragRowSize( True )
		self.gDatos.SetRowLabelSize( 80 )
		self.gDatos.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gDatos.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer1.Add( self.gDatos, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.mCrearTablas, id = self.menuCrear.GetId() )
		self.Bind( wx.EVT_MENU, self.mMostrarDatos, id = self.menuMostrar.GetId() )
		self.Bind( wx.EVT_MENU, self.mInsertar, id = self.menuInsertar.GetId() )
		self.Bind( wx.EVT_MENU, self.mModificar, id = self.menuModificar.GetId() )
		self.Bind( wx.EVT_MENU, self.mEliminar, id = self.menuEliminar.GetId() )
	
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
		gSizer2.Add( self.lblMensaje, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

