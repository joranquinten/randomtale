import file_loader
import player

read_folder = "./input/"
file_to_play = file_loader.random_file(read_folder)

player.player_load(file_to_play, 1)
player.player_start() # doesn't seem to get to this point!


'''
http://www.pygame.org/docs/ref/music.html
'''