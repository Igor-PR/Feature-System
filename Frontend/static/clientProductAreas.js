$( document ).ready(function(){
	var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	  acc[i].addEventListener("click", function() {
	    this.classList.toggle("active");
	    var panel = this.nextElementSibling;
	    if (panel.style.maxHeight){
	      panel.style.maxHeight = null;
	    } else {
	      panel.style.maxHeight = panel.scrollHeight + "px";
	    }
	  });
	}

	getClients(updateTableClient)
	getProductAreas(updateTableProductAreas)
});


function updateTableClient(clients) {
	// Find a <table> element with id="clients":
	var table = document.getElementById("clients");

	if (clients.length != 0) {
		// Create an empty <tr> element and add it to the 1st position of the table:
		var row = table.insertRow(0);

		// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
		var cell1 = row.insertCell(0);
		var cell2 = row.insertCell(1);
		var cell3 = row.insertCell(2);

		// Add some text to the new cells:
		cell1.innerHTML = "Id";
		cell2.innerHTML = "Client";
		cell3.innerHTML = "Options";

		// var cell,i
		for(x = 0; x < clients.length; x++){
			row = table.insertRow(-1);
			row.id = "client " + clients[x][0]
			for (i = 0; i < clients[x].length; i++) {
				cell = row.insertCell(i)
				cell.innerHTML = clients[x][i]
			}

			cell = row.insertCell(-1)
			cell.innerHTML = "<button onclick='deleteFromTable(this)' class='btn btn-danger'>"
							+ "<i class='glyphicon glyphicon-remove'></i> Delete</button>"			
		}
	}
}

function updateTableProductAreas(productAreas) {
	// Find a <table> element with id="clients":
	var table = document.getElementById("productAreas");

	if (clients.length != 0) {
		// Create an empty <tr> element and add it to the 1st position of the table:
		var row = table.insertRow(0);

		// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
		var cell1 = row.insertCell(0);
		var cell2 = row.insertCell(1);
		var cell3 = row.insertCell(2);

		// Add some text to the new cells:
		cell1.innerHTML = "Id";
		cell2.innerHTML = "Product Area";
		cell3.innerHTML = "Options";

		// var cell,i
		for(x = 0; x < productAreas.length; x++){
			row = table.insertRow(-1);
			row.id = "productArea " + productAreas[x][0]
			for (i = 0; i < productAreas[x].length; i++) {
				cell = row.insertCell(i)
				cell.innerHTML = productAreas[x][i]
			}

			cell = row.insertCell(-1)
			cell.innerHTML = "<button onclick='deleteFromTable(this)' class='btn btn-danger'>"
							+ "<i class='glyphicon glyphicon-remove'></i> Delete</button>"			
		}
	}
}

function deleteFromTable(element){
	var row = element.parentNode.parentNode
	var id = row.id;
	var stringArray = id.split(" ");

	if (stringArray[0].includes("client")){
		deleteClient(stringArray[1])
	}
	else{
		if (stringArray[0].includes("productArea")){
			deleteProductArea(stringArray[1])
		}
	}

	
	row.parentNode.removeChild(row);
}

