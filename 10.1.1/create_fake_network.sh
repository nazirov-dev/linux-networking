#!/bin/bash

# Change the hostname as root
echo "Changing hostname to 'server01'"
echo "server01" | sudo tee /etc/hostname
echo "127.0.0.1   server01" | sudo tee -a /etc/hosts

# Create a virtual bridge interface (br0)
echo "Creating virtual bridge interface br0"
sudo ip link add name br0 type bridge
sudo ip link set br0 up
sudo ip addr add 192.168.1.1/24 dev br0

# Create a virtual Ethernet pair (veth0, veth1)
echo "Creating virtual Ethernet pair veth0 and veth1"
sudo ip link add veth0 type veth peer name veth1

# Attach veth0 to the bridge
echo "Attaching veth0 to br0 bridge"
sudo ip link set veth0 master br0

# Bring up the interfaces
echo "Bringing up the interfaces"
sudo ip link set veth0 up
sudo ip link set veth1 up

# Optionally, assign an IP to veth0 (if required)
echo "Assigning IP address to veth0"
sudo ip addr add 192.168.1.2/24 dev veth0

echo "Fake network interfaces created successfully"
