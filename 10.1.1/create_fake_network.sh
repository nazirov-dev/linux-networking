#!/bin/bash

# Change hostname
echo "Changing hostname to 'server01'"
hostnamectl set-hostname server01
echo "127.0.0.1   server01" >> /etc/hosts

# Create virtual bridge interface br0 if it doesn't exist
if ! ip link show br0; then
    echo "Creating virtual bridge interface br0"
    ip link add br0 type bridge
    ip link set br0 up
else
    echo "Bridge br0 already exists."
fi

# Create virtual Ethernet pair veth0 and veth1 if they don't exist
if ! ip link show veth0; then
    echo "Creating virtual Ethernet pair veth0 and veth1"
    ip link add veth0 type veth peer name veth1
else
    echo "veth0 and veth1 already exist."
fi

# Attach veth0 to the bridge
echo "Attaching veth0 to br0 bridge"
ip link set veth0 master br0

# Bring up interfaces
echo "Bringing up the interfaces"
ip link set veth0 up
ip link set veth1 up

# Assign IP addresses (example)
echo "Assigning IP address to veth0"
ip addr add 172.16.50.1/24 dev veth0

# Output success message
echo "Fake network interfaces created successfully"
