# OER on analyzing IoT air quality data streams using Kafka and Jupyter Notebooks          
Storyboard
[In square brackets: suggested content and related comments]



## Table of Content
1. Overview	
2. Background on IoT and analyzing PM2.5 data streams	
     2.1 IoT and Sensor Things	
     2.2 Analyzing near real-time data streams	
     2.3 Stream processing with Apache Kafka	
     2.4 Air Quality and PM2.5	
     2.5 Test your knowledge	
3. Tutorial on Analyzing PM2.5 data streams with Jupyter Notebooks	
     3.1 Installing the SW environment	
     3.2 Preparing the PM2.5 data stream	
     3.3 Preparing the PM2.5 monitor	
     3.4 Test your knowledge	
4. Wrap up



         	           	
## 1. Overview
[
Abstract
Learning Objectives
Learning activities
Overview on the structure of the learning material
How to use the learning material
Target Group and required knowledge
Authors reference
License reference
Funding reference
 ]

In this course, you’ll learn how to use Kafka and Jupyter Notebooks (Python) to access and analyze data streams coming from IoT devices that provide air quality data (e.g. PM2.5 sensor data). 

You will
* use docker to install Kafka, Jupyter and a Python notebook on your local computer
* use PM2.5 sensor data from the Open Sensemap project 
* use Jupyter notebooks to run Python scripts for simulating IoT data streams and for analyzing those data

In Chapter 2 we’ll provide you with background on the Internet of Things (IoT), processing of data streams and on Particulate Matter (PM2.5). 
If you are mainly interested in the technical aspects, you can jump directly to chapter 3, where we guide you through the installation and use of Kafka and Jupyter notebooks to manage and process PM2.5 data streams.

With the help of some self-tests, you can check whether you have understood the essential concepts and technologies.  

We designed the course to be used by students and professionals who want to improve their skills in developing applications for near-real-time data. You should have some basic knowledge of Python and it wouldn't be bad if you already have some experience with Docker and Jupyter notebooks too. But don't worry, we will guide you through all those technologies and you can also use the tutorial to get your first hands-on experience with it. 

This Tutorial has been developed at the Institute for Geoinformatics, University of Münster. Authors are Jaskaran Puri (main idea, technical tutorial) with contributions from Sandhya Rajendran, Thomas Kujawa and Albert Remke.

You are free to use, alter and reproduce the tutorial (H5P content) under the terms of the CC-BY-SA 4.0 license. The source code can be used under the terms of the MIT license [link]. 

The OER4SDI project has been recommended by the Digital University NRW and is funded by the Ministry of Culture and Science NRW. 
 
[@Thomas: see MKW funding notice for obligations on how to reference the funding authorities (text, ogo)]

## 2. Background on IoT and analyzing PM2.5 data streams

[What this chapter is about]
                              	
### 2.1 IoT and Sensor Things

