# Day 2: Ports

## Objective
Understand how ports are used to access specific features and services

## Common Network Ports

### Port 22 — SSH
- Used for secure remote login
- Encrypted connection
- Commonly used by system administrators

### Port 80 — HTTP
- Standard web traffic
- Not encrypted
- Used by normal websites

### Port 443 — HTTPS
- Secure web traffic
- Used by secure websites


## Concepts
- Ports are used as part of exchanging information and are appeneded onto IPs when sent
- 3 levels of ports: system (0-1023), registered (1024-49151), private (49152 - 65535)

## Lab

### netstat -an
- Shows all the active network connections currently running on the computer along with IP and ports of the sources and destinations