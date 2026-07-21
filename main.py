from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

# Function to analyze each packet
def packet_analyzer(packet):
    print("=" * 60)

    # Packet Length
    print(f"Packet Length : {len(packet)} Bytes")

    # Check IP Layer
    if packet.haslayer(IP):
        ip = packet[IP]

        print(f"Source IP      : {ip.src}")
        print(f"Destination IP : {ip.dst}")

        # TCP Protocol
        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print("Protocol       : TCP")
            print(f"Source Port    : {tcp.sport}")
            print(f"Destination Port: {tcp.dport}")

        # UDP Protocol
        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print("Protocol       : UDP")
            print(f"Source Port    : {udp.sport}")
            print(f"Destination Port: {udp.dport}")

        # ICMP Protocol
        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")

        else:
            print(f"Protocol Number: {ip.proto}")

        # Payload
        if packet.haslayer(Raw):
            try:
                payload = packet[Raw].load
                print("\nPayload:")
                print(payload[:100])   # Show first 100 bytes
            except:
                print("Payload: Unable to Read")

    else:
        print("Non-IP Packet")

    print("=" * 60)


print("\n")
print("======================================")
print(" Python Network Packet Analyzer ")
print("======================================")
print("Capturing Packets...")
print("Press CTRL + C to Stop\n")

# Start Capturing
sniff(prn=packet_analyzer, store=False)