var express = require('express');
var router = express.Router();

console.log("Cargando rutas principales");

/* GET home page. */
router.get('/', function(req, res) {
	console.log("si llega al request")
    res.render('index', { title: 'Express' });
});

router.get('/otra', function(req, res) {
	console.log("si llega al request")
    res.render('index', { title: 'otra' });
});

module.exports = router;