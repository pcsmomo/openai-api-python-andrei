import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('remote_host', username='username', password='password')

stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())

ssh.close()
