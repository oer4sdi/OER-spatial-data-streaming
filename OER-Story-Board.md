# OER on analyzing IoT air quality data streams using Kafka and Jupyter Notebooks  (work in progress!)        


         	           	
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

# 3. Installing and using Apache Kafka and Jupyter Notebooks for analyzing PM 2.5 data streams

This section guides you through the installation and use of Docker, Kafka and Jupyter Notebooks for analyzing PM 2.5 data streams. 

[Architecture diagram]

Software components used in this tutorial

* **Docker** allows us to package all needed software components as Docker Images and execute those images as Docker Containers in the Docker Environment, e.g. on Linux, Windows or Mac. With the docker-compose tool we can define multiple docker images and configure how they communicate with each other.

* **Apache Kafka** is a messaging system. Kafka is used for applications which need to ingest, process and disseminate huge amounts of incoming data with millisecond latency. Kafka is conceptually based on a publish-subscribe architecture where one type of systems (**Producers**) publish topic-related messages at a virtual **Broker** and other types of systems (**Consumers**) subscribe to those topics, filter, access and use those messages for real-time applications. The Topics are useful to structure the data streams and to support scaling of the Kafka system. The broker acts as the bridge between producers and consumers. The broker also acts as message store, where messages can wait to be consumed by a consumer app.

* Recently, **Zookeeper** became an optional component, but for some years it was the backbone for Kafka clusters. Zookeeper is used to coordinate clusters of Kafka brokers. For example, Zookeeper "knows" which servers act as brokers and creates a new broker if one of the brokers fails.

* **Jupyter Notebook** is an interactive web-based environment for creating and using Notebook documents. It implements the reed-eval-print-loop (REPL), i.e., each document can have a sequence of input/output cells which may contain multimedia content or executable code (Python, R, Julia). Once the user activates a code cell, the print-output of the code will be inserted into the document. This supports both, describing a method or workflow, which involves code and direct interaction with the code as to learn and understand, how the code works. Following a common practice, our Notebook Documents have the extension ".ipynb".

We use docker to build and run three containers: 

* The **Jupyter container** runs the Jupyter Notebook server. We’ll use three Jupyter Notebooks to implement and explain the software that is needed to support Step-1, Step-2 and Step-3 of our technical exercise.

* The **Kafka Container** runs the Kafka Broker, that receives the sensor data, stores them in a temporal data store and provides access to the data for consumer apps. 

* The third container runs **zookeeper**, that coordinates the Kafka cluster.

In our exercise, we will first download PM 2.5 sensor data from the openSenseMap project (Step-1). In a second step we will use this sample data to create a sensor data stream that is sent to a Kafka broker by a producer app (Step-2). Finally, we will show, how to analyze and visualize the PM 2.5 data by a consumer app (Step-3). 

Please notice: In this exercise, we simplify a real-world scenario where many sensors (producer apps) would continuously send their data to the broker. Many consumer apps would sign up for topics of their interest, access the corresponding data in either push or pull mode and process the data in near real-time.






### 3.1 Installing the SW environment

Now that we've gained some understanding of the workflow and the technologies involved, let's set up the software environment. 


#### Installing Docker

To begin with, we will start by installing Docker. Please go to the official web site [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/) and follow the guidance which is provided there to install docker on your local computer (Linux, Windows or Mac). It is recommended to have at least 8GB RAM to support smooth functioning of Docker.

#### Starting The containers 

Please ensure `docker` is up and running in background and open a `Terminal/Command Prompt` in your OS.

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

