import sys
import os
sys.path.append(os.getcwd())

import time
from pyadept.tcputil import create_connected_client_socket, socket_send_bytes
import argparse

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description='Send some messages to a TCP server.')
    arg_parser.add_argument('--host', default='127.0.0.1')
    arg_parser.add_argument('--port', default=1234)
    arg_parser.add_argument('--sleep', type=float, default=0.25)
    args = arg_parser.parse_args()

    print(args)

    socket = create_connected_client_socket(args.host, args.port)

    socket_send_bytes(socket, b'hello\r\n')
    time.sleep(args.sleep)

    socket_send_bytes(socket, b'hello again') # <- no delimiter
    time.sleep(args.sleep)

    socket_send_bytes(socket, b', and one more time\r\n')
    time.sleep(args.sleep)

    socket_send_bytes(socket, b'one\r\ntwo\r\nthree\r\nfour\r\nfive\r\n')
    time.sleep(args.sleep)

    #socket.close()
