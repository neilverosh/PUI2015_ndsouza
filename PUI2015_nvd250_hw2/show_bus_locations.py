import datetime
import json
import sys
import urllib2

if __name__=="__main__":
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	bus = json.load(request)
	number = bus['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	print 'Bus Line :', sys.argv[2]
	print 'Number of buses : ', len(number)
	n = 0
	for each in number:
		busLong = each['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		busLat = each['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		print 'Bus %d is at latitude %s and at longitude %s' % (n, busLat, busLong)
		n = n+1