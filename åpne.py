import os
import platform
import subprocess

def åpne_fil(fil):
    try:
        if platform.system() == 'Windows': os.startfile(fil)
        elif platform.system() == 'Darwin': subprocess.run(["open", fil], check=True)
        else: subprocess.run(["xdg-open", fil], check=True)
    except Exception as e:
        print(f"Klarer ikke åpne fil: {e}")

åpne_fil("/home/benspz/Documents/test.txt")

