# DevOpsTask

This is a simple Python app flask-app/pythonapp.py running in Flask framework that shows Hello, Devops! on a url on a AWS EC2 instance. 

Upon any push changes, the Github Actions will be triggered and first it will build the image via Dockerfile in the repo and then it will push it to the Docker Hub .github/workflows/build-and-push-docker.yml using login credentials from GitHub Secrets environment. Then the deploy to AWS instance will be triggered and it will also start the container on port 80. Port 80 is mapped to port 5000 inside the running container. 
So any changes in a code for example will build new image, push that image to Docker Hub and after that it will deploy it on AWS instance.

Setup

Prerequisites on the server: Docker

Install Docker:

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

secrets.DOCKERHUB_PASSWORD -> Docker Hub password

secrets.CLOUD_SSH_KEY -> ssh-keygen on the remote server (usually located in /home/user/.ssh folder) and cat id_rsa or however you named the key and paste it in secrets

secrets.SERVER_IP -> public ip address of the server

You should be able to access webpage on http://public_ip_address or dns_name
