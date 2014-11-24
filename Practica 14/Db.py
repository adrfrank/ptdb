import MySQLdb 

def runSQL(query):
	db = MySQLdb.connect("127.0.0.1","root","","practica14")
	cursor = db.cursor();  
	data = None  
	print "Ejecutando: ",query
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