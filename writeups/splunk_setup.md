# SIEM Ingestion Setup & Telemetry Verification

## Environment Setup
* **Host Machine:** macOS (Apple Silicon M4 Pro)
* **SIEM Platform:** Splunk Enterprise (macOS native)
* **Target VM:** Ubuntu ARM64 (VirtualBox NAT Network - `10.0.2.15`)
* **Transport:** Syslog over UDP Port 514

---

## Configuration Steps

### 1. Ubuntu Telemetry Forwarding (`rsyslog`)
Appended the following forwarding rule to `/etc/rsyslog.conf` on the Ubuntu Target VM to redirect authentication events to the Mac host IP (`10.0.2.1`):

```text
auth,authpriv.* @10.0.2.1:514