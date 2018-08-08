import sys
import zmq

context = zmq.Context()

if len(sys.argv) < 2:
    print('error: no message given')
    sys.exit(1)

print('connecting...')
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:1234')
socket.send(sys.argv[1].encode('utf-8'))
message = socket.recv()
print('got message: {0}'.format(message))
