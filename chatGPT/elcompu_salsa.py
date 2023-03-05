# this code was created by chatGPT when requested: using python package Sonic Pi create a salsa beat

from sonicpi import SonicPi

# create a Sonic Pi instance
sp = SonicPi()

# set tempo and time signature
sp.tempo = 120
sp.time_signature = (4, 4)

# define instruments
bass_drum = sp.DSaw(amp=0.5, release=0.1)
snare_drum = sp.DSaw(amp=0.3, release=0.1)
hi_hat = sp.DSaw(amp=0.2, release=0.1)

# define patterns
bass_drum_pattern = "x-x-"
snare_drum_pattern = "--x-"
hi_hat_pattern = "x-x-"

# play patterns
sp.play_pattern_timed(bass_drum, bass_drum_pattern, beat=0.25)
sp.play_pattern_timed(snare_drum, snare_drum_pattern, beat=0.25)
sp.play_pattern_timed(hi_hat, hi_hat_pattern, beat=0.25)


