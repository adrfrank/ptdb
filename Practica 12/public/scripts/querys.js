//querys.js

var btnExecute = $("#btn-query");
var txtQuery = $("#txt-query");

function executeQuery (query) {
	$.ajax({
		url:'/querys/execute',
		type: 'post',
		dataType: 'json',
		data: {query:query}
	}).done(function  (res) {
		if(res.error){
			$("#res-container").html(res.error);
			$("#res-container").append(res.errData);
		}else{
			console.log(res);
			var pres = generateTable(res);
			$("#res-container").html(res.mensaje)
			$("#res-container").append(pres);
		}
		
	}).fail(function  (error) {
		$("#res-container").html("Error!")
		$("#res-container").appendz("<br />");
		$("#res-container").append(error.message);

	});
}

btnExecute.on("click",function  (e) {
	var query =  txtQuery.val().trim();
	console.log("Ejecutando: ",query);
	if(query == ""){
		alert("No hay ningun comando para enviar!");
		return false;
	}
	executeQuery(query);
});