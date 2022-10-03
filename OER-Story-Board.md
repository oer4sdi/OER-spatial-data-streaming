# OER on analyzing IoT air quality data streams using Kafka and Jupyter Notebooks  (work in progress!) x       


         	           	
## 1. Overview

In this open educational resource (OER) you will learn how to use Kafka and Jupyter notebooks to process and analyse streams of sensor data (particulate matter, PM2.5). After you have completed this tutorial, you will know how to

* use Docker to install and run Apache Kafka and Jupyter Notebooks on your local computer
* use Python to access and download PM2.5 sensor data from the Open Sensemap project
* simulate a PM2.5 sensor data stream that runs against Kafka and how to analyze that data stream for monitoring air quality

The module is structured as follows

1. Overview
2. Background on IoT, sensor data streams and the air quality parameter particulate matter (PM2.5)
3. Installing and using Apache Kafka and Jupyter Notebooks for analyzing PM2.5 data streams
4. Wrap up

If you are mainly interested in the technical aspects, you can jump directly to chapter 3 where we guide you through the technical exercise. With the help of some self-tests you can check if you have understood the essential concepts and technologies.

This tutorial is designed for students and professionals who want to spend about 90 minutes on improving their skills in developing applications based on real-time data. You should have some basic knowledge of Python and it wouldn't be bad if you already have some experience with Docker and Jupyter notebooks too. But don't worry, we will guide you through all those technologies and you can also use the tutorial to get your first hands-on experience with it.

This Tutorial has been developed at the Institute for Geoinformatics, University of Münster. Authors are Jaskaran Puri (main idea, technical tutorial) with contributions from Sandhya Rajendran, Thomas Kujawa and Albert Remke.

You are free to use, alter and reproduce the tutorial (H5P content) under the terms of the CC-BY-SA 4.0 license. Any code provided with the tutorial can be used under the terms of the MIT license. Please see the [full license terms](https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/LICENSE.md).

The OER4SDI project has been recommended by the Digital University NRW and is funded by the Ministry of Culture and Science NRW. 

## 2. Background on IoT and analyzing PM2.5 data streams

With the following slides we provide you with some context and background on processing streams of PM2.5 sensor data. 

### 2.1 read and learn...

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/P1_00_Overview.svg" width="1000">

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/P1_01_InternetOfThings.svg" width="1000">

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/P1_02_SensorThings.svg" width="1000">

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/P1_03_ProcessingSensorDataStreams.svg" width="1000">

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/P1_04_NRT_Applications.svg" width="!000">

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/P1_05_ApacheKafka.svg" width="1000">

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/P1_06_OpenSenseMap.svg" width="1000">


### 2.2 Test your knowledge
[
Quiz
Expected advantages of the IoT
Characteristics of streaming data
processing workflow (what needs to be done)
PM25 official thresholds
]

# 3. Installing and using Apache Kafka and Jupyter Notebooks for analyzing PM2.5 data streams

This section guides you through the installation and use of docker, kafka and jupyter notebooks for analyzing PM 2.5 data streams in real-time. It is important to note that this is a mock setup of a real-world scenario. The data itself and pulling mechanism is real-world and real-time, however, the component of streaming data using a jupyter notebook is an artificial setup with the aim to show how real-world data is transmitted and consumed in reality and how can we perform analytical functions over it. 

The tutorial is completed using three jupyter notebooks, in the order explained below:

> `src/step_1_data_prep.ipynb`: In this notebook you'll perform various tasks like code completion and map interactions. You'll then be able to pull live data from the Opensensemap APIs in real-time and store it locally

> `src/step_2_producer.ipynb`: This notebook represents a function that usually takes place within an IoT sensor like uploading/streaming of data to cloud. You'll be able to stream data in a kafka environment, however, just on your local PC where your own system acts like a cloud server

> `src/step_3_event_processing.ipynb`: Finally, the streamed data is retained in your docker's memory as it is waiting to be consumed by a `kafka consumer`. In this notebook you'll be able to pull this data and perform event detection and visualization for the same.

All the jupyter notebooks will run in a docker environment to enable dependency-free learning using the latest technologies.

In this chapter we will start with our implementation of the application from setting up the software environment to performing analytics with the data streams. Before we begin, there are few technical details you should be aware of to fully understand the functioning of this app. Here's an overall architecture of what the final flow of the app would look like.

<p align="center">
    <b>Here's one of the many possible designs (You can save it and zoom-in to view the captions)</b>
     <img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/archi_updated.png" width="1000"/>
</p>

The application itself isn't built using one specific programming language but is a result of multiple tools that are commonly used in while developing microservice architecture in cloud environments.

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

<p align="center">
     Here's a simple architecture of a Kafka system [[Source](http://cloudurable.com/blog/kafka-architecture/index.html)]
     <img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/kafka_archi.png" width="500">
</p>

- **Zookeeper:** Recently, zookeeper became an optional component but was the backbone for Kafka clusters for quite a few years. Zookeeper acts like a host on top of which Kafka brokers used to communicate, store metadata like topic names, ids etc. This component would know what servers are acting as brokers and spawns a new broker or leader in case one of the broker server fails. This component is more relevant in distributed systems where multiple servers are running in parallel.

