FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV HOSTNAME=server01
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    vim \
    iproute2 \
    net-tools \
    apache2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash haady && \
    echo "haady:xavfsizlik" | chpasswd 

USER root
WORKDIR /root
RUN for i in $(seq 1 19); do ip link add name br-$i type bridge; done && \
    ip addr add 172.16.50.1/24 dev br-5720f05dd68a && \
    ip link set br-5720f05dd68a up

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]