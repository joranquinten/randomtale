from os import listdir
from os.path import isfile, join
import random

mypath = "input"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

filetoplay = (random.choice(onlyfiles))

print(filetoplay)

'''
http://www.pygame.org/docs/ref/music.html
'''