import file_loader
import player

file_to_play = file_loader.random_file("./input/")
player.player_load(file_to_play, 1)
player.player_start()

'''
http://www.pygame.org/docs/ref/music.html
'''