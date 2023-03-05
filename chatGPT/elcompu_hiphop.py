# this code was created by chatGPT when requested: using python package Sonic Pi create a hiphop beat


# Basic Hip Hop Beat
use_bpm 90

# Define the kick drum sound
define :kick do
  sample :bd_808, amp: 3
end

# Define the snare drum sound
define :snare do
  sample :sn_dolf, amp: 2
end

# Define the hi-hat sound
define :hihat do
  sample :drum_cymbal_closed, amp: 1, release: 0.1
end

# Define the bass sound
define :bass do
  use_synth :tb303
  play :c2, release: 0.2, cutoff: 80, res: 0.8, amp: 1.5
end

# Play the beat
4.times do
  kick
  sleep 0.5
  snare
  sleep 0.5
  kick
  sleep 0.5
  hihat
  sleep 0.5
end

# Add some variation with the bass
2.times do
  bass
  sleep 1
end
