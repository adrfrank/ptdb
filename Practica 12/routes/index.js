var express = require('express');
var router = express.Router();
var app = express();

console.log("Cargando rutas principales");

/* GET home page. */
router.get('/', function(req, res) {
    res.render('index', { title: 'Practica 12' });
});


module.exports = router;

