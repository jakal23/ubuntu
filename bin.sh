#!/bin/bash

# adding java ppa
sudo apt install software-properties-common
sudo add-apt-repository ppa:linuxuprising/java

sudo add-apt-repository ppa:inkscape.dev/stable

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list

# Add to sources Insomnia
echo "deb https://dl.bintray.com/getinsomnia/Insomnia /" | sudo tee -a /etc/apt/sources.list.d/insomnia.list
# Add public key used to verify code signature
wget --quiet -O - https://insomnia.rest/keys/debian-public.key.asc | sudo apt-key add -

curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

# Refresh repository sources
sudo apt-get update

# install
echo "--------------Install open jdk 8-------------------"
sudo apt install openjdk-8-jdk
echo "--------------Install open jdk 11-------------------"
sudo apt install oracle-java11-installer

java -version

sudo apt install clang
sudo apt install inkscape
sudo apt install sublime-text
sudo apt install insomnia
sudo apt-get install jenkins
sudo apt-get install -y aircrack-ng

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install code # or code-insiders

sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation

# Windows USB/DVD Download Tool allow you to easily create bootable DVD or USB Keys for Windows 7/8 installation from the ISO file downloaded from Microsoft Store
# wget https://codeplexarchive.blob.core.windows.net/archive/projects/wudt/wudt.zip

export WORKSPACE=/home/workspace
export ANDROID_HOME=$WORKSPACE/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64