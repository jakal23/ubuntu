#!/bin/bash

# adding java ppa
sudo apt install software-properties-common
sudo add-apt-repository ppa:linuxuprising/java

# Add to sources Jenkins
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
# Add public key used to verify code signature
echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list

# Refresh repository sources
sudo apt-get update

# install
echo "--------------Install open jdk 8-------------------"
sudo apt install openjdk-8-jdk -y
echo "--------------Install open jdk 11-------------------"
sudo apt install oracle-java11-installer -y

java -version

echo "--------------Install sensors package-------------------"
sudo apt install lm-sensors -y

echo "--------------Install Git package-------------------"
sudo apt-get install git -y

sudo apt install jenkins -y
sudo apt install hardinfo -y
sudo apt install -y aircrack-ng
sudo apt install phpmyadmin php-mbstring php-gettext -y

echo "--------------Install Codec pack packages package-------------------"
sudo apt install libdvdnav4 libdvdread4 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libdvd-pkg
sudo apt install ubuntu-restricted-extras

echo "--------------Install Youtube-dl package-------------------"
sudo wget https://yt-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+x /usr/local/bin/youtube-dl
hash -r

sudo apt-get install apt-transport-https

sudo apt update
sudo apt install mysql-server -y
sudo mysql_secure_installation
