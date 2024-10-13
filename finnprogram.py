import  os

def finn_app(app):
    # Sjekker om platform er Windows eller Mac/Linux
    if os.name == 'nt': delimiter = ";"
    else:
        delimiter = ":"
    funnet = False
    path = os.environ['PATH'].split(delimiter)
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
