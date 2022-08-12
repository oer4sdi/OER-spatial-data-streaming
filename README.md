Data Streaming Using Kafka
============

Mock stream producer for CSV data using Kafka.

Requires Docker and Docker Compose (Linux OS)

Usage
-------------------

Clone repo and cd into directory.

```
git clone 
cd data-streaming-kafka
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
docker run -it --rm --network=host -v D:\geoinformatica\data-stream-kafka\:/home kafkacsv python bin/processStream.py pm25_stream
```

**Shut down and clean up**

Stop the consumer with Return and Ctrl+C.

Shutdown Kafka broker system:

```
docker compose down
```