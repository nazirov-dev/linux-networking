#!/bin/bash

# Change the hostname
echo "Changing hostname to 'server01'"
echo "server01" > /etc/hostname
echo "127.0.0.1   server01" >> /etc/hosts

# Create a virtual bridge interface (br0)
echo "Creating virtual bridge interface br0"
ip link add name br0 type bridge
ip link set br0 up
ip addr add 192.168.1.1/24 dev br0

# Create a virtual Ethernet pair (veth0, veth1)
echo "Creating virtual Ethernet pair veth0 and veth1"
ip link add veth0 type veth peer name veth1

# Attach veth0 to the bridge
echo "Attaching veth0 to br0 bridge"
ip link set veth0 master br0

# Bring up the interfaces
echo "Bringing up the interfaces"
ip link set veth0 up
ip link set veth1 up

# Optionally, assign an IP to veth0 (if required)
echo "Assigning IP address to veth0"
ip addr add 192.168.1.2/24 dev veth0

echo "Fake network interfaces created successfully"
