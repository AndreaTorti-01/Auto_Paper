import os
from sys import exit
from pathlib import Path
from time import sleep
from tkinter.filedialog import askdirectory
import pyperclip
import requests
from portforwardlib import forwardPort

folder = Path("C:\\")

# get the version list
def get_versions():
    try:
        response = requests.get('https://papermc.io/api/v2/projects/paper/')
    except:
        print('api error')
        exit()
    return response.json()['versions'][::-1]

# portforwarding
def open_ports():
    UPnPu = forwardPort(25565, 25565, None, None, False, 'UDP', 0, 'Minecraft UPnP', False)
    UPnPt = forwardPort(25565, 25565, None, None, False, 'TCP', 0, 'Minecraft UPnP', False)
    if UPnPt == False:
        print('TCP port forwarding failed')
    if UPnPu == False:
        print('UDP port forwarding failed')

def close_ports():
    UPnPu = forwardPort(25565, 25565, None, None, True, 'UDP', 0, 'Minecraft UPnP', False)
    UPnPt = forwardPort(25565, 25565, None, None, True, 'TCP', 0, 'Minecraft UPnP', False)
    if UPnPt == False:
        print('TCP port forwarding failed')
    if UPnPu == False:
        print('UDP port forwarding failed')

# choose installation folder
def folder_selection():
    folder = Path(askdirectory())
    return folder

# read/create version file
def start_server(chosen_version):
    installed_file = folder / 'installed.txt'
    server_file = folder / 'server.jar'
    try:
        with open(installed_file, mode='r', encoding='utf-8') as f:
            installed_ver = int(f.read())
    except IOError:
        with open(installed_file, mode='w', encoding='utf-8') as f:
            f.write('0')
            installed_ver = 0
    response = requests.get(f'https://papermc.io/api/v2/projects/paper/versions/{chosen_version}/')
    latest_build = response.json()['builds'][-1]

    if latest_build != installed_ver:
        print ('downloading new version...')
        data = requests.get(f'https://papermc.io/api/v2/projects/paper/versions/{chosen_version}/builds/{latest_build}/downloads/paper-{chosen_version}-{latest_build}.jar')

        with open(server_file, 'wb') as f:
            f.write(data.content)

        with open(installed_file, 'w', encoding='utf-8') as f:
            f.write(str(latest_build))

    else:
        print('latest version already installed')

    # starts the server
    os.chdir(folder)
    os.startfile('server.jar')

    # waits for start if never started
    mod_eula = False
    while(not os.path.exists(folder / 'eula.txt')):
        sleep(2)
        mod_eula = True

    # edits eula if eula is false
    if mod_eula == True:
        a_file = open(folder / 'eula.txt', 'r')
        list_of_lines = a_file.readlines()
        list_of_lines[3] = 'eula=true\n'
        a_file = open(folder / 'eula.txt', 'w')
        a_file.writelines(list_of_lines)
        a_file.close()
        os.startfile('server.jar')

    # gives the user the address, prompts to close and !portforwards
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    print(f"{ip}:25565 copied to clipboard!")
    pyperclip.copy(f"{ip}:25565")

def stop_server():
    os.system('taskkill /im  javaw.exe')