import socket
import struct

import argparse
import binascii

parser = argparse.ArgumentParser(version="0.1",description='Magic packet sender')
parser.add_argument('--mac', action="store", default=None, required=True, help="The mac address to wake up")
arg = parser.parse_args()

arg.mac = arg.mac.replace(":",'')

data 		= ''.join(['FFFFFFFFFFFF', arg.mac * 20])
send_data 	= '' 

for i in range(0, len(data), 2):
	send_data = ''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(send_data, ('<broadcast>', 7))
sock.close()