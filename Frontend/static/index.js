var basicUrl = "https://iws-frontend.herokuapp.com"
//= "http://127.0.0.1:8000"

$( document ).ready(function(){
	document.getElementById("clientProductArea").onclick = function () {
	    location.href = basicUrl + "/clientproductareas";
	};
	document.getElementById("showFeatures").onclick = function () {
	    location.href = basicUrl + "/features";
	};

	getClients(addOptionsToClientSelect)
	getProductAreas(addOptionsToProductAreaSelect)

});


function addOptionsToClientSelect(array) {
	var select = document.getElementById("clients");

	//Create and append the options
	for(i = 0; i < array.length; i++){
	    var option = document.createElement("option");
	    option.value = array[i][0];
	    option.text = array[i][1];
	    select.appendChild(option);
	}
}

function addOptionsToProductAreaSelect(array) {
	var select = document.getElementById("productAreas");

	//Create and append the options
	for(i = 0; i < array.length; i++){
	    var option = document.createElement("option");
	    option.value = array[i][0];
	    option.text = array[i][1];
	    select.appendChild(option);
	}
}
