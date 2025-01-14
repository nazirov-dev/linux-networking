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

# Create the user "haady" with password "xavfsizlik"
RUN useradd -m -s /bin/bash haady && \
    echo "haady:xavfsizlik" | chpasswd

# Copy the change_hostname.sh script
COPY change_hostname.sh /home/haady/
RUN chmod +x /home/haady/change_hostname.sh && \
    echo "/home/haady/change_hostname.sh" >> /home/haady/.bashrc

# Set up the working directory and switch to the "haady" user
USER haady
WORKDIR /home/haady

# Default command to run in the container
CMD ["/bin/bash"]