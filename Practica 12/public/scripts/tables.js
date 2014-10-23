//tables client sctipt

function generateTable (data) {
	if(data && data.table && data.table != null){
			var $table = $("<table>").addClass("table");
			var headers = false;
			if(data.data.length == 0)
				return "No hay datos para mostrar";
			for(var i in data.data){
				if(headers == false){
					headers = true;
					var $th =  $("<tr>");
					for(var h  in data.data[i]){
						$th.append($("<th>").html(h));
						
					}
					$table.append($th);
				}
				var $tr = $("<tr>");
				for(var j in data.data[i]){
					$tr.append($("<td>").html(data.data[i][j]));
				}
				$table.append($tr);
			}			
			console.log($table);
			return $table;
		}else{
			return "Error consultando la tabla";
		}
}

$(".tablenames a").on("click",function  (e) {
	e.preventDefault();
	var btn = $(e.target);
	$.getJSON('/tables/view/'+btn.attr("data-table")).done(function  (data) {
		console.log(data);
		var container = $("#tableContainer");
		container.html(generateTable(data));
		
	})
})