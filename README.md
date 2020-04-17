# Install_bulk_pytthon_packages_docker
Install bulk python packages in docker image


1. Created EC2 instance 
	- Ubuntu 18.04 AMI
2. Login EC2 using Putty and PPK file
	- Created and Download PEM file while creating EC2 instance
	- Converted PEM to PPK using PuttyGen
	- Login using Putty with Public IP (getting new IP for every restart)
	- Default user is ubuntu
	- Changed root password (will provide in seperate file)
		- sudo su
		- passwd root
		- enter new password
3. Install Docker on Ubuntu EC2 instance - https://docs.docker.com/engine/install/ubuntu/
	- sudo apt-get update
	- sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
	- sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
	- apt-get update
	- apt-get install docker-ce docker-ce-cli containerd.io
	- docker run hello-world

4. Create and RUN Docker file to create Dockr Image (project path - /home/ubuntu/Docker_project)
	- Created requirements.txt with listed packages in given excel sheet
	- Created pyhton script
		- Read each package name in requirements.txt 
		- Install the package and capture the error to /data/error.log file inside container
	- docker login
	- docker build -t suneelmallela/install_bulk_python_packages_docker .
4. Push Docker Image to ECR
	- docker push suneelmallela/install_bulk_python_packages_docker
	- This image is in your dockerhub account (please make this a private if required)
5. How to use the Image
	- docker run suneelmallela/install_bulk_python_packages_docker
	- docker run -it suneelmallela/install_bulk_python_packages_docker bash
	- exit
	- docker ps -a
	- note recent continer id 
	- docker start container id
	- docker cp <container id>:/data/error.log /data/<c_id>_error.log
	- docker stop <container id>
	- See error.log in your local system
