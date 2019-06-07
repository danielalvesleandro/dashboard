
import paramiko

# ler chave guardando na memória
key = paramiko.RSAKey.from_private_key_file('./python-521.pem')

# define a política
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# cria a conexão
client.connect(hostname='18.231.109.74', username='ubuntu', pkey=key)

commands = [

    'sudo apt-get update -y',
    'sudo apt-get install -y python3-pip',

    'git clone https://github.com/danielalvesleandro/dashboard.git',

    'pip3 install -r dashboard/requirements.txt',
    'sudo python3 dashboard/app.py',

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())
