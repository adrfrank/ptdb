
var pg =require("pg");

var Database = {
	conString : "postgres://postgres@localhost/practica12",
	executeQuery: function  (query, res, error) {
		pg.connect(this.conString, function(err, client, done) {
			if(err) {
				error(err);
				return console.error('error fetching client from pool', err);
			}
			client.query(query, function(err, result) {
				//call `done()` to release the client back to the pool
				done();
				if(err) {
					error(err);
				  	return console.error('error running query', err);
				}
				if(res)
					res(result);
			});
		});
	}
}

module.exports = Database;