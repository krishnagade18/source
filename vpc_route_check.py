import json
import boto.vpc
import sys
#usage python vpc_check.py filename keyname
conn = boto.vpc.connect_to_region('us-east-1')
lis=[]
item=['active','local']
with open(sys.argv[1]+'.json') as data_file:    
    data = json.load(data_file)
    vpcid=data[sys.argv[2]]
route_table1 = conn.get_all_route_tables(filters={'vpc-id':vpcid})
for route in route_table1:
	print route
	rtroutes=route.routes
	for rtlist in rtroutes:
		lis.append(rtlist.destination_cidr_block)
		lis.append(rtlist.state)
		lis.append(rtlist.gateway_id)
print lis
for item in lis:
	if item in lis:
		print True
	else:
		raise Exception('rules does not match')