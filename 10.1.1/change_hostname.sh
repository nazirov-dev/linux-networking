#!/bin/bash

# Hostname ni o'zgartirish
hostnamectl set-hostname server01

# Interfeyslarni yaratish
for i in {1..19}; do
    ip link add br-5720f05dd68a.$i type bridge
    ip addr add 172.16.50.1/24 brd 172.16.50.255 dev br-5720f05dd68a.$i
    ip link set br-5720f05dd68a.$i up
done
