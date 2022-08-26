#!/usr/bin/env python

"""Consumes stream for printing all messages to the console.
"""
import pandas as pd
import json
import sys
import time
import socket
from confluent_kafka import Consumer, KafkaError, KafkaException

def main():
    
    ## Consumbed message will be stored in this variable
    df = pd.DataFrame()

    ## Set topic name as set in sendStream.py
    topic = "pm25_stream"

    ### START: AVOID MAKING CHANGES ###

    '''
    Offset decides in what order to consume the message. "smallest" means read the first message that was sent at 1st position and then the others.
    "largest" will mean to read the most 'recent' message in 1st position and then others in the same order
    '''

    conf = {'bootstrap.servers': '0.0.0.0:9092',
            'default.topic.config': {'auto.offset.reset': 'smallest'},
            'group.id': socket.gethostname()}
    ### EMD: AVOID MAKING CHANGES ###

    consumer = Consumer(conf)

    running = True
    consumer.subscribe([topic])

    try:
        while running:

            msg = consumer.poll(timeout=10) # wait 10 seconds before exit. If no messages are received for 10 seconds, consuming will stop 
            if msg is None:
                break

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                        (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error().code() == KafkaError.UNKNOWN_TOPIC_OR_PART:
                    sys.stderr.write('Topic unknown, creating %s topic\n' %
                                        (topic))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                
                input = json.loads(msg.value())
                key = list(input.keys())[0]

                lat = input[key][0]
                lon = input[key][1]
                pm25 = float(key)

                df = df.append([[lat, lon, pm25]])
    
    except KeyboardInterrupt:
        pass
    
    finally:
        consumer.close()
        df.rename(columns ={0:'lat',1:'lon',2:'value'}, inplace=True)
        df[['lat','lon','value']].to_csv('data/streamed_output.csv')

if __name__ == "__main__":
    main()
