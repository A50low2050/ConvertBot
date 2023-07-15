import os
from config import PATH, MEDIA

for address, dirs, files in os.walk(os.path.join(PATH, MEDIA)):
    for name in files:
        os.remove(os.path.join(address, name))
