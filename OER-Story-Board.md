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


## 2. Background on the IoT and the analysis of PM2.5 data streams

With the following slides we provide you with some context and background on processing streams of PM 2.5 sensor data. 

### 2.1 Read and learn...

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

<img src="https://github.com/oer4sdi/OER-spatial-data-streaming/blob/main/img/OER Streaming Architecture.svg" width="1000">

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


#### A) Installing Docker

To begin with, we will start by installing Docker. Please go to the official web site [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/) and follow the guidance which is provided there to install docker on your local computer (Linux, Windows or Mac). It is recommended to have at least 8GB RAM to support smooth functioning of Docker.

#### B) Downloading the sources from GitHub

[Download](https://github.com/oer4sdi/OER-spatial-data-streaming/archive/refs/heads/main.zip) the zipfile for the code and unzip it in a location you want to use as a **Working Directory**.

Advanced users can also clone it using `git` from [here](https://github.com/oer4sdi/OER-spatial-data-streaming) using the following command

```
git clone https://github.com/oer4sdi/OER-spatial-data-streaming.git
```


#### C) Starting The containers 

Please ensure `docker` is up and running in background and open a `CMD/Terminal` in your OS.

At the command prompt, change to the Working Directory (e.g. "OER-spatial-data-streaming-main") and start up the docker containers:

```
cd OER-spatial-data-streaming-main
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

### 3.2 Downloading the PM 2.5 sample data set (Step-1)

As a first step, we want to download PM 2.5 sensor data from the [openSenseMap project](https://docs.opensensemap.org/) and we will use our first Jupyter Notebook document to perform this task.

As to get the URL of the Jupyter Notebook server, open a new `CMD/Terminal` window and enter the following command: 

```
docker logs jupyter
```

The output should look like this:
[Jupyter_logsScreen]

Goto your browser and access the URL that starts with `http://127.0.0.1:8888/?token=` (please take the `token` from the previous command output).

You will see the UI of the Jupyter Notebook server which informs you about the files that are available and the documents that are currently running. Please open the folder “src” to see the three Notebook documents that are prepared for our exercise. 

[Jupyter-UI]

Please start the first Notebook document `src/step_1_data_prep.ipynb` and activate the sequence of cells of the document one by one. In the document, you will be required to perform a few tasks to complete the data downloading process.

Please be aware:
* Some of the code cells need some time to complete the computing, i.e., please wait for the output before you continue with the next cell. 
* Each cell works with the current state of the system, which is a result of the code and data that has been activated before. I.e., the order in which you activate cells matters. If you are not sure about the state of the system, please re-initialize the system by re-starting the kernel (see buttons in the Jupyter Notebook UI).
* If you change the notebook (and you are invited to experiment with the code), the changes will be persisted in your notebook. If you are not sure about how to fix problems that occurred with your changes you still have the possibility to fall back on downloading a fresh copy of the notebook document from the OER code repository [here](https://github.com/oer4sdi/OER-spatial-data-streaming).

After having completed the Notebook document please come back and continue with the next chapter of this tutorial.


### 3.3 Sending a PM 2.5 data stream to the Kafka Broker (Step-2)

After we have downloaded the PM 2.5 sample data from openSenseMap we can now use the data from the resulting CSV file to produce a data stream that will be sent to the Kafka broker. 

From the Jupyter Notebook UI in your browser: please start the second Notebook document `src/step_2_producer.ipynb` and follow the guidance there. 

Once you have successfully activated the sequence of cells in the Notebook document, you should see an output of messages confirming the transmission of all PM 2.5 measurements form the CSV file. 

After having completed the Notebook document, please come back and continue with the next chapter of this tutorial.


### 3.4 Analysing and Visualizing PM 2.5 data streams (Step-3)

Now the Kafka broker has received a number of messages with PM 2.5 sensor data. Each message contains the information on what has been measured when and where. All messages have been tagged to belong to the topic “pm25_stream”. The Kafka broker has stored the messages in a temporary message store. 

Our next Jupyter Notebook implements a Consumer app that connects to the Kafka server and subscribes to the topic “pm25_stream” to get access to the sensor data stream. The Consumer app will use the data for two purposes: 
* to create a map that informes us about the location and current status of the PM 2.1 sensors 
* to send alerts in the case of the event that a sensor observes PM 2.5 concentrations that exceed a certain threshold for more than three days in a row. 

Now please open the third Notebook document `src/step_3_event_processing.ipynb`, read and activate the cells one-by-one. 

After having completed the Notebook document, please come back and continue with the next chapter of this tutorial.


### 3.5 Shut down and clean up

Now that we have used the Notebook documents to perform and understand all the tasks of our exercise we shut down and clean up our working environment.

In your terminal/CMD window that you used to build the docker images and start up the docker containers type `docker compose down` to shut down the docker containers. 

The docker images are still available in your docker environment. Next time when you want to run the environment, you can just use `docker compose up -d` to start up the containers again.

If you want to remove the images as well from your docker environment type Docker images to get a list of the available images. Then use `docker image rm [image id]` to remove the images that you want to delete. 


## 4. Wrap up

Hey! You did a great job! You installed and applied a powerful software stack for processing sensor data, including Docker, Kafka, Zookeeper and Jupyter Notebook. You prepared a PM 2.5 sample dataset using these technologies, sent a sensor data stream to a Kafka broker, and then analysed and visualised it using a consumer app. 
We hope that you now have an idea of how to work with spatial data streams, even though we have somewhat simplified the real applications in our exercise. For example: 
* In our example scenario, all messages were sent in a single stream from a single producer; in the real world, these messages come continuously and from many producers at the same time. 
* In our example, the consumer pulls the data from the stream in a batch mode; in near-real-time applications, the stream processors are often triggered by incoming data and are thus able to react to new information with the shortest possible delay.
* In our exercise, we downloaded a historical dataset (January 2022) and used the consumer application as if the data was from today. In fact, there was a long period without data in between. However, the consumer app would work the same way if we had used near real-time data.


**Interested In Learning More?**

On the Internet you will find a wealth of resources on NRT processing of data streams. Here are some recommendations: 
* MQTT.Org (2022): WebSite with information on MQTT, the de facto messaging protocol standard for IoT applications. https://mqtt.org
* Warhner, Kai (2020): Apache Kafka + Kafka Connect + MQTT Connector + Sensor Data. A practical example on how to combine Kafka and MQTT. GitHub repository. https://github.com/kaiwaehner/kafka-connect-iot-mqtt-connector-example
* Hughes, Jim (2021): GeoMesa – Big Data for GIS. FOSS4G 2021 Buenos Aires, October 1, 2021. Presentation:  https://www.geomesa.org/assets/outreach/foss4g-2021-streaming-data.pdf 
* Mollenkopf, A. (2017): Applying Geospatial Analytics at a Massive Scale using Kafka, Spark & Elastic Search on DC/OS. MesosCon North America:  https://www.youtube.com/watch?v=sa4RiH1RXEA&ab_channel=TheLinuxFoundation


**Your feedback is welcome!**

If you have identified shortcomings in this OER module or have ideas for improving the OER material, you are invited to add entries to the issue list in the [Github repository of this OER]( https://github.com/oer4sdi/OER-spatial-data-streaming).