This course introduces you to setting up zookeeper in a docker environment to show a mock setup of distributed applications.

### 3.1 Installing the SW environment

Now that we've gained some very basic knowledge about what each component does. Let's begin by setting up the software environment. To begin with, we will start by installing **Docker**

Installation
-------------------

To be able to run this application you need to setup `Docker` on your system as it provides you with a dependency free environment to work in. Docker installation steps are available here: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

The following operating systems are supported by Docker:

<li>Linux (All Variants)</li>
<li>Windows `(It is recommended to have at least 8GB RAM to support smooth functioning of Docker on Windows)`</li>
<li>Mac</li>


**Starting The Application**

Please ensure `docker` is up and running in background and open a relevant `Terminal/Command Prompt` in your OS.

[Download](https://github.com/oer4sdi/OER-spatial-data-streaming/archive/refs/heads/main.zip) the zipfile for the code and unzip it in a desired location

Advanced users can also clone it using `git` from [here](https://github.com/oer4sdi/OER-spatial-data-streaming) using the following command

```
git clone https://github.com/oer4sdi/OER-spatial-data-streaming.git
```

In your CMD/Terminal, enter this:

```
cd OER-spatial-data-streaming
docker compose up --build -d
```

On successfull run, you should see a similar console output

```
[+] Running 4/4
 - Network oer-spatial-data-streaming_default        Created                                                       1.5s
 - Container jupyter                                 Started                                                      12.2s
 - Container oer-spatial-data-streaming_zookeeper_1  Started                                                      12.2s
 - Container oer-spatial-data-streaming_kafka_1      Started                                                      14.2s
```
At this point, you should have all the three containers running: `zookeeper`, `kafka` and `jupyter`

### 3.2 Preparing the PM2.5 data stream

The data downloading/pre-processing can be done in an automated way using the `src/step_1_data_prep.ipynb` jupyter notebook. The data is fetched from the `Opensensemap API` available [here](https://docs.opensensemap.org/).

<p align="center">
     <b>The map canvas will look something like this</b>
     <img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/map.png" width="1000"/>
</p>

The following endpoints from the API are used and should not be modified:

```
sensebox_url = https://api.opensensemap.org/boxes
sensebox_data_url = https://api.opensensemap.org/statistics/descriptive
```

In the notebook, you will be required to peform few tasks to complete the data downloading process. You should first launch the jupyter notebook, this way we can work directly inside a docker environment.

To do this, open a new terminal/CMD window and enter the following command to get the URL of the hosted Jupyter Notebook

```
docker logs jupyter
```

Goto your browser and access the url that starts with `http://127.0.0.1:8888/?token=` (`token` should be available in the previous command output)

You should now start downloading the data from `src/step_1_data_prep.ipynb`

### 3.3 Using Kafka Producer To Stream Data

After downloading the data, you can choose to run the kafka producer jupyter notebook from `src/step_2_producer.ipynb`. 
On successfull run, you should see an output of messages confirming the transmission of data points.

### 3.4 Ingestion & Analysis On Streams of Data Using Kafka Consumer

Now you can  open `src/step_3_event_processing.ipynb` to read the kafka stream, perform event detection and geo-plotting. The jupyter notebook will guide you through the next steps. 

On successfull run, you should see an output map canvas showing locations of different senseboxes in your jupyter notebook

### 3.5 Shut down and clean up

Use `CTRL + C` or `docker-compse down` to exit the docker environment. Next time when you want to run the environment, you can just use `docker compose up -d`

Stop the consumer with Return and Ctrl+C.

Shutdown Kafka broker system:

```
docker compose down
```

## 4. Wrap up

This marks the end of the tutorial series on how to stream and process data using Kafka and Jupyter Notebooks. However, there are few points that should be highlighted

- In our mock scenario all messages are send in a bulk stream (more or less); nevertheless we have the time-stamps of the real observations.

- The consumer doesnt wait for messages but pulls data from the stream; this is different from what we  do with stream processors that may be triggered by incoming data within the Kafka environment.

- The data range used in the tutorial was older, however, in a real-world scenarios all the components would work as a single file and would not need to be triggered separately. The data pulled from API would trigger the producer at the same time. The consumer on other end would pull messages in regular intervals or in fact can also be kept in listening mode 24x7

By completing this series, you should've achieved some understanding about:

- The advantages of having access to any kind of data in real-time
- How real-time IoT sensors can be configured to stream data using Kafka
- How to perform analytics on a stream of data

**Interested In Learning More?**

Check out the following links to enhance your learning about these topics:

- IoT Messaging In Real-World: https://mqtt.org
- Kafka + MQTT Github: https://github.com/kaiwaehner/kafka-connect-iot-mqtt-connector-example
- GeMesa - BigData for GIS Applications: https://www.geomesa.org/assets/outreach/foss4g-2021-streaming-data.pdf
- Video On Real-Time Geospatial Analytics: https://www.youtube.com/watch?v=sa4RiH1RXEA&ab_channel=TheLinuxFoundation

**Your feedback is welcome!**

If you have identified shortcomings in this OER module or have ideas for improving the OER material, you are invited to add entries to the issue list in the [Github repository of this OER]( https://github.com/oer4sdi/OER-spatial-data-streaming).

