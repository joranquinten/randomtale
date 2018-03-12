import file_loader
import player
from pynput import keyboard

read_folder = "./input/"
file_to_play = file_loader.random_file(read_folder)

def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener
    if k in ['space']: # keys interested
        # self.keys.append(k) # store it in global-like variable
        print('Input received: ' + k)
        player.player_load(file_to_play, 1)
        player.player_start() # doesn't seem to get to this point!
        return False # remove this if want more keys

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys

'''
http://www.pygame.org/docs/ref/music.html
'''