import os


for mappe in os.environ['PATH'].split(";" if os.name == 'nt' else ":"): print(mappe)
