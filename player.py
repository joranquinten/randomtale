import pygame as pg

def player_load(music_file, volume=0.8):
    print("Loading")
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

def player_start():
    print("Started")
    if pg.mixer.music.get_busy() == False:
        pg.mixer.music.play()

def player_stop():
    print("Stopped")
    if pg.mixer.music.get_busy():
        pg.mixer.music.stop()

def player_pause():
    print("Paused")
    if pg.mixer.music.get_busy():
        pg.mixer.music.pause()

def player_resume():
    print("Resumed")
    if pg.mixer.music.get_busy():
        pg.mixer.music.unpause()
