#!/usr/bin/env python

"""Generates a stream to Kafka from a time series csv file.
"""
## Import Libraries
import argparse
import pandas as pd
import json
import sys
from dateutil.parser import parse
from confluent_kafka import Producer
import socket

def acked(err, msg):

    '''
    This function handles callback for Kafka Producer. It handles the error/success messages
    '''
    
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg.value()), str(err)))
    else:
        print("Message produced: %s" % (str(msg.value())))


def main():

    '''
    This is the main() function which should be invoked. It runs in the following order:

    1. Initialise Arguments Input: args.filename
    2. Topic: Every Kafka message should be associated to a kafka topic, it can be named anything
    3. conf: Init Kafka server with IP:Port
    '''
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename', type=str,
                        help='CSV file.')
    args = parser.parse_args()

    topic = "pm25_stream"
    p_key = args.filename
    
    ### START: AVOID MAKING CHANGES ###
    conf = {'bootstrap.servers': "kafka:9093", 'client.id': socket.gethostname()}
    producer = Producer(conf)
    ### END: AVOID MAKING CHANGES ###

    # Read CSV using Pandas
    df = pd.read_csv(p_key)
    
    # Init For Loop for number of records in CSV file
    for i in range(df.shape[0]): ## df.shape returns dimension of the dataframe (rows, columns)

        result = {} ## Init Dict
        result[df.loc[i,'value']] = [df.loc[i,'lat'], df.loc[i,'lon'], str(df.loc[i,'day']), df.loc[i,'boxId']]

        '''
        Format of result JSON:

        {
            'pm25_value_1': [lat, lon, day, boxId]
        }
        '''

        # Store as JSON as Kafka supports JSON transmission as standard
        result = json.dumps(result)
        
        ## Key is optional, used to categorize messages by partition, in this case all messages get the same partition name. 
        ## Is Mostly used for scalability 

        producer.produce(topic, key=p_key, value=result, callback=acked)

        ## Complete the sending of message from buffer and get a acknowledgement
        producer.flush()

if __name__ == "__main__":
    main()
