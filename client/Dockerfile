FROM ubuntu:20.04

# Copy client files
COPY client.py /client/client.py
COPY client.sql /client/client.sql

# Change TimeZone
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# Update ubuntu
RUN apt update && apt upgrade -y

# Install APM
RUN apt install apache2 mysql-server php php-common \
    php-mysql php-mbstring php-curl php-xml php-gd php-zip -y

# Install python3, crontab, vim
RUN apt install vim cron python3 python3-pip -y

# Install python3 package
RUN pip3 install pymysql

# Make flag directory & file
RUN mkdir /flag && touch /flag/flag

# Change client.py, client.sql mode
RUN chmod 600 /client/client.py /client/client.sql

# Set crontab 
RUN echo "0 */3 * * * /usr/bin/python3 /flag/client.py" >> /etc/crontab