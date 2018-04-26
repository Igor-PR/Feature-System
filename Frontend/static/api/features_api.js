var baseAPI 
= "https://iws-backend.herokuapp.com/"
// = "http://127.0.0.1:5000"

/*
	addFeature makes a call to the server using with all the information for the feature colected from the form as parameter.
	After it receives the response from the server, it will create an alert with the string 'Success' in case 
	it was a success and toggles the modal or create an alert with the responseText(error) in case it was a failure
	The function checks if the user selected a Client and a Product Area in the form. In case any of them isn't selected,
	it creates an alert.
*/

function addFeature() {
	if ($('#clients').val() != 0) {
		var xhttp = new XMLHttpRequest();
		var params = "title=" + $('#title').val()+ "&" +
				  "description=" + $('#description').val()+ "&" +
				  "client_id=" + $('#clients').val()+ "&" +
				  "date=" + $('#datepicker').val()+ "&" +
				  "client_priority=" + $('#client_priority').val()+ "&" +
				  "product_area=" + $('#productAreas').val();

		
		xhttp.open("POST", baseAPI + "/Features", true);
		xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

		xhttp.onload = function(){ 
			alert ("Success!"); 
			$("#myModal").modal("toggle");
			} // success case
		xhttp.onerror = function(){ alert (xhttp.responseText); } // failure case
		
		xhttp.send(params);
	}
	else{
		alert("Client or Product Area isn't selected!")
	}
} 

/*
	getFeatures makes a call to the server with no parameters using fetch.
	After it receives the response from the server, it parses the content and calls a callback funtion that is passed
	as an argument to the function.
*/
function getFeatures(callback){
	const url = baseAPI + "/Features";
	fetch(url,  {
		mode: 'cors',
	    method : "GET",
	}).then(
	    response => response.text() 
	).then(
	    html =>{ 
	    	features = JSON.parse(html)
	    	callback(features)
	    }	
	)    
}

/*
	deleteFeature makes a call to the server using with an id as parameter.
	After it receives the response from the server, it will create an alert with the string 'Deleted' in case it was a success
	or create an alert with the responseText(error) in case it was a failure
*/

function deleteFeature() {
	var xhttp = new XMLHttpRequest();
	var params = "id=" + arguments[0]

	xhttp.open("DELETE", baseAPI + "/Features", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhttp.onload = function(){ alert ("Deleted"); } // success case
	xhttp.onerror = function(){ alert (xhttp.responseText); } // failure case

	xhttp.send(params);
}  