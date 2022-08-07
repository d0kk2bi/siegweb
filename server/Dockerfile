FROM ubuntu:20.04

# Change TimeZone
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# Update ubuntu
RUN apt update && apt upgrade -y

# Install python3
RUN apt install git python3 python3-pip -y

# Install pre-docker package
RUN apt install ca-certificates curl gnupg lsb-release -y

# Register docker GPG Key
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Register stable repository
RUN echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update ubuntu to download docker engines
RUN apt update -y

# Install docker engine
RUN apt install docker-ce docker-ce-cli containerd.io -y

# Install docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

# Copy server files
COPY server.py /server/server.py

# Clone CTFd
RUN git clone https://github.com/CTFd/CTFd.git /CTFd

# Change directory
WORKDIR "/CTFd"

# Server run
RUN docker-compose up
