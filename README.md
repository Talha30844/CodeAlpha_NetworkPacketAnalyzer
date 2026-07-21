# Network Packet Analyzer

## Project Overview

The Network Packet Analyzer is a Python-based application that captures and analyzes live network traffic. It helps users understand how data travels through a network by displaying important packet information such as source IP address, destination IP address, protocol type, port numbers, packet size, and payload (if available).

This project is developed for educational purposes to learn the basics of computer networking, packet structures, and network protocols.

## Objectives

- Capture live network traffic.
- Analyze the structure of network packets.
- Display useful packet information.
- Understand how different network protocols work.
- Learn packet sniffing using Python and Scapy.

## Features

- Captures live network packets.
- Displays Source IP Address.
- Displays Destination IP Address.
- Detects TCP, UDP, and ICMP protocols.
- Displays Source and Destination Port Numbers.
- Shows Packet Length.
- Displays Payload (if available).
- Runs continuously until stopped by the user.

## Technologies Used

- Python 3.x
- Scapy Library
- Npcap (Windows only)
- Visual Studio Code

## Requirements

Before running the project, install the following:

- Python 3.xs
- Scapy

Install Scapy using:

```bash
pip install scapy
```

For Windows users, install **Npcap** and enable **WinPcap Compatible Mode** during installation.

---

## Project Structure

```
PacketAnalyzer/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install Python.
2. Install Scapy.
3. Install Npcap (Windows).
4. Open Command Prompt or VS Code as Administrator.
5. Run the following command:

bash
python main.py

The program will start capturing network packets immediately.

Press **Ctrl + C** to stop the program.

## Sample Output

============================================================
Packet Length : 74 Bytes

Source IP : 192.168.1.10
Destination IP : 142.250.190.78

Protocol : TCP

Source Port : 52133
Destination Port: 443

Payload:
b'GET / HTTP/1.1 ...'
============================================================

## Protocols Used

### TCP (Transmission Control Protocol)

Used for reliable communication such as web browsing, file transfer, and email.

### UDP (User Datagram Protocol)

Used for fast communication such as video streaming, online gaming, and voice calls.

### ICMP (Internet Control Message Protocol)

Used for network diagnostics, such as the `ping` command.

## Learning Outcomes

After completing this project, you will understand:

- Basics of Computer Networks
- Packet Sniffing
- IP Addressing
- TCP/IP Protocol Suite
- Network Packet Structure
- Scapy Library
- Network Traffic Analysis

---

## Limitations

- Requires Administrator privileges.
- Payload may not be readable for encrypted traffic (HTTPS).
- Captures packets only from the selected network interface.

## Future Improvements

- Add a graphical user interface (GUI).
- Save captured packets to a file.
- Export packet details to CSV or PDF.
- Filter packets by protocol or IP address.
- Display network statistics.
- Add real-time packet graphs.

## Conclusion

This project provides a simple and practical introduction to packet sniffing using Python. It demonstrates how network packets can be captured and analyzed to better understand communication between devices. The project is intended for educational use and should only be used on networks where you have permission to monitor traffic.

## Author

**Muhammad Talha**
