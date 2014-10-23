//querys.js

var express = require("express");
var router = express.Router();
var db = require('./../Database');




router.all('/execute',function (req,res,next) {
	if(req.body.query){
		var query = req.body.query;
		console.log(query);
		db.executeQuery(query, function  (results) {
			console.log(results);
			r = (results.rows?results.rows:[]);
			//console.log(r);
			res.json({mensaje:"El comando se ejecutó correctamente", data: r, table: query});
			next();
		}, function  (err) {
			res.json({error:"error ejecutando la cunsulta", errData: err})
			next();
		});

	}else{
		console.log(res);
		res.json({error:"No se envío query"});
		next();
	}
	//next();
});

router.all('/',function  (req,res,next) {
	res.render("querys/index",{});
	next();
});

module.exports = router;