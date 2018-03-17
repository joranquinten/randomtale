import file_loader
import player

read_folder = "./input/"
file_to_play = file_loader.random_file(read_folder)

player_instance = player

player_instance.player_load(file_to_play, 0.7)
player_instance.player_start()

'''
http://www.pygame.org/docs/ref/music.html
'''
