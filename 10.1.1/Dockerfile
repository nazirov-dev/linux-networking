# Use an official Ubuntu image
FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install necessary packages
RUN apt-get update && apt-get install -y \
    iproute2 \
    net-tools \
    iputils-ping \
    sudo \
    bridge-utils \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the user "haad" with password "xavfsizlik"
RUN useradd -m -s /bin/bash haad && \
    echo "haad:xavfsizlik" | chpasswd

# Set the hostname directly in /etc/hostname
RUN echo "server01" > /etc/hostname

# Configure the hostname and network interface within the container
RUN hostname "server01" && \
    ip link add name br-5720f05dd68a type bridge && \
    ip addr add 172.16.50.1/24 dev br-5720f05dd68a && \
    ip link set br-5720f05dd68a up

# Set up the working directory and switch to the "haad" user
USER haad
WORKDIR /home/haad

# Default command to run in the container
CMD ["/bin/bash"]
