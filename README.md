# rpi-ioexpander - Demo with MCP23018-E/SP , fastAPI, GPIO, i2C
https://www.digikey.ca/en/products/detail/microchip-technology/MCP23018-E-SP/1999505

https://www.digikey.ca/en/products/detail/texas-instruments/CD40109BE/376604

# Set Up Headless Pi
## SD Card
- SDCardFormatter -> Quick Format the SD Card
- Rasperry Pi Imager -> Install Raspbian onto SD Card
- In "boot" directort, 
  - add a file called SSH
  - Add "ip=192.168.x.x" to the end of the line in cmdline.txt

## Run Config
    sudo raspi-config

- WiFi region, ssid, passphrase 
- Interface ... Turn on i2C, SPI

### Network Interface Stuff...
    sudo nano /etc/dhcpcd.conf

    interface eth0
    static ip_address=192.168.x.x/24
    metric 400  --> Higher priority means lower number.

### install python
    sudo apt update
    sudo apt install python3

### install git
    sudo apt install git

### Run docker install script
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker $USER
    # When you do a reboot, you can just type docker ---.
    # Alternatively, to make it work in your current session, just type
    newgrp docker

### Check if docker is installed correctly
    sudo docker run hello-world

### prepare for project, clone this repo, point to new repo.
    mkdir myproject
    git clone https://github.com/djoha/rpicontainer.git
    git remote set-url origin https://github.com/user/newrepo.git

# Editor
## Open VS COde
Make sure Remote-SSH Extension is installed

 - Crtl+Shift+P
 - Remote-SSH: Connect To Host
 - pi@192.168.x.x
 - Choose OS (Linux)
 - Enter Password (default: raspberry)

## Click "Open Folder"... navigate to repo.
Note the project structure

    .
    ├── app
    │   ├── __init__.py
    │   └── main.py
    ├── Dockerfile
    └── requirements.txt

# Run the Container

## Build the Image: First time takes a while
    sudo docker build -t myimage .

## Run the container.  Make sure port matches Dockerfile
    sudo docker run -d --name mycontainer -p 80:80 --restart unless-stopped --privileged myimage

## Stop
    sudo docker stop mycontainer
## Remove
    sudo docker rm mycontainer

## Check Logs for Trouble Shooting:
    tail -f /var/log/syslog
    sudo docker logs mycontainer

## Check docs page:
    http://192.168.x.x:80/docs
