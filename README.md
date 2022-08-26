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

docker run hello-world

```

*Windows*

Executable file can be downloaded from [https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe]


Usage
-------------------

Please ensure `docker` is up and running in background

Open a relevant `Terminal/Command Prompt` in your OS

Clone repo and cd into directory.

```
git clone https://github.com/oer4sdi/spatial-streaming.git
cd spatial-streaming
```

**Start the Kafka broker** (To be run in a separate CMD/Terminal as it should be running in background)

```
cd spatial-streaming
docker compose up --build
```

**Build a Docker image**

From the main root directory:
Open a separate `CMD/Terminal`

```
cd spatial-streaming
docker build -t "oerkafka" .
```

**Input Data**

Samples from 10 random locations around Geramny for *Air Quality PM 2.5* were collected from [Opensensemap](https://opensensemap.org/) for August, 2022. Following is the distribution. We will use these points to interpolate the levels around Germany. The size of Red Marker signifies the amount of PM 2.5 recorded in that location.

<img src="https://github.com/oer4sdi/spatial-streaming/blob/main/img/input_data.png" width="300"/>

**Run Kafka Producer**

```
docker run -it --rm --network=host oerkafka python bin/sendStream.py data/sample_multilocation.csv
```

**Start Kafka Consumer**

To start a consumer for printing all messages in real-time from the stream "pm25_stream":

```
(Windows)
docker run -it -exec --network=host -v C:\path\to\spatial-streaming:/home oerkafka python bin/processStream.py

(Linux)
docker run -it -exec --network=host -v $(pwd):/home oerkafka bash
```

(Now you're working inside a terminal of the Docker Container)
Run The Following To Launch a Jupyter Notebook


```
(Windows)
docker run -it -exec -p 8888:8888 -v C:\path\to\spatial-streaming:/home oerkafka bash

(Linux)
docker run -it -exec -p 8888:8888 -v $(pwd):/home oerkafka bash

jupyter notebook --ip '*' --port 8888 --allow-root --no-browser
```

GoTo your browser and access `http://localhost:8888?token=` and access `interpolation.ipynb`
(`Token` should be available in the previous command output)

Use `exit` to exit the docker shell

**Results**

The following files should be generated from the Jupyter Notebook
```
- interpolated_rectangular.tif
- interpolated_cropped.shp (Optional)
```

You can use GIS processing tools like QGIS/ArcGIS Pro to crop the `interpolated_rectangular.tif` using `germany_simplified.shp`
A pre-generated output is already available in `data/interpolated_cropped.tif`

| Interpolated Output | Input Overlayed |
| --------------- | --------------- |
|  |  |

**Shut down and clean up**

Stop the consumer with Return and Ctrl+C.

Shutdown Kafka broker system:

```
docker compose down
```