[
Contect/objective: understanding the concepts: IoT, Sensors
Content
About IoT (vision, brief definition, Internet of Things, WebOfThings, Geospatial WebOfThings
Nature and capabilities of Things (physical/virtual, identity, sensing, processing, acting, communication, ..)
Sensor things (specifics)
Communication with sensor things (connectivity, pattern: pull/push, streaming)
Typical IoT sensor network architectures (sensors, platforms)
Real-world applications
Example in more detail: open SenseBox and OpenSenseMap
]

### 2.2 Analyzing near real-time data streams

[
Context/objective: Understanding the notion of stream processing
content
stream processing: definition, characteristics, basis for near real-time applications
Use cases:
monitoring the current state
detecting events
forecasting, ..
Selected use case in detail
Monitoring air quality
processes: data access, data preparation, event detection, presentation
challenges: data quality, outages, trust, ..
]  

              	
### 2.3 Stream processing with Apache Kafka
[
context/objective: Understanding, how Apache Kafka supports stream processing
content 
Overview on the functionality (ETL aspects): data access, filtering, storing, data provision
Overview on the logical compnents: producer, broker, topics, comsumer..
]

### 2.4 Air Quality and PM2.5

[
Context and relevance of air quality
Particular matter(definition, health risks)
PM25 (definition, official air quality thresholds)
How to measure PM25 (sensors, sensor placements)
]

### 2.5 Test your knowledge
[
Quiz
Expected advantages of the IoT
Characteristics of streaming data
processing workflow (what needs to be done)
PM25 official thresholds
]

# Chapter 3: Tutorial on Analyzing PM2.5 data streams with Jupyter Notebooks

In this chapter we will start with our implementation of the application from setting up the software environment to performing analytics with the data streams. Before we begin, there are few technical details you should be aware of to fully understand the functioning of this app.

The application itself isn't built using one specific programming language but is a result of multiple tools that are commonly used in while developing microservice architecture in cloud environments.

Let's begin with what is a microservice architecture. In short, when independent tools are able to communicate with each other through APIs to make a single application function, we can label it as a microservice app. The major advantage here is of the independent nature of the multiple tools that allow additional control over each of the components, better fault-tolerance and improved scalability.

Coming back to our application which includes the following components:

1. Docker
2. Kafka
3. Zookeeper
4. Jupyter/Python Environment

Here's a few more details about each of the components:

- **Docker:** A very commonly used technology that allows running of applications irrespective of the host environment/dependencies. An application developed using tools that are only available in linux for example can be packaged into a, what we call as a **Docker Image** and then execute is image on any other system for example even Windows.

Every time you execute a Docker Image, it gets converted one docker container, which means the application itself. In the case like ours where we have more than one independent components or Docker Images that we'll require, it is recommended to use what we call as a **docker-compose** tool. Using this you can define multiple docker images in a single file and also configure how they communicate with each other.

- **Kafka:** Officially known as Apache Kafka, in simpler terms is a messaging system. Kafka is mostly useful for applications where there is a need to ingest huge amount of incoming data with millisecond latency. Kafka is conceptually based on a publish-subscribe architecture where one system is responsible to publish message to a virtual "broker" while some systems are responsible for consuming the messages, also known as consumers because they subscribe to the broker. Here are the components that you should be aware of:

     - **Producer:** The component responsible to send a message to the Kafka cluster under a certain topic

     - **Consumer:** The component responsible to receive message from the Kafka cluster. A consumer would subscribe to a certain topic and receive messages for this topic only

     - **Topic:** Any message that is produced will always be tagged with a specific topic or a keyword. Technically, topics help in scaling the Kafka system, however, in our application a topic can be seen as a way to organise messages. This can be named anything.

     - **Broker:** This component acts as the bridge between producer and consumer. You can think of this as a storage space for Kafka, messages are stored by this component, waiting to be consumed by a consumer component

<img src="https://miro.medium.com/max/795/1*HdrdFds-0W6KW9Hw0UP96w.png" width="250">
*Here's a simple architecture of a Kafka system*

```
A real-world replica of this model would be your mail/letterbox.

**Post-Man:** This guy is the producer, whose job is just to pick data and drop it in your mailbox
**Mail/Letter Box:** This is your broker, the letters will keep piling up if no one comes to collect it.
**Your Address:** This is your topic, how does the post-man know where to send this data?
**You:** You are the consumer, it’s your responsibility to collect this data and process it further
```

- **Zookeeper:** Recently, zookeeper became an optional component but was the backbone for Kafka clusters for quite a few years. Zookeeper acts like a host on top of which Kafka brokers used to communicate, store metadata like topic names, ids etc. This component would know what servers are acting as brokers and spawns a new broker or leader in case one of the broker server fails. This component is more relevant in distributed systems where multiple servers are running in parallel.

This course introduces you to setting up zookeeper in a docker environment to show a mock setup of distributed applications.

### 3.1 Installing the SW environment

Now that we've gained some very basic knowledge about what each component does. Let's begin by setting up the software environment. To begin with, we will start by installing **Docker**

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

### 3.2 Preparing the PM2.5 data stream

Samples from 10 random locations around Geramny for *Air Quality PM 2.5* were collected from [Opensensemap](https://opensensemap.org/) for August, 2022. Following is the distribution of these locations. We will use these points to interpolate the levels around Germany. The size of Red Marker signifies the amount of PM 2.5 recorded in that location. Total sample count is `30` as each location was recorded over `3 Days`

<img src="https://github.com/oer4sdi/spatial-streaming/blob/main/img/input_data.png" width="300"/>

### 3.3 Processing the PM2.5 data stream

Before developing an application it is always recommended to draw an architecture diagram to understand how different components would interact with each other, what would be the data flow etc. There's no one right architecture as it is possible to design and place the same components in several different ways. What do you think would be good architecture for our application?

Here's one of the many possible designs (You can save it and zoom-in to view the captions)

<img src="https://github.com/oer4sdi/spatial-streaming/blob/main/img/archi.png" width="300"/>

**Using The Application**

Please ensure `docker` is up and running in background and open a relevant `Terminal/Command Prompt` in your OS
(Download)[https://github.com/oer4sdi/spatial-streaming/archive/refs/heads/main.zip] the zipfile for the code and unzip it in a desired location

Advanced users can also clone it using `git` from (here)[https://github.com/oer4sdi/spatial-streaming] using the following command

```
git clone https://github.com/oer4sdi/spatial-streaming.git
```

In your CMD/Terminal, enter this:

```
cd spatial-streaming
```

**Change Docker Path**

Before proceeding further, please change the path `C:/path/to/spatial-streaming/:/home` in `docker-compose.yml` to the location where you cloned this repo in your system.

**Start the Kafka broker** (To be run in a separate CMD/Terminal as it should be running in background)

```
cd spatial-streaming
docker compose up --build 
```

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


### 3.4 Test your knowledge
[Quiz - tbd]


## 4. Wrap up
[
Brief summary of the expected learning outcomes (2-3 sentences)
Links to further OER that might be interesting to deepen the knowledge in certain fields
Invitation to contribute by providing FeedBack, info on how to do so..
Funding reference
]

