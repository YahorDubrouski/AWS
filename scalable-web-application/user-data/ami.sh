#!/bin/bash

# Install Web Server
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd

# Install MySQL client
sudo dnf update -y
sudo dnf install -y https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
sudo dnf install -y mysql-community-client --nogpgcheck

# Add EC2 instance Info to index.html
echo "<h1>Yahor says Hello World from an instance $(hostname -f)</h1>" >> /var/www/html/index.html
