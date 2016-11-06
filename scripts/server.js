var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var fs = require('fs');

io.on('connection', function(socket){
    
    console.log('a user connected');

    socket.on('disconnect', function(){
        console.log('user disconnected');
    });    
    
    socket.on('commands', function(msg){
        console.log(msg)
        io.emit('commands', msg)
    });
    
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
