## 1. TCP 3-Way Handshake

A normal TCP connection begins with a 3-way handshake.

The three packets are:

1. **SYN** — The client requests to establish a TCP connection.
2. **SYN-ACK** — The server acknowledges the request and responds that it is ready to communicate.
3. **ACK** — The client acknowledges the server's response.

The process can be represented as:

Kali → Ubuntu: SYN  
Kali ← Ubuntu: SYN-ACK  
Kali → Ubuntu: ACK

After these three packets, the TCP connection is established and application data can be exchanged.

In this lab, this type of handshake can be observed when Kali establishes a normal SSH connection with the Ubuntu target.

---

## 2. Nmap SYN Scan

The Nmap command used was:

    sudo nmap -sS <ubuntu-ip>

The `-sS` option performs a TCP SYN scan.

Instead of completing the normal TCP 3-way handshake, Nmap sends a SYN packet and examines the response.

For an open port, the sequence is generally:

Kali → Ubuntu: SYN  
Kali ← Ubuntu: SYN-ACK  
Kali → Ubuntu: RST

The RST packet terminates the attempted connection rather than sending the final ACK and establishing a normal application connection.

This allows Nmap to determine whether a TCP port is open without establishing a complete TCP connection.

---

## 3. Normal TCP Connection vs. Nmap SYN Scan

| Normal TCP Connection | Nmap SYN Scan |
|---|---|
| SYN | SYN |
| SYN-ACK | SYN-ACK |
| ACK | RST |
| Connection established | Connection terminated |

The main difference is the final packet.

A normal TCP connection sends an **ACK** after receiving the SYN-ACK, completing the handshake.

An Nmap SYN scan sends a **RST** instead, preventing the connection from being fully established.

---

## 4. Wireshark Filters

The following filters were used to examine the captured traffic:

### DNS

    dns

This displays DNS queries and responses.

### Initial TCP SYN packets

    tcp.flags.syn == 1 && tcp.flags.ack == 0

This filter displays TCP packets with the SYN flag set and the ACK flag unset. These packets can include the initial SYN packets generated during the Nmap scan.

### SSH traffic

    tcp.port == 22

This displays TCP traffic involving port 22, which is the standard port used by SSH.

---

## 5. Findings

The Wireshark capture demonstrated the difference between normal TCP communication and Nmap reconnaissance.

The Nmap scan generated TCP SYN packets directed at ports on the Ubuntu target. Responses from the target allowed Nmap to determine whether ports were open or closed.

The SSH traffic demonstrated TCP communication involving port 22. Failed SSH authentication attempts can also generate authentication events that are recorded by the Ubuntu operating system.

---

## 6. Security Relevance

Nmap SYN scans are commonly used for network reconnaissance. An attacker can use port scanning to identify which services are exposed by a target.

From a defensive perspective, network monitoring tools such as Wireshark can reveal patterns associated with reconnaissance, such as a large number of SYN packets being sent to different ports in a short period of time.

This type of activity could be used as an indicator of potential network scanning and could eventually be incorporated into a security detection system.

---

## Key Takeaways

- TCP normally establishes connections using SYN → SYN-ACK → ACK.
- An Nmap SYN scan uses SYN → SYN-ACK and then RST rather than completing the connection.
- Port 22 is commonly used for SSH.
- Wireshark can be used to observe TCP flags and network traffic.
- Large numbers of SYN packets targeting many ports can indicate reconnaissance activity.