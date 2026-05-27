# Day 4: Subnetting

## Concepts
- Subnetting splits the network into smaller partitions.
- The subnet mask decides which devices belong to the same network.
- Routers are essential for the communication process between different networks.
- Segmentation is necessary for networking purposes.

## /24 Explained

An IP address with `/24` means that the first 24 bits refer to the network portion of the address, while the remaining 8 bits identify the host on the network.

Example:

192.168.1.15 /24

In this case:
- 192.168.1 = network
- 15 = device/host

A `/24` subnet usually allows devices from:

192.168.1.1 -> 192.168.1.254

to communicate on the same local network, with 192.168.1.0 being used to identify the network itself and 192.168.1.255 used as a way to broadcast to all devices in the network.

## Same Network vs Different Network

Devices on the same subnet can communicate directly with each other.

Example:

- 192.168.1.10/24
- 192.168.1.20/24

These are on the same network because the network portion matches.

Devices on different subnets must communicate through a router.

Example:

- 192.168.1.10/24
- 192.168.2.15/24

These are different networks because their network portions are different.

Traffic must be sent to a router or gateway to reach the other network.