<?php
// Server configuration
$host = 'localhost';
$port = 5000;

// Message to send
$client = $_GET['client'];
$message = $_GET['message'];
$message = $client.":".$message;

// Create a socket
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

// Connect to the socket
$result = socket_connect($socket, $host, $port);
if ($result === false) {
    echo 'Failed to connect to the socket: ' . socket_strerror(socket_last_error()) . PHP_EOL;
    exit;
}
socket_send($socket, 'HOST', strlen('HOST'), 0);
sleep(1);
// Send the message to the socket
$result = socket_send($socket, $message, strlen($message), 0);
if ($result === false) {
    echo 'Failed to send message to the socket: ' . socket_strerror(socket_last_error($socket)) . PHP_EOL;
}
else
{
    echo json_encode(array('status'=>true,'message'=>'message sent'));
}

// Close the socket
socket_close($socket);
?>
