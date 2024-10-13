import  os

#Sjekker om platform er Windows eller Mac/Linux
if os.name == 'nt': split_mod = ";"
else: split_mod = ":"

def find_app(app):
    path = os.environ['PATH'].split(split_mod)
    try:
        for dir in path:
            os.chdir(dir)
            if app in os.listdir(dir):
                print(f"{app} found in: {dir}")
    except FileNotFoundError:
        pass

find_app("tailscale")
