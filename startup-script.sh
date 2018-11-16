#!/bin/bash

echo "Hello computer user !!!"

yum -y install httpd mod_ssl
systemctl enable httpd
systemctl start httpd

