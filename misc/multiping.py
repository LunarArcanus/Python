# Pinging an IP range on Windows (Python3)

import os
import argparse
import ipaddress

def ping(begin, end, size=32, n=1):
    "Ping the range of addresses (begin, end) with size bytes of data n times."
    ip_range = range(int(ipaddress.ip_address(begin)), int(ipaddress.ip_address(end))+1)
    for address in ip_range:
        os.system("ping -n %d -l %d %s" %(n, size, str(ipaddress.ip_address(address))))

parser = argparse.ArgumentParser()
parser.add_argument("ip_start", help="IPv4 start address.")
parser.add_argument("ip_end", help="IPv4 end address.")
parser.add_argument("--size", help="Bytes per ping (defaults to 32).", type=int)
parser.add_argument("--n", help="Ping host n times (defaults to 1).", type=int)
args = parser.parse_args()

if not args.size:
	args.size = 32
if not args.n:
	args.n = 1
ping(args.ip_start, args.ip_end, args.size, args.n)
