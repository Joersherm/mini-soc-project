# Port Scan Report

## Target
Ubuntu VM: 10.0.2.15

## Scan

Command:
sudo nmap -sS -p- 10.0.2.15

## Findings

| Port | Protocol | State | Service |
|------|----------|-------|---------|
| 22   | TCP      | Open  | SSH     |

## Analysis

Port 22 was open, indicating that the Ubuntu
machine was accepting SSH connections.

The open SSH service became the target for
the next phase of the lab: authentication
testing and log analysis.