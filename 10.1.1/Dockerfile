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

# Add "haady" to sudoers group
RUN usermod -aG sudo haady

# Copy the fake network setup script into the container
COPY create_fake_network.sh /home/haady/

# Make the script executable
RUN chmod +x /home/haady/create_fake_network.sh

# Run the script as root during the build process to set up the fake network
RUN /home/haady/create_fake_network.sh

# Ensure the script is also executed when "haady" logs in
RUN echo "/home/haady/create_fake_network.sh" >> /home/haady/.bashrc

# Set up the working directory and switch to the "haady" user
USER haady
WORKDIR /home/haady

# Default command to run in the container
CMD ["/bin/bash"]