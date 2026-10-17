import socket
import sys 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1337)
print >>sys.stderr, 'starting up on %s port %s % server_address
sock.bind(server_address)

sock.listen(1)

while True
	# wait for a connection

	print >>sys.stderr, 'waiting for a connection hold up you bitch'
	connection, client_address = socket.accept()

try:
	print >>sys.stderr, 'connection from', client_address

#Receive the data in small chunks and retrasmit it 

while True
	data = connection.recv(16)
	print >>sys.stderr, 'received "%s:"' % data
if data
	print >>sys.stderr, 'sending data back to the client'
	connection.sendall(data)
	
	else:
		print >>sys.stderr, 'no more data from' client_address
		break
		

finally:
	# Clean up the connection
	connection.close()
	
# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port where the server is listening 

server_address = ('localhost' 1337)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


try:
	# Send data	
	message = ' Hello World!!'
	print >>sys.stderr 'sending "%s"' % message
	sock.sendall(message)
	#look ofr the response
	amount_received = 0
	amount_expected = len(message)
	
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >>sys.stderr, 'received "%s"' % data
		
finally:
	print >>sys.strderr, 'closing socket'
	sock.close()
	
	
	
def get_constants(prefix):
	"""create a dictionary mapping socket module constants to their names."""
	return dict( (getattr(socket, n), n)
		for n in dir(socket)
		if n.startswith(prefix)
		)
		
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection('localhost', 1337)

print >>sys.stderr, 'Family  :', families[sock.family]
print >>sys.stderr, 'Type   :', types[sock.type]
print >> sys.stderr, 'Protocol: ', protocols[socket.proto]
print >> sys.stderr



try:
	# send data
	message = 'Hello world2.0!
	print >>sys.stderr, 'sening "%s"' % message
	sock.sendall(message)
	
	amount_received = 0
	amount_expected = len(message)
	
	
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >> sys.stderr, 'received "%s"' % data
		
finally:
	print >> sys.stderr, 'closing socket'
	sock.close()
	
	
	# Create a TCP/IP socket
	sock = socket..socket(socket.AF_INET, socket.SOCK_STREAM)
	
	
	$ Bind that socket to the damn address you pussy
	server_name = sys.argv[1]
	server_address = (server_name, 1337)
	print >>sys.stderr, 'starting up on %s prot %s' % server_address
	sock.connect(server_address)
	
	try:
		message = 'Hello_world3.1'
		print >>sys.stderr, 'sending "%s"' % message
		sock.sendall(message)
		
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print >> stderr, 'received "%s"' % data
			
finally:
	sock.close()
	
	
	
	# Create theee TCP/IP socket
	scok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	
	# bind dat mothafucka
	server_address = (''. 1337)
	sock.bind(server_address)
	print >> sys.stderr, 'starting up on %s prot %s' % sock.getsockname()
	sock.listen(1)
	
	
	while True:
		print >>sys.stderr, 'waiting for a connection'
		connection, client_address = sock.accept()
		try:
			print >> sys.stderr, 'client connected:', client_address
			while True:
				data = connection.recv(16)
				print >>sys.stderr, 'receoved "%s"' % data
				if data:
					connection.sendall(data)
				else:
					break
					
		finally:
			connection.close()
		

