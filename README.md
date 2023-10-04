# DevOpsTask

This is a simple python app runing flask framework that shows Hello, Devops! on url.
It is configured firstly to build and push Dockerfile to Docker Hub using Github Actions and upon any push changes, deploys to aws instance and start flask on port 5000. Port 80 is translated to 5000 dockerized image.
So any changes on name for example will build new Dockerfile, push to Docker Hub and after push it on AWS instance


Setup

Prerequisites on the server: Docker, python3, flask

Python3 is usually installed on Ubuntu server but if it isn’t:
Check if python is installed: python3 –-version
If not :  sudo apt install python3; sudo apt-get python3-pip

Install flask: pip3 install flask --user

Update the package index on your Ubuntu server: 
1. sudo apt update
2. sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
4. echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Install Docker:
1. sudo apt update
2. sudo apt install docker-ce docker-ce-cli containerd.io
3. sudo systemctl start docker
4. sudo systemctl enable docker
check Docker version: docker --version

Configure build and deploy:

In order for this to work in your environment, you must first setup secrets and variables in github repo settings -> action secrets and environments

secrets.DOCKERHUB_USERNAME -> Docker Hub username

secrets.DOCKERHUB_PASSWORD -> -> Docker Hub password

secrets.CLOUD_SSH_KEY -> ssh-keygen on the remote server (usually located in /home/user/.ssh folder) and cat id_rsa or however you named the key and paste it in secrets

secrets.SERVER_IP -> public ip address of the server

You should be able to access webpage on http://public_ip_address or dns_name
