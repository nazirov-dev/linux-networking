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

# Set the hostname by modifying /etc/hostname and /etc/hosts
RUN echo "server01" > /etc/hostname && \
    echo "127.0.0.1 server01" >> /etc/hosts

# Create network interface setup (simulate this since Docker doesn't allow bridge interface creation during build)
RUN ip link add name br-5720f05dd68a type bridge && \
    ip addr add 172.16.50.1/24 dev br-5720f05dd68a && \
    ip link set br-5720f05dd68a up

# Set up the working directory and switch to the "haad" user
USER haad
WORKDIR /home/haad

# Default command to run in the container
CMD ["/bin/bash"]
