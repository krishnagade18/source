import boto.ec2
import boto
import json
import sys
print "instance status report intiated"
with open(sys.argv[1]+'.json') as data_file:
    data = json.load(data_file)
    instanceid=data[sys.argv[2]]
conn = boto.ec2.connect_to_region('us-east-1')
istatus=conn.get_all_instance_status(instance_ids=instanceid)
status= istatus[0].system_status.status
if status=="ok":
        print "status ok"
else:
        raise Exception('status not okay ')

