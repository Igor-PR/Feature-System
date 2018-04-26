var baseAPI 
= "https://iws-backend.herokuapp.com/"
// = "http://127.0.0.1:5000"

/*
	addClient makes a call to the server using with a client name as parameter.
	After it receives the response from the server, it will create an alert with the string 'Success' in case 
	it was a success and reloads the page or create an alert with the responseText(error) in case it was a failure
*/

function addClient () {
	var xhttp = new XMLHttpRequest();
	var params = "name=" + arguments[0]
	
	xhttp.open("POST", baseAPI + "/Clients", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhttp.onload = function(){ 
		alert ("Success!"); 
		location.reload(); 
	} // success case
	xhttp.onerror = function(){ alert (xhttp.responseText); } // failure case


	xhttp.send(params);
}

/*
	deleteClient makes a call to the server using with an id as parameter.
	After it receives the response from the server, it will create an alert with the string 'Deleted' in case it was a success
	or create an alert with the responseText(error) in case it was a failure
*/

function deleteClient() {
	var xhttp = new XMLHttpRequest();
	var params = "id=" + arguments[0]

	xhttp.open("DELETE", baseAPI + "/Clients", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhttp.onload = function(){ alert ("Deleted"); } // success case
	xhttp.onerror = function(){ alert (xhttp.responseText); } // failure case

	xhttp.send(params);
}


/*
	getClients makes a call to the server with no parameters using fetch.
	After it receives the response from the server, it parses the content and calls a callback funtion that is passed
	as an argument to the function.
*/
function getClients(callback){
	const url = baseAPI + "/Clients";

	fetch(url,  {
		mode: 'cors',
	    method : "GET",
	}).then(
		response => response.text() 
	).then(
	    html => {
	    	clients = JSON.parse(html)
	    	callback(clients)
	    }
	)
}