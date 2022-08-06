FROM ubuntu:20.04

# Update ubuntu
RUN apt update && apt upgrade -y

# Install python3
RUN apt install git python3 python3-pip -y

# Clone CTFd
RUN git clone https://github.com/CTFd/CTFd.git

# Install requirements
RUN pip3 install -r CTFd/requirements.txt

