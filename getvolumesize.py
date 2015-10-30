import json
import sys
from boto.ec2 import connect_to_region
#usage python getvolumesize.py filename (size of instance) (number of volume)
conn = connect_to_region('us-east-1')
def check_size(instanceid,size):
	volumes = conn.get_all_volumes(filters={'attachment.instance-id': instanceid})
	k=volumes[0]
	remote_size=k.size
	if not remote_size == size:
		raise Exception('size not equal')
	else:
		print "True"
		#return True
def checkvolumes(instanceid,size):
	volumes = conn.get_all_volumes(filters={'attachment.instance-id': instanceid})
	if not len(volumes)==size:
		raise Exception('failed number of volumes')
	else:
		print "True"
		#return True
with open(sys.argv[1]+'.json') as data_file:    
    data = json.load(data_file)
    instanceid=data['InstanceId']
check_size(instanceid,int(sys.argv[2]))
checkvolumes(instanceid,int(sys.argv[3]))