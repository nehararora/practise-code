/*
simple.js: Some basic sample code.

*/
function fizzBuzz (n) {
	
	for(var i =1; i<=n; i++){
	
		if (i%3 == 0 && i%5 == 0) {
			console.log("FizzBuzz");
		}  else if (!(i % 3)){
			console.log("Fizz");
		} else if (!(i%5)) {
			console.log("Buzz");
		} else {
			console.log(i);
		}
	}
}


//code from: http://howtonode.org/hello-node
//Simple http server
function http_server() {
	var http =  require('http');
	
	var server = http.createServer(function (request, response) {
		response.writeHead(200, {"Content-Type": "text/plain"})
		response.end("Hello World\n");
	});
	
	server.listen(8000);
	console.log("Server running at http://127.0.0.1:8000/");
}


fizzBuzz(16);
http_server();