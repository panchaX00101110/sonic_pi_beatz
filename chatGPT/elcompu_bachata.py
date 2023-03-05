# this code was created by chatGPT when requested: using python package Sonic Pi create a bachata beat

from psonic import *

# Set the tempo and key
use_bpm(120)
use_synth(DEFAULT_SYNTH)
set_volume(0.5)
set_mixer_control!

# Define the bassline
bassline = [ :G2, :D2, :F2, :C2 ].ring

# Define the chord progression
chords = [ :G2, :B2, :D3, :F3 ]

# Define the rhythm
rhythm = (ring 1, 1, 2, 3, 4, 4.5, 2, 3)

# Play the bassline and chords
in_thread do
  loop do
    play bassline.tick, release: 0.1, amp: 0.5
    sleep 0.25
  end
end

in_thread do
  loop do
    play_chord chords, release: 0.3, amp: 0.3
    sleep 1
  end
end

# Play the percussion
in_thread do
  loop do
    sample :drum_cymbal_closed, amp: 0.5
    sleep 0.5
  end
end

in_thread do
  loop do
    sample :bd_tek, amp: 2
    sleep rhythm.tick
  end
end

in_thread do
  loop do
    sample :elec_hi_snare, amp: 0.8
    sleep 0.25
    sample :elec_hi_snare, amp: 0.5
    sleep 0.75
  end
end




