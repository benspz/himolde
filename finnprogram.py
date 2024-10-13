import  os

#Sjekker om platform er Windows eller Mac/Linux
if os.name == 'nt': split_mod = ";"
else: split_mod = ":"

def finn_app(app):
    funnet = False
    path = os.environ['PATH'].split(split_mod)
    try:
        for dir in path:
            if app in os.listdir(dir):
                print(f"{app} funnet i: {dir}")
                funnet = True
    except FileNotFoundError:
        pass
    if not funnet:
        print("Fant ikke program")

finn_app("tailscale")