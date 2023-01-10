from google.transit import gtfs_realtime_pb2
import urllib.request as ur
import json
import datetime as dt
import pandas as pd
import pickle
import time

# routes = pd.read_csv('data/routes.txt')
# stop_times = pd.read_csv('data/stop_times.txt')
# stops = pd.read_csv('data/stops.txt')
# fare_rules = pd.read_csv('data/fare_rules.txt')
# fare_attributes = pd.read_csv('data/fare_attributes.txt')
# trips = pd.read_csv('data/trips.txt')


# a = trips[['route_id', 'service_id', 'trip_id', 'trip_headsign', 'direction_id']]
# b = routes[['route_id', 'route_short_name', 'route_long_name']]
# c = stop_times[['trip_id', 'arrival_time', 'stop_id', 'stop_sequence']]
# tmp = c.merge(a, how = 'left', on='trip_id')
# fullStops = tmp.merge(b, how='inner', on = 'route_id')
# #fullStops.to_pickle('api/fullStops.pkl')







def updateFullStops(fullStops=None):

	feed = gtfs_realtime_pb2.FeedMessage()
	header = gtfs_realtime_pb2.FeedHeader()


	response = ur.Request('http://api.bart.gov/gtfsrt/tripupdate.aspx', headers={'User-Agent': 'Mozilla/5.0'})

	response = ur.urlopen(response)

	feed.ParseFromString(response.read())
	header.ParseFromString(response.read())
	print(type(feed))

	f = open("barter.out", "w")
	f.write(str(feed))
	f.close()
	print(type(feed.entity))
	print(len(feed.entity))

	g = open("outter.out", "w")
	g.write(str(feed.entity[0]))
	g.close()



def getData():

	fullStops = pd.DataFrame(pickle.load(open('fullStops.pkl', 'rb')))
	print(fullStops.head(40))
	allStops = pickle.load(open('allStops.pkl', 'rb'))
	print(allStops)
	print(len(allStops))


	updateFullStops(fullStops)

	ret = {}



updateFullStops()



# e = json.dumps(str(feed))

# with open('dumper.json', 'w') as f:
#     f.write(str(feed))

# for entity in feed.entity:
#   print(type(entity))
#   if entity.HasField('trip_update'):
#     print("id----------------------" + entity.id)
#     print(entity.trip_update)

