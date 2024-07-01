from cvprac.cvp_client import CvpClient
from cvprac.cvp_client_errors import CvpApiError
from pprint import pprint
import pyeapi

client = CvpClient()
client.connect(['10.18.168.105'], 'cvpadmin', 'Arista123!')
api_user = 'admin'
api_password = 'Arista123!'



#Create new container.
# parent = client.api.search_topology('Tenant')
# client.api.add_container('General_Config', 'Tenant', parent['containerList'][0]['key'])
# new_container = client.api.search_topology('General_Config')

#Get CVP Inventory
# inventory = client.api.get_inventory()
# print (inventory)

# Create configlet from configs folder
# with open("configs/HOST1B.34435ec582c9.cfg", "r") as f:
#     configlet_content = f.read()


# configlet_name = 'HOST1B.34435ec582c9'
# # Check if we already have a configlet by this name
# try:
#     configlet = client.api.get_configlet_by_name(configlet_name)
# except CvpApiError as err:
#     if 'Entity does not exist' in err.msg:
#         # Configlet doesn't exist let's create one
#         result = client.api.add_configlet(configlet_name, configlet_content)
#         pprint(result)
#     else:
#         raise
# else:
#     # Configlet does exist, let's update the content
#     result = client.api.update_configlet(configlet_content, configlet['key'], configlet_name)
#     pprint(result)
# configlet_info = client.api.get_configlet_by_name(configlet_name)
# pprint(configlet_info)


######################
# with open("clab/override_configs/HOST1B.34435ec582c9.cfg", "r") as f:
#     configlet_content = f.read()


# configlet_name = 'OR.HOST1B.34435ec582c9'
# # Check if we already have a configlet by this name
# try:
#     configlet = client.api.get_configlet_by_name(configlet_name)
# except CvpApiError as err:
#     if 'Entity does not exist' in err.msg:
#         # Configlet doesn't exist let's create one
#         result = client.api.add_configlet(configlet_name, configlet_content)
#         pprint(result)
#     else:
#         raise
# else:
#     # Configlet does exist, let's update the content
#     result = client.api.update_configlet(configlet_content, configlet['key'], configlet_name)
#     pprint(result)
# configlet_info = client.api.get_configlet_by_name(configlet_name)
# pprint(configlet_info)



task_list = []
# for device in devices:
#   with open(device['deviceName']+".cfg") as file:
#      configlet_file = file.read()
#   print (f"Creating configlet {device['configletName']} for {device['deviceName']}\n")
#   try:
#      configlet = client.api.get_configlet_by_name(device['configletName'])
#      client.api.update_configlet(configlet_file, configlet['key'], device['configletName'])
#   except:
#      client.api.add_configlet(device['configletName'], configlet_file)


# Move device into container
###################
# device = client.api.get_device_by_name('HOST1B')
# container = client.api.get_container_by_name('General_Config')
# print("Moving device to container")
# move = client.api.move_device_to_container("python", device, container)
# task_list = task_list + move['data']['taskIds']
# # client.api.apply_configlets_to_device("", device, [configlet])
# print(f"Generated task IDs are: {task_list}\n")
 



# Execute each task separately (legacy way)
# for task in task_list:
#   client.api.execute_task(task)

device = client.api.get_device_by_name('HOST1B')

connection = pyeapi.connect(host=device['ipAddress'], transport='https', username=api_user, password=api_password)
connection.transport._context.set_ciphers('DHE-RSA-AES256-SHA')
running_config = connection.execute(['enable', 'show running-config'], 'text')

result = client.api.update_reconcile_configlet(device['systemMacAddress'],running_config['result'][1]['output'],"",'HOST1B.34435ec582c9.Reconcile',True)
# configlet = client.api.get_configlet_by_name('HOST1B.34435ec582c9')
# configlet_list = []
# configlet_list = configlet_list.append(configlet['key'])

# reconcile = client.api.validate_configlets_for_device(device['systemMacAddress'],configlet_list, 'validate')
# task_list = task_list + move['data']['taskIds']
# # client.api.apply_configlets_to_device("", device, [configlet])
# print(f"Generated task IDs are: {task_list}\n")
pprint(result)