import PyInstaller.__main__
import os
import shutil

PyInstaller.__main__.run([
    'Auto_Paper.py',
    '--onefile',
    '--noconsole'
])

shutil.move("dist\Auto_Paper.exe", "Auto_Paper.exe")

os.remove("Auto_Paper.spec")

try:
    shutil.rmtree("build")

except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

try:
    shutil.rmtree("dist")

except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))