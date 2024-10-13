import os

def vistreff(søketekst, søkemappe):
    org_pos = os.getcwd()
    os.chdir(søkemappe)
    mapper = os.listdir()
    if søketekst in mapper:
        print(os.getcwd() + "/" + søketekst)
        return
    for mappe in mapper:
        if os.path.isdir(mappe):
            vistreff(søketekst, mappe)
    os.chdir(org_pos)


vistreff("test.txt", "/home/")