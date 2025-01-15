#!/bin/bash

# Step 1: Create 19 virtual interfaces with random names

# 2. Create virtual Ethernet pairs (veth{random-string} and veth{random-string}) and attach them to the bridge
for i in $(seq 1 9); do
    # Generate random strings for interface names using /dev/urandom
    random_veth1="veth$(head /dev/urandom | tr -dc a-f0-9 | head -c 8)"
    random_veth2="veth$(head /dev/urandom | tr -dc a-f0-9 | head -c 8)"

    # Create virtual Ethernet pair with random names
    sudo ip link add $random_veth1 type veth peer name $random_veth2

    # Attach the first interface to the bridge
    sudo ip link set $random_veth1 master br-5720f05dd68a

    # Bring up both interfaces
    sudo ip link set $random_veth1 up
    sudo ip link set $random_veth2 up
    if [ $i -eq 4 ]; then
        sudo ip link add name br-5720f05dd68a type bridge
        sudo ip addr add 172.16.50.1/24 dev br-5720f05dd68a
        sudo ip link set br-5720f05dd68a up
    fi
done