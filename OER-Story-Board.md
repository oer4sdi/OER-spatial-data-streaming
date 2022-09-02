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

## 3. Tutorial on Analyzing PM2.5 data streams with Jupyter Notebooks
[What this chapter is about,
Technical approach, architecture (mock data stream, ..),
Overview on the tasks to be performed,
Technical prerequisites]

### 3.1 Installing the SW environment
[
Guidance on Installing Docker
Brief summary about Docker and its purpose in the tutorial
Instructions on how to download and install Docker
Information on how to check if Docker is available as needed

Guidance on Installing the SW via docker compose

Brief description of the installation
Brief summary about Anaconda and its purpose in the Tutorial; Information on how to check if Anaconda, Python and Jupyter are available as needed
Kafka, Information on how to check if Kafka is available as needed
Python code/Jupyter Notebook, Information on how to check if the code/notebook is available as needed
]

### 3.2 Preparing the PM2.5 data stream

[
Access OpenSenseMap and download PM2.5 Sensor Data
Brief summary about OpenSenseMap and ist data access offerings
Instructions on how to download and store PM2.5 data as CSV
Information on how to check if the data is available as needed

guidance on how to run the python code/Jupyter Notebook

Jupyter Notebook:
Code & explanations
evidence that the stream is(was) up- and running
]

### 3.3 Preparing the PM2.5 monitor

[
(@Jaskaran: let us discuss if we stick to the interpolation use case, take another parameter (e.g. temperature) or switch to event detection.. )
guidance on how to run the python code/Jupyter Notebook


Jupyter Notebook:
Code & explanations
evidence that the monitoring is(was) up- and running
]

### 3.4 Test your knowledge
[Quiz - tbd]

## 4. Wrap up
[
Brief summary of the expected learning outcomes (2-3 sentences)
Links to further OER that might be interesting to deepen the knowledge in certain fields
Invitation to contribute by providing FeedBack, info on how to do so..
Funding reference
]
