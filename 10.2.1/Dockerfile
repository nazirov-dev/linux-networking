FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    iproute2 \
    net-tools \
    iputils-ping \
    sudo \
    bridge-utils \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash haady && \
    echo "haady:xavfsizlik" | chpasswd

# Copy Python scripts to container
COPY listener.py /var/tmp/listener.py
COPY 555.py /var/tmp/555.py
COPY 456.py /var/tmp/456.py
# Allow haady to run 555.py as root without a password
RUN echo "haady ALL=(ALL) NOPASSWD: /var/tmp/555.py" >> /etc/sudoers.d/haady
RUN echo "haady ALL=(ALL) NOPASSWD: /var/tmp/listener.py" >> /etc/sudoers.d/haady

# Allow haady to run ss as root without a password
RUN echo "haady ALL=(ALL) NOPASSWD: /usr/bin/ss -natup" >> /etc/sudoers.d/haady
RUN echo "haady ALL=(ALL) NOPASSWD: /usr/bin/ss" >> /etc/sudoers.d/haady


# Add the command to execute listener.py & run the Python script via sudo
RUN echo "sudo /var/tmp/listener.py &" >> /home/haady/.bashrc
RUN echo "sudo /var/tmp/555.py &" >> /home/haady/.bashrc
RUN echo "python3 /var/tmp/456.py &" >> /home/haady/.bashrc

# Ensure executable permissions on the scripts
RUN chmod +x /var/tmp/555.py /var/tmp/listener.py /var/tmp/456.py /var/tmp/555.py

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]