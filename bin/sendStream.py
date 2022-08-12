#!/usr/bin/env python

"""Generates a stream to Kafka from a time series csv file.
"""

import argparse
import pandas as pd
import json
import sys
from dateutil.parser import parse
from confluent_kafka import Producer
import socket


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg.value()), str(err)))
    else:
        print("Message produced: %s" % (str(msg.value())))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename', type=str,
                        help='CSV file.')
    args = parser.parse_args()

    topic = "pm25_stream"
    p_key = args.filename

    conf = {'bootstrap.servers': "0.0.0.0:9092",
            'client.id': socket.gethostname()}
    producer = Producer(conf)

    df = pd.read_csv(args.filename)
    
    for i in range(df.shape[0]):

        result = {}

        result[df.loc[i,'value']] = [df.loc[i,'lat'], df.loc[i,'lon']]
        result = json.dumps(result)
        
        producer.produce(topic, key=p_key, value=result, callback=acked)
        producer.flush()

if __name__ == "__main__":
    main()
