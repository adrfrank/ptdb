//tables routes
var express = require('express');
var router = express.Router();
var pg = require('pg')

var conString = "postgres://postgres@localhost/practica12";

router.all('/view/:tablename',function  (req,res,next) {
	var table =  req.params.tablename
	pg.connect(conString, function  (err,client,done) {
		if(err) {
		    return console.error('error fetching client from pool', err);
		    next();
		}
		client.query('SELECT * FROM '+table, function(err,result) {
			done();
			if(err) {
			  	res.json({ table:null, mensaje: "no hay datos para mostrar"});
			  	next();
		      	return console.error('error running query', err);
		    }
			console.log(result);
			//console.log("Table result!");
			//console.log(result.rows.length)
			res.json({table: table, data: result.rows });
			
		});
	});

router.all('/',function  (req,res,next) {
	console.log("si deberia de cargar");
	res.render("tables/index",{});
	next();
});
	
})


module.exports = router;
