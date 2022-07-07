from ec2 import *

#Returns all instance details
get_instances()

#Security Groups Available
get_security_groups()

#Delete Security Group
delete_security_group('sg-0be42c43e2151a2')



#Create a class for the required instance
Test_Instance = Instance(['i-0eb0a54670'])

#Commands available
Test_Instance.get_details()
Test_Instance.start()
Test_Instance.stop()
Test_Instance.terminate()


