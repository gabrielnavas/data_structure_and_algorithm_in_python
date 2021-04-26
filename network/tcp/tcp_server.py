import socket

IP = '0.0.0.0'
PORT = 9997
MAX_CONNECTIONS = 5

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, PORT))
	server.listen(MAX_CONNECTIONS)
	print(f'[*] Listening in {IP}:{PORT}')

	while True:
		client, address = server.accept()
		show_address(address)
		handle_client(client)

def show_address(address_list):
	client_ip = address_list[0]
	client_port = address_list[1]
	print(f'[*] Accept connection from {client_ip}:{client_port}')

def handle_client(client_socket):
	with client_socket as sock:
		request = sock.recv(1024)
		message = request.decode("utf-8")
		print(f'[*] Received: {message}')
		sock.send(b'ACK')

if __name__ == "__main__":
	main()	