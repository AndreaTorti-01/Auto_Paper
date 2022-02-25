import os
from sys import exit
from pathlib import Path
from time import sleep

import tkinter
from tkinter.filedialog import askdirectory
from tkinter import simpledialog
import pyperclip

import requests
from portforwardlib import forwardPort

def main():
    # boilerplate
    root = tkinter.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    class ChoiceDialog(simpledialog.Dialog):
        def __init__(self, parent, title, text, items):
            self.selection = None
            self._items = items
            self._text = text
            super().__init__(parent, title=title)

        def body(self, parent):
            self._message = tkinter.Message(parent, text=self._text, aspect=400)
            self._message.pack(expand=1, fill=tkinter.BOTH)
            self._list = tkinter.Listbox(parent)
            self._list.pack(expand=1, fill=tkinter.BOTH, side=tkinter.TOP)
            for item in self._items:
                self._list.insert(tkinter.END, item)
            return self._list

        def validate(self):
            if not self._list.curselection():
                return 0
            return 1

        def apply(self):
            self.selection = self._items[self._list.curselection()[0]]

    def dialogchoice(text, items):
        dialog = ChoiceDialog(root, 'window', text=text, items=items)
        return dialog.selection


    # portforwarding
    UPnPu = forwardPort(25565, 25565, None, None, False, 'UDP', 0, 'Minecraft UPnP', False)
    UPnPt = forwardPort(25565, 25565, None, None, False, 'TCP', 0, 'Minecraft UPnP', False)
    if UPnPt == False:
        print('TCP port forwarding failed')
    if UPnPu == False:
        print('UDP port forwarding failed')


    # choose installation folder
    answer = dialogchoice('do you want to install server in custom folder?', ['no', 'yes'])

    if answer == 'no':
        folder = Path('C:/mc_server')
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
    else:
        folder = Path(askdirectory())


    # read/create version file
    installed_file = folder / 'installed.txt'
    server_file = folder / 'server.jar'

    try:
        with open(installed_file, mode='r', encoding='utf-8') as f:
            installed_ver = int(f.read())
    except IOError:
        with open(installed_file, mode='w', encoding='utf-8') as f:
            f.write('0')
            installed_ver = 0


    # get the version list and prompt to choose one
    try:
        response = requests.get('https://papermc.io/api/v2/projects/paper/')
    except:
        print('api error')
        exit()

    choice = response.json()['versions']
    chosen_version = dialogchoice('select minecraft version', choice[::-1])


    # get the builds list and download latest
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

    input('Press Enter to close the server...')
    os.system('taskkill /im  javaw.exe')
    UPnPu = forwardPort(25565, 25565, None, None, True, 'UDP', 0, 'Minecraft UPnP', False)
    UPnPt = forwardPort(25565, 25565, None, None, True, 'TCP', 0, 'Minecraft UPnP', False)

if __name__ == "__main__":
    main()
