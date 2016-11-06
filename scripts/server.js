var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var fs = require('fs');

io.on('connection', function(socket){
    
    console.log('a user connected');

    socket.on('disconnect', function(){
        console.log('user disconnected');
    });    
    
    socket.on('remote', function(msg){
	console.log(msg)
	fs.writeFile("data.txt", "", function(err) {
		if(err) {
			return console.log(err)
		}
	});
	fs.writeFile("data.txt", msg, function(err) {
		if(err) {
			return console.log(err)
		}
	});
    });
    
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
