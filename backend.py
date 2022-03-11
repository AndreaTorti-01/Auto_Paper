import platform
import os
import sys
import subprocess
from pathlib import Path
from time import sleep
from tkinter.filedialog import askdirectory
import pyperclip
import requests
from portforwardlib import forwardPort
import variables
from threading import Thread
import tempfile

# auxilliary
def run_file(file):
    try:
        subprocess.Popen(file, shell=False)
    except:
        subprocess.Popen(str(file), shell=True)

# downloads and runs zulu java installer
def install_java():
    Thread(target=install_java_t).start()
def install_java_t():
    download_string = 'https://api.azul.com/zulu/download/community/v1.0/bundles/latest/binary?bundle_type=jre&arch=x86'

    if platform.machine().endswith('64'):
        download_string = download_string + '&hw_bitness=64'
    else:
        download_string = download_string + '&hw_bitness=32'

    if platform.system() == 'Linux':
        system = "linux"
        extension = "deb"
    elif platform.system() == 'Windows':
        system = "windows"
        extension = "msi"
    elif platform.system() == 'Darwin':
        system = "macos"
        extension = "dmg"
    download_string = download_string + f'&os={system}&ext={extension}'

    chosen_java_version = variables.chosenJavaVersion.get()
    download_string = download_string + f'&java_version={chosen_java_version}'

    print("downloading java, please wait for the installer to start...")
    response = requests.get(download_string)
    
    tempDir = Path(tempfile.gettempdir())
    with open(tempDir / f"javainstaller.{extension}", 'wb') as f:
        f.write(response.content)
    run_file(tempDir / f"javainstaller.{extension}")

# get the version list
def get_minecraft_versions():
    try:
        response = requests.get('https://papermc.io/api/v2/projects/paper/')
    except:
        print('api error')
        sys.exit()
    return response.json()['versions'][::-1]

# gets list of available java versions
def get_java_versions():
    get_versions_string = 'https://api.azul.com/zulu/download/community/v1.0/bundles?bundle_type=jre&arch=x86'

    if platform.machine().endswith('64'):
        get_versions_string = get_versions_string + '&hw_bitness=64'
    else:
        get_versions_string = get_versions_string + '&hw_bitness=32'

    if platform.system() == 'Linux':
        get_versions_string = get_versions_string + '&os=linux&ext=deb'
    elif platform.system() == 'Windows':
        get_versions_string = get_versions_string + '&os=windows&ext=msi'
    elif platform.system() == 'Darwin':
        get_versions_string = get_versions_string + '&os=macos&ext=dmg'

    response = requests.get(get_versions_string)
    list_of_dicts = response.json()
    java_versions = []
    for dict in list_of_dicts:
        if not dict['java_version'][0] in java_versions:
            java_versions.append(dict['java_version'][0])

    return java_versions

# portforwarding
def open_ports():
    Thread(target=open_ports_t).start()
def open_ports_t():
    UPnPu = forwardPort(25565, 25565, None, None, False, 'UDP', 0, 'Minecraft UPnP', False)
    UPnPt = forwardPort(25565, 25565, None, None, False, 'TCP', 0, 'Minecraft UPnP', False)
    if UPnPt == False:
        print('TCP port forwarding failed')
    if UPnPu == False:
        print('UDP port forwarding failed')
    print('ports opened successfully')

def close_ports():
    Thread(target=close_ports_t).start()
def close_ports_t():
    UPnPu = forwardPort(25565, 25565, None, None, True, 'UDP', 0, 'Minecraft UPnP', False)
    UPnPt = forwardPort(25565, 25565, None, None, True, 'TCP', 0, 'Minecraft UPnP', False)
    if UPnPt == False:
        print('TCP port forwarding failed')
    if UPnPu == False:
        print('UDP port forwarding failed')
    print('ports closed successfully')

# choose installation folder
def folder_selection():
    variables.folder.set(Path(askdirectory()))

# read/create version file
def start_server():
    Thread(target=start_server_t).start()
def start_server_t():
    chosen_version = variables.chosenMinecraftVersion.get()
    folder = Path(variables.folder.get()) / f'{chosen_version}'
    if(not os.path.exists(folder)):
        os.mkdir(folder)
    installed_file = folder/ 'installed.txt'
    server_file = folder / 'server.jar'
    try:
        with open(installed_file, mode='r', encoding='utf-8') as f:
            installed_build = int(f.read())
    except IOError:
        with open(installed_file, mode='w', encoding='utf-8') as f:
            f.write('0')
            installed_build = 0
    response = requests.get(f'https://papermc.io/api/v2/projects/paper/versions/{chosen_version}/')
    latest_build = response.json()['builds'][-1]

    if latest_build != installed_build:
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
    run_file('server.jar')
    print('starting up...')

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
        run_file('server.jar')

    # gives the user the address, prompts to close and !portforwards
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    print(f"-> {ip}:25565 <- copied to clipboard! Share this with your friends to play togheter")
    pyperclip.copy(f"{ip}:25565")

def stop_server():
    Thread(target=stop_server_t).start()
def stop_server_t():
    os.system('taskkill /im  javaw.exe')
    print('stopping server...')
