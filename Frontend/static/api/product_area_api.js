var baseAPI 
= "https://iws-backend.herokuapp.com/"
// = "http://127.0.0.1:5000"

/*
	addProductArea makes a call to the server using with a product area name(productArea) as parameter.
	After it receives the response from the server, it will create an alert with the string 'Success' in case 
	it was a success and reloads the page or create an alert with the responseText(error) in case it was a failure
*/

function addProductArea() {
	var xhttp = new XMLHttpRequest();
	var params = "productArea=" + arguments[0]
	
	xhttp.open("POST", baseAPI + "/ProductAreas", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhttp.onload = function(){ 
		alert ("Success!"); 
		location.reload(); } // success case
	xhttp.onerror = function(){ alert (xhttp.responseText); } // failure case


	xhttp.send(params);
}  

/*
	deleteProductArea makes a call to the server using with an id as parameter.
	After it receives the response from the server, it will create an alert with the string 'Deleted' in case it was a success
	or create an alert with the responseText(error) in case it was a failure
*/


function deleteProductArea() {
	var xhttp = new XMLHttpRequest();
	var params = "id=" + arguments[0]

	xhttp.open("DELETE", baseAPI + "/ProductAreas", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhttp.onload = function(){ alert ("Deleted"); } // success case
	xhttp.onerror = function(){ alert (xhttp.responseText); } // failure case

	xhttp.send(params);
}  

/*
	getProductAreas makes a call to the server with no parameters using fetch.
	After it receives the response from the server, it parses the content and calls a callback funtion that is passed
	as an argument to the function.
*/
function getProductAreas(callback){
	const url = baseAPI + "/ProductAreas";
	fetch(url,  {
		mode: 'cors',
	    method : "GET",
	}).then(
		response => response.text() 
	).then(
	    html => {
	    	productAreas = JSON.parse(html)
	    	callback(productAreas)
	    }
	) 
}