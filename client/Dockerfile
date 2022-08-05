FROM ubuntu:20.04

# Change TimeZone
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# Update ubuntu
RUN apt update && apt upgrade -y

# Install python3, crontab
RUN apt install cron, python3 python3-pip -y

# Install python3 package
RUN pip3 install pymysql

# Make flag directory & file
RUN mkdir /flag && touch /flag/flag