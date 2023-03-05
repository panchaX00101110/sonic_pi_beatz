# The code was created by chatGPT when requested: using python package Sonic Pi create a mexican banda beat

# This code uses the use_synth function to set the synthesizer to PROPHET, which is a good choice for creating brass sounds. 
# It then sets the tempo and time signature using the use_bpm function and defines the rhythms and notes for the bass line, 
# brass section, and percussion using tuples and lists. Finally, it loops through the rhythms and notes, 
# playing them using the play and sample functions and sleeping for the appropriate durations using the sleep function.


from psonic import *

use_synth(PROPHET)

# Set the tempo and time signature
bpm = 120
use_bpm(bpm)
time_signature = (3, 4)

# Define the rhythm and notes for the bass line
bass_rhythm = (1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 1.5, 0.5)
bass_notes = [E2, E2, G2, E2, G2, F2, E2, D2, C2, D2, E2, C2, A1, REST]

# Define the rhythm and notes for the brass section
brass_rhythm = (1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 1.5, 0.5)
brass_notes = [A2, A2, C3, A2, A2, G2, F2, E2, C2, REST]

# Define the rhythm and notes for the percussion
perc_rhythm = (0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1)
perc_notes = [DRUM_BASS_SOFT, DRUM_SNARE_SOFT, DRUM_BASS_SOFT, DRUM_SNARE_SOFT,
              DRUM_BASS_SOFT, DRUM_SNARE_SOFT, DRUM_CYMBAL_CLOSED, DRUM_CYMBAL_PEDAL]

# Play the bass line
for i in range(len(bass_rhythm)):
    duration = time_signature[1] * bass_rhythm[i]
    play(bass_notes[i], release=duration * 0.9, sustain=duration * 0.1)
    sleep(duration)

# Play the brass section
for i in range(len(brass_rhythm)):
    duration = time_signature[1] * brass_rhythm[i]
    play(brass_notes[i], release=duration * 0.9, sustain=duration * 0.1, amp=0.8)
    sleep(duration)

# Play the percussion
for i in range(len(perc_rhythm)):
    duration = time_signature[1] * perc_rhythm[i]
    sample(perc_notes[i], rate=1.2, amp=0.7)
    sleep(duration)

    
    
