# this code was created by chatGPT when requested: using python package Sonic Pi create a merengue beat


from psonic import *
use_synth(SAW)

# Define the tempo and time signature
bpm = 120
time_sig = 4

# Set the root note and chord progression
root_note = :C4
chords = [:C, :G, :F, :G]

# Define the drum pattern for the Merengue beat
drum_pattern = [0, 1, 0, 0, 1, 0, 1, 0]

# Set up the loop to play the beat
in_thread do
  loop do
    # Play the bass line
    play_pattern_timed([root_note, root_note, root_note, root_note - 12], [0.5, 0.5, 0.5, 1], amp: 0.5)
    
    # Play the chord progression
    chords.each do |chord|
      play_chord(chord, release: 0.5, amp: 0.3)
      sleep 1
    end
    
    # Play the drum pattern
    drum_pattern.each do |drum|
      sample :drum_bass_hard if drum == 1
      sample :drum_cymbal_closed if drum == 0
      sleep 0.25
    end
  end
end

# Set the tempo
use_bpm(bpm)

# Wait for the loop to finish
sleep time_sig * 4


