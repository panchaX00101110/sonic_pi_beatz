# this code was created by chatGPT when requested: using python package Sonic Pi create a reggaeton beat


from sonic_pi_tool import *

# Set tempo and time signature
set_tempo(95)
use_bpm(95)
set_volume(1)

# Define drum sounds
bd = :bd_haus
sd = :sn_dolf
ch = :drum_cymbal_pedal

# Define reggaeton beat pattern
pattern = [bd, ch, sd, ch, bd, ch, sd, ch]

# Loop the pattern
live_loop :beat do
  pattern.each do |p|
    sample p
    sleep 0.25
  end
end

