FROM ubuntu:16.04
MAINTAINER Pwnpectf sapgan "admin@insignectf.in"
LABEL Description="CS628A CTF 2017 Web3" VERSION=1.0

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y apache2 php libapache2-mod-php php-mysql python


RUN a2enmod ssl
RUN mkdir /etc/apache2/ssl
RUN openssl req -new -x509 -nodes -days 365 -newkey rsa:2048 -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com" -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt

COPY default.conf /etc/apache2/sites-available/default-ssl.conf
COPY default.conf /etc/apache2/sites-enabled/ctf.conf
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN a2ensite default-ssl.conf
RUN service apache2 restart


COPY queries.sql /var/www
CMD mysql -u root < queries.sql
WORKDIR /var/www
COPY ./src /var/www/html

WORKDIR /var/www/html
RUN rm index.html
EXPOSE 443
CMD /usr/sbin/apache2ctl -D FOREGROUND
