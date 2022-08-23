Data Streaming Using Kafka
============

Mock stream producer for CSV data using Kafka. This repository is to support the OER course for the *PM 2.5 | Real Time streaming course*

Requires Docker and Docker Compose (Linux OS)

Installation
-------------------

Docker installation steps are available here: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

A summarized version can be followed below:

*Ubuntu (Linux)*

```
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
    
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

docker run hello-world (Test)

```

*Windows*

Executable file can be downloaded from [https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe]


Usage
-------------------

Clone repo and cd into directory.

```
git clone https://github.com/oer4sdi/spatial-streaming.git
cd spatial-streaming
```

**Start the Kafka broker**

```
docker compose up --build
```

**Build a Docker image (optionally, for the producer and consumer)**

From the main root directory:

```
docker build -t "kafkacsv" .
```

If you want to use Docker for the python scripts, this should now work:

```
docker run -it --rm --network=host kafkacsv python bin/sendStream.py data/sample.csv
```

**Start a consumer**

To start a consumer for printing all messages in real-time from the stream "pm25_stream":

```
docker run -it --rm --network=host -v {C:\path\to\spatial-streaming\}:/home kafkacsv python bin/processStream.py pm25_stream
```

**Shut down and clean up**

Stop the consumer with Return and Ctrl+C.

Shutdown Kafka broker system:

```
docker compose down
```
