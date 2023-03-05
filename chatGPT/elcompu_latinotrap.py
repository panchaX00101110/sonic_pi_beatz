# this code was created by chatGPT when requested:  using python package Sonic Pi create a Latino trap beat


import sonicpi

sonicpi.connect()

# Set tempo and time signature
sonicpi.set_tempo(130)
sonicpi.set_time_signature(4, 4)

# Define instruments
bass = :bd_808
snare = :sn_dolf
hihat = :drum_cymbal_closed
synth = :pretty_bell

# Define patterns
bass_pattern = [1, 0, 0, 0, 1, 0, 0, 0]
snare_pattern = [0, 0, 1, 0, 0, 0, 1, 0]
hihat_pattern = [1, 1, 1, 1, 1, 1, 1, 1]
synth_pattern = [0.5, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5]

# Define functions to play patterns
def play_bass():
    sonicpi.play_pattern_timed(bass, bass_pattern, 0.25)

def play_snare():
    sonicpi.play_pattern_timed(snare, snare_pattern, 0.25)

def play_hihat():
    sonicpi.play_pattern_timed(hihat, hihat_pattern, 0.25)

def play_synth():
    sonicpi.play_pattern_timed(synth, synth_pattern, 0.25)

# Play the beat
for i in range(4):
    play_bass()
    play_snare()
    play_hihat()
    play_synth()

    
