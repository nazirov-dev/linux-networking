FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install necessary packages
RUN apt-get update && apt-get install -y \
    iproute2 \
    net-tools \
    iputils-ping \
    sudo \
    curl \
    bridge-utils \
    vim \
    python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the user "haady" with password "xavfsizlik"
RUN useradd -m -s /bin/bash haady && \
    echo "haady:xavfsizlik" | chpasswd

RUN usermod -aG sudo haady

# Copy the fake network setup script into the container

COPY server.py /var/tmp/server.py
RUN chmod +x /var/tmp/server.py

COPY create_fake_network.sh /var/tmp/create_fake_network.sh
RUN touch /home/haady/.sudo_as_admin_successful
# Make the script executable
RUN chmod +x /var/tmp/create_fake_network.sh

# Add the script to .bashrc so it runs when the user logs in
RUN echo "/var/tmp/create_fake_network.sh" >> /root/.bashrc && \
    echo "python3 /var/tmp/server.py &" >> /root/.bashrc && \
    echo "cd /home/haady" >> /root/.bashrc && \
    echo "su haady" >> /root/.bashrc && \
    echo "clear" >> /root/.bashrc
# Set up the working directory and switch to the "haady" user
USER root
WORKDIR /root
# Default command to run in the container
CMD ["/bin/bash"]
