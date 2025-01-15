#!/bin/bash

# Step 1: Change the hostname to 'server01'
echo "Changing hostname to 'server01'"
echo "server01" | sudo tee /etc/hostname
echo "127.0.0.1   server01" | sudo tee -a /etc/hosts

# Step 2: Create 17 virtual interfaces and assign IPs
# 1. Create the first bridge interface br-5720f05dd68a
echo "Creating virtual bridge interface br-5720f05dd68a"
sudo ip link add name br-5720f05dd68a type bridge
sudo ip addr add 172.16.50.1/24 dev br-5720f05dd68a
sudo ip link set br-5720f05dd68a up

# 2. Create virtual Ethernet pairs (vethX and vethY) and attach them to the bridge
for i in $(seq 1 16); do
    # Create virtual Ethernet pair veth$i and veth$((i+1))
    echo "Creating virtual Ethernet pair veth$i and veth$((i+1))"
    sudo ip link add veth$i type veth peer name veth$((i+1))

    # Attach veth$i to br-5720f05dd68a bridge
    echo "Attaching veth$i to br-5720f05dd68a bridge"
    sudo ip link set veth$i master br-5720f05dd68a

    # Bring up both interfaces
    echo "Bringing up veth$i and veth$((i+1))"
    sudo ip link set veth$i up
    sudo ip link set veth$((i+1)) up
done

# Step 3: Assign IP addresses to the interfaces if needed
echo "Assigning IP address to veth1"
sudo ip addr add 172.16.50.2/24 dev veth1

echo "Fake network interfaces created successfully"
