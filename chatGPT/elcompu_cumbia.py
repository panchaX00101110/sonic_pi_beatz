# this code was created by chatGPT when requested: using python package Sonic Pi create a cumbia beat

from psonic import *

# set the BPM (beats per minute) to 120
use_bpm(120)

# define the cumbia rhythm using drum samples
def cumbia_rhythm():
    sample(DRUM_HEAVY_KICK, rate=0.8)
    sleep(0.5)
    sample(DRUM_SNARE_HARD)
    sleep(0.25)
    sample(DRUM_HEAVY_KICK, rate=0.8)
    sleep(0.25)
    sample(DRUM_SNARE_HARD)
    sleep(0.25)
    sample(DRUM_HEAVY_KICK, rate=0.8)
    sleep(0.5)
    sample(DRUM_CYMBAL_OPEN, sustain=0.1)
    sleep(0.25)
    sample(DRUM_HEAVY_KICK, rate=0.8)
    sleep(0.5)

# play the cumbia rhythm
for i in range(4):
    cumbia_rhythm()
