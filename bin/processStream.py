#!/usr/bin/env python

"""Consumes stream for printing all messages to the console.
"""
import geopandas as gpd
import pandas as pd
import argparse
import json
import sys
import time
import socket
from confluent_kafka import Consumer, KafkaError, KafkaException
from tobler.area_weighted import area_interpolate

def main():

    df = pd.DataFrame()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('topic', type=str,
                        help='Name of the Kafka topic to stream.')

    args = parser.parse_args()

    conf = {'bootstrap.servers': '0.0.0.0:9092',
            'default.topic.config': {'auto.offset.reset': 'smallest'},
            'group.id': socket.gethostname()}

    consumer = Consumer(conf)

    running = True
    consumer.subscribe([args.topic])

    try:
        while running:

            msg = consumer.poll(timeout=10) # wait 5 seconds before exit
            if msg is None:
                break

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error().code() == KafkaError.UNKNOWN_TOPIC_OR_PART:
                    sys.stderr.write('Topic unknown, creating %s topic\n' %
                                     (args.topic))
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
        # Close down consumer to commit final offsets.
        consumer.close()

        df.rename(columns ={0:'lat',1:'lon',2:'value'}, inplace=True)

        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
        gdf.set_crs(epsg=4326, inplace=True)
        gdf.to_crs(epsg=3035, inplace=True)
        gdf.drop(['lon','lat'], axis=1, inplace=True)
        gdf['geometry'] = gdf.geometry.buffer(0.0001)
        
        area = gpd.read_file('data/de_10km.shp')
        area.to_crs(epsg=3035, inplace=True)
        
        interpolation = area_interpolate(source_df=gdf, target_df=area, intensive_variables=['value'])
        print(interpolation)
        interpolation.to_crs(epsg=4326, inplace=True)
        interpolation.to_file('data/interpolated.shp', driver='ESRI Shapefile')


if __name__ == "__main__":
    main()
