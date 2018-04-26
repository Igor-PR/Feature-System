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

	getFeatures(updateTableFeatures)
});

function updateTableFeatures(features) {
	// Find a <table> element with id="clients":
	var table = document.getElementById("features");

	if (features.length != 0) {
		// Create an empty <tr> element and add it to the 1st position of the table:
		var row = table.insertRow(0);

		// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
		var cell = row.insertCell(-1);
		cell.innerHTML = "Id";
		var cell = row.insertCell(-1);
		cell.innerHTML = "Title";
		var cell = row.insertCell(-1);
		cell.innerHTML = "Description";
		var cell = row.insertCell(-1);
		cell.innerHTML = "Client";
		var cell = row.insertCell(-1);
		cell.innerHTML = "Client Priority";
		var cell = row.insertCell(-1);
		cell.innerHTML = "Product Area";
		var cell = row.insertCell(-1);
		cell.innerHTML = "Target Date";
		var cell = row.insertCell(-1);
		cell.innerHTML = "Options";
		// var cell2 = row.insertCell(1);
		// var cell3 = row.insertCell(2);

		// Add some text to the new cells:
		// cell.innerHTML = "Id";
		// cell2.innerHTML = "Title";
		// cell2.innerHTML = "Description"
		// cell2.innerHTML = "Client"
		// cell2.innerHTML = "Client Priority"
		// cell2.innerHTML = "Product Area"
		// cell2.innerHTML = "Target Date"
		// cell3.innerHTML = "Options";

		// var cell,i
		for(x = 0; x < features.length; x++){
			row = table.insertRow(-1);
			row.id = "productArea " + features[x][0]
			for (i = 0; i < features[x].length; i++) {
				cell = row.insertCell(i)
				cell.innerHTML = features[x][i]
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

	deleteFeature(stringArray[1])

	row.parentNode.removeChild(row);
}