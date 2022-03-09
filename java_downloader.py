import requests
import os
import platform

def download_java():
    download_string = 'https://api.azul.com/zulu/download/community/v1.0/bundles/latest/binary?java_version=17.0&os=windows&arch=x86&'

    if platform.machine().endswith('64'):
        download_string = download_string + 'hw_bitness=64&ext=msi&bundle_type=jre'
    else:
        download_string = download_string + 'hw_bitness=32&ext=msi&bundle_type=jre'

    response = requests.get(download_string)

    with open("javainstaller.msi", 'wb') as f:
        f.write(response.content)
    os.startfile("javainstaller.msi")