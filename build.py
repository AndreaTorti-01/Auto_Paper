import PyInstaller.__main__
import os
import shutil
from pathlib import Path
import platform

PyInstaller.__main__.run([
    'Auto_Paper.py',
    '--onefile',
    '--noconsole'
])

if platform.system() == 'Linux':
    shutil.move(Path("dist/Auto_Paper"), "Auto_Paper")
elif platform.system() == 'Windows':
    shutil.move(Path("dist/Auto_Paper.exe"), "Auto_Paper.exe")
elif platform.system() == 'Darwin':
    shutil.move(Path("dist/Auto_Paper"), "Auto_Paper")

os.remove("Auto_Paper.spec")

try:
    shutil.rmtree("build")

except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

try:
    shutil.rmtree("dist")

except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))