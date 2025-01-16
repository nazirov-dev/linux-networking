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

    

COPY listener.py /var/tmp/listener.py
COPY 555.py /var/tmp/555.py

RUN echo "haady ALL=(ALL) NOPASSWD: /var/tmp/555.py" >> /etc/sudoers.d/haady

RUN echo "python3 /var/tmp/listener.py &" >> /home/haady/.bashrc
RUN echo "echo \"xavfsizlik\" | sudo -S python3 /var/tmp/555.py" >> /home/haady/.bashrc

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]