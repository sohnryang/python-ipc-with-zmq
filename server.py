import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:1234')

while True:
    message = socket.recv()
    print('got message: {0}'.format(message))
    if message == b'quit':
        print('closing the server')
        socket.send(b'server closed')
        break
    time.sleep(1)
    socket.send(b'recieved message')
