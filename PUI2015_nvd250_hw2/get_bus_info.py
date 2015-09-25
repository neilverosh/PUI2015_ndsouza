import json
import sys
import csv
import urllib2

if __name__=="__main__":
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	bus = json.load(request)
	number = bus['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	n = 0
	with open(sys.argv[3], 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
		for each in number:
			busLong = each['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
			busLat = each['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			stopName = each['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
			stopStat = each['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
			row = [busLat, busLong, stopName, stopStat]
			writer.writerow(row)
			n =n+1
	with open(sys.argv[3], 'rb') as csvfile:
		busreader = csv.reader(csvfile)
		for row in busreader:
			print ', '.join(row)