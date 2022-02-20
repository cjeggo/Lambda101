import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [{
            'Name': "tag:Name",
            'Values': ["StopMe"]
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    #filter the instances
    instances = ec2.describe_instances(Filters=filters)
    
    kill_ids = []
    instances_full_details = instances['Reservations']
    for instance_detail in instances_full_details:
        group_instances = instance_detail['Instances']
        for instance in group_instances:
            instance_id = instance['InstanceId']
            kill_ids.append(instance_id)
    print(kill_ids)

        #make sure there are actually instances to shut down.
    if len(kill_ids) > 0:
        #perform the shutdown
        shuttingDown = ec2.stop_instances(InstanceIds=kill_ids)
        print(shuttingDown)
    else:
        print("All good")