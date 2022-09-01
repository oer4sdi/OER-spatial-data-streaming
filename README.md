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

`(It is recommended to have at least 8GB RAM to support smooth functioning of Docker on Windows)`

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

**Input Data**

Samples from 10 random locations around Geramny for *Air Quality PM 2.5* were collected from [Opensensemap](https://opensensemap.org/) for August, 2022. Following is the distribution of these locations. We will use these points to interpolate the levels around Germany. The size of Red Marker signifies the amount of PM 2.5 recorded in that location. Total sample count is `30` as each location was recorded over `3 Days`

<img src="https://github.com/oer4sdi/spatial-streaming/blob/main/img/input_data.png" width="300"/>

**Event Detection & Spatial Interpolation**

You should first launch the jupyter notebook, this way we can work directly inside a docker environment
To do this, open a new terminal/CMD window and enter the following command to get the URL of the hosted Jupyter Notebook

```
docker-compose logs jupyter
```

Goto your browser and access the url that starts with `http://localhost:8888?token=` (`Token` should be available in the previous command output)

Once you're inside the Jupyter environment, `Goto New > Terminal`

*Install Python Libraries*

```
pip3 install -r requirements.txt
```

*Run Kafka Producer*

```
python bin/sendStream.py data/sample_multilocation.csv
```

The output on your jupyter terminal should look like this (30 Messages Sent)

<img src="https://github.com/oer4sdi/spatial-streaming/blob/main/img/terminal.png" width="600"/>

*Kafka Consumer & Analysis*

Now you can  open `bin/interpolation.ipynb` to read the kafka stream, perform event detection and spatial interpolation. The jupyter notebook will guide you through the next steps

Use `CTRL + C` or `docker-compse down` to exit the docker environment. 
Next time when you want to run the environment, you can just use `docker compose up -d`

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
| <img src="https://github.com/oer4sdi/spatial-streaming/blob/main/img/output_interpolated.png" width="300"/> | <img src="https://github.com/oer4sdi/spatial-streaming/blob/main/img/output_compared.png" width="300"/> |

**Shut down and clean up**

Stop the consumer with Return and Ctrl+C.

Shutdown Kafka broker system:

```
docker compose down
```
