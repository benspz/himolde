import  os

def finn_app(app):
    # Sjekker om platform er Windows eller Mac/Linux
    path = os.environ['PATH'].split(";" if os.name == 'nt' else ":")
    for dir in path:
        try:
            if app in os.listdir(dir):
                print(f"{app} funnet i: {dir}")
                break
        except FileNotFoundError:
            continue
    else:
        print("Fant ikke program")

finn_app("bash")
