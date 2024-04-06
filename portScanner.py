import threading
import socket
import threading
from scapy.all import *

target = input("Enter the target IP: ")
xx = 1

class PacketSniffer(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        sniff(filter=f"dst {target} and port {self.port}", prn=self.process_packet)

    def process_packet(self, packet):
        print(f"Packet received on port {self.port}: {packet.summary()}")

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        scan = s.connect((target, port))
        print("Port:", port, "is open.")
        scan.close()
    except:
        pass

for x in range(1, 9000):
    trea = threading.Thread(target=portscan, kwargs={'port': xx})
    xx += 1
    trea.start()

packet_sniffers = []
for port in range(1, 9000):
    packet_sniffer = PacketSniffer(port)
    packet_sniffers.append(packet_sniffer)
    packet_sniffer.start()

