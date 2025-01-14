FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV HOSTNAME=server01

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    vim \
    iproute2 \
    net-tools \
    apache2 \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create user haady with the specified password
RUN useradd -m -s /bin/bash haady && \
    echo "haady:xavfsizlik" | chpasswd

# Set the container's hostname
RUN echo "server01" > /etc/hostname && \
    hostname -F /etc/hostname

# Create 19 network interfaces
RUN for i in $(seq 1 19); do ip link add name br-$i type bridge; done && \
    ip addr add 172.16.50.1/24 dev br-5720f05dd68a && \
    ip link set br-5720f05dd68a up

# Set the user to root temporarily to configure network interfaces
USER root
WORKDIR /root

# Switch to haady user for the default environment
USER haady
WORKDIR /home/haady

# Set default command to bash
CMD ["/bin/bash"]
