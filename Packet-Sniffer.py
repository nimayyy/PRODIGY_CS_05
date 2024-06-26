from scapy.all import *

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")
        
        if TCP in packet:
            payload = packet[TCP].payload
            print("TCP Payload:", payload)
        elif UDP in packet:
            payload = packet[UDP].payload
            print("UDP Payload:", payload)
        elif ICMP in packet:
            payload = packet[ICMP].payload
            print("ICMP Payload:", payload)
        
        print("-" * 50)

# Sniff packets and call packet_handler function for each packet
sniff(prn=packet_handler, filter="ip")
