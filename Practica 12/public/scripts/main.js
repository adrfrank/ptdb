;

$(".nav").on("click",'li a',function (e) {
		//console.log("click");
		//e.preventDefault();
		var li = $(e.target).closest("li");
		var nav = li.closest(".nav");
		nav.find("li").removeClass("active");
		li.addClass("active");
	});

$("#btn-test").on("click", function  (e) {
	$.ajax({
		url: '/tables/view/test',
		type: 'get',
		dataType: 'json'
	}).done(function(res){
		console.log(res);
		alert("Ok");
	}).fail(function(err){
		console.log("Error en la llamada");
		console.log(err);
	});
})

$(window).on("hashchange",function  (e) {
	console.log("Loading "+window.location.hash);
	switch(window.location.hash){
		case "#tables":
			$("#main-content").load("/tables/");
			break;
		case "#querys":
			$("#main-content").load("/querys/");
			break;
		default:
			console.log("Error cargando el recurso");
	}
})