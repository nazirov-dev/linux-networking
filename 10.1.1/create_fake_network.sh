#!/bin/bash

# Step 1: Change the hostname to 'server01'
echo "Changing hostname to 'server01'"
echo "server01" | sudo tee /etc/hostname
echo "127.0.0.1   server01" | sudo tee -a /etc/hosts

# Step 2: Create 17 virtual interfaces and assign IPs
# 1. Create the first bridge interface with a random name
for i in $(seq 1 16); do
    random_string=$(openssl rand -hex 5)
    bridge_name="br-$random_string"
    echo "Creating virtual bridge interface $bridge_name"
    sudo ip link add name $bridge_name type bridge
    sudo ip addr add 172.16.50.$((i+1))/24 dev $bridge_name
    sudo ip link set $bridge_name up

    # Create virtual Ethernet pair veth$i and veth$((i+1))
    echo "Creating virtual Ethernet pair veth$i and veth$((i+1))"
    sudo ip link add veth$i type veth peer name veth$((i+1))

    # Attach veth$i to the created bridge
    echo "Attaching veth$i to $bridge_name bridge"
    sudo ip link set veth$i master $bridge_name

    # Bring up both interfaces
    echo "Bringing up veth$i and veth$((i+1))"
    sudo ip link set veth$i up
    sudo ip link set veth$((i+1)) up
done

# Step 3: Assign IP addresses to the interfaces if needed
echo "Assigning IP address to veth1"
sudo ip addr add 172.16.50.2/24 dev veth1

echo "Fake network interfaces created successfully"
