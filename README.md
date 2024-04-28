# PRODIGY_CS_05
Network Packet Analyzer
Packet Sniffer
This Python script demonstrates how to sniff and analyze network packets to display relevant information such as source and destination IP addresses, protocols, and payload data.

How it Works
The script uses the Scapy library to sniff incoming IP packets on the network interface. For each packet captured, it extracts and prints the following information:

Source IP address
Destination IP address
Protocol (TCP, UDP, or ICMP)
Payload data (if available)
Requirements
Python 3.x
Scapy library (pip install scapy)
Usage
Clone or download this repository to your local machine.
Install the required Python library using pip install scapy.
Run the script by executing python packet_sniffer.py.
Ensure that you have appropriate privileges (root/administrator) to capture packets on the network interface.
Output
The script continuously listens for incoming packets and prints the relevant information to the console. Each captured packet displays the source and destination IP addresses, protocol type, and payload data (if available).

Note
This script is for educational purposes only. Ensure that you have proper authorization before using it.
Use responsibly and respect the privacy of others.
Be cautious when running packet sniffing code in production environments, as it may capture sensitive information.
