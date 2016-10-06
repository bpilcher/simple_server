import sys
import socket
import os

def init_connection():
	# create a socket
	global my_socket
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# bind to an IP and port
	my_socket.bind(('127.0.0.1', 1024))

	# listen
	my_socket.listen(1)


def accept_connections():
	while True: # begin a loop of waiting for connections
		# begin accepting client connections
		conn, addr = my_socket.accept()

		# receive data
		data = conn.recv(1024)
		print "received data %s"
		data_chunks = data.split()
		if data_chunks[0] == "GET":
			file_path = data_chunks[1]
			return_info(file_path, conn)

		if not data:
			break

		#print data


def return_info(data_to_send, connection):
	# send data in return
	#file = open
	
	connection.sendall( read_file(data_to_send) )

def read_file(file_to_read):
	file_obj = open( os.path.dirname(os.path.abspath(__file__)) + file_to_read, 'r')
	file_content = file_obj.read()
	return file_content


if __name__ == "__main__":
	init_connection()
	accept_connections()