import boto3


#GET LIST OF ALL INSTANCES
def get_instances():
    ec2_client = boto3.client('ec2')
    reservations = ec2_client.describe_instances().get('Reservations')
    
    for res in reservations:
        try:
            for instance in res['Instances']:
                print(instance['InstanceId'])
                print(instance['InstanceType'])
                print(instance['PublicIpAddress'])
                print(instance['PublicDnsName'])
                print(instance['State']['Name'])
                print(instance['Tags'][0]['Value'])
                print('-----------------------')
        except:
            pass

#GET LIST OF ALL SECURITY GROUPS
def get_security_groups():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_security_groups()
    for res in response['SecurityGroups']:
        print(res['GroupName'])
        print(res['GroupId'])
        print('-------------')


#DELETE A SECURITY GROUP
def delete_security_group(secuirity_group_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.delete_security_group(
        GroupId = secuirity_group_id
    )
    print(response)


#CREATE AN EC2 INSTANCE CLASS
class Instance:
    def __init__(self,instance_id):
        self.instance_id = instance_id

    def stop(self):
        ec2_client = boto3.client('ec2')
        response = ec2_client.stop_instances(InstanceIds=self.instance_id)
        print(response)

    def start(self):
        ec2_client = boto3.client('ec2')
        response = ec2_client.start_instances(InstanceIds=self.instance_id)
        print(response)

    def terminate(self):
        ec2_client = boto3.client('ec2')
        response = ec2_client.terminate_instances(InstanceIds=self.instance_id)
        print(response)
    
    def get_details(self):
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances(InstanceIds=self.instance_id).get('Reservations')
        try:
          for res in response:
            for instance in res['Instances']:
                print(instance.get('InstanceId'))
                print(instance.get('InstanceType'))
                print(instance.get('PublicIpAddress'))
                print(instance.get('PublicDnsName'))
                print(instance.get('State')['Name'])
                print(instance.get('Tags')[0]['Value'])
                print('-----------------------')
        except:
            pass







