document.addEventListener('DOMContentLoaded', ()=> {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    send_message = socket.send(document.querySelector('.message-box').value);
}) 