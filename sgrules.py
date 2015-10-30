import boto.ec2
import json
import sys
print "security group rules check intiated"
conn = boto.ec2.connect_to_region("us-east-1")
with open(sys.argv[1]+'.json') as data_file:
    data = json.load(data_file)
    sgid=data[sys.argv[2]]
lis=[]
item=['tcp',8080,443]
print sgid
groups = conn.get_all_security_groups(group_ids=sgid)
for group in groups:
        #print group.name
        for rule in group.rules:
                print rule.ip_protocol, rule.from_port, rule.to_port, rule.grants
                lis.append(rule.ip_protocol)
                lis.append(rule.from_port)
                lis.append(rule.to_port)
                lis.append(rule.grants)
for item in lis:
        if item in lis:
                print True
        else:
                raise Exception('rules does not match')

