import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('200.0.0.1', port=90, username='admin', password='asdfasdfsecret')

stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())

ssh.close()
