#!/bin/bash

# Step 1: Create 19 virtual interfaces with random names
# 1. Create the first bridge interface br-5720f05dd68a
echo "Creating virtual bridge interface br-5720f05dd68a"
sudo ip link add name br-5720f05dd68a type bridge
sudo ip addr add 172.16.50.1/24 dev br-5720f05dd68a
sudo ip link set br-5720f05dd68a up

# 2. Create virtual Ethernet pairs (veth{random-string} and veth{random-string}) and attach them to the bridge
for i in $(seq 1 8); do
    # Generate random strings for interface names using /dev/urandom
    random_veth1="veth$(head /dev/urandom | tr -dc a-f0-9 | head -c 8)"
    random_veth2="veth$(head /dev/urandom | tr -dc a-f0-9 | head -c 8)"

    # Create virtual Ethernet pair with random names
    echo "Creating virtual Ethernet pair $random_veth1 and $random_veth2"
    sudo ip link add $random_veth1 type veth peer name $random_veth2

    # Attach the first interface to the bridge
    echo "Attaching $random_veth1 to br-5720f05dd68a bridge"
    sudo ip link set $random_veth1 master br-5720f05dd68a

    # Bring up both interfaces
    echo "Bringing up $random_veth1 and $random_veth2"
    sudo ip link set $random_veth1 up
    sudo ip link set $random_veth2 up
done