import os


def vistreff(søketekst, søkemappe):
    try:
        for fil in os.listdir(søkemappe):
            fil_sti = os.path.join(søkemappe, fil)
            if søketekst in fil:
                return fil_sti
            else:
                if os.path.isdir(fil_sti):
                    undermapper = []
                    undermapper.append(fil)
                    for mappe in undermapper:
                        vistreff(søketekst, søkemappe + "/" + mappe + "/")
    except:
        pass

print(vistreff("test.txt", "/home/benspz/"))