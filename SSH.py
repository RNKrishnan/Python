import paramiko

HOST_NAME = '192.168.1.17'
USER_NAME = 'root'
PASS_WD = '1990'
SSH_CLIENT = paramiko.SSHClient()

SSH_CLIENT.set_missing_host_key_policy(paramiko.AutoAddPolicy)

SSH_CLIENT.connect(hostname=HOST_NAME,username=USER_NAME,password=PASS_WD)
print('connection established')
CMD = 'df -h'

stdin,stdout,stderr = SSH_CLIENT.exec_command(CMD)
stdout = stdout.readlines()
print(stdout)




