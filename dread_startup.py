import os
import random
import time
import winsound

# set the directory path containing sound files
# Use os.path.dirname(__file__) to get the directory of the script
# Then join it with 'sounds' to make the path relative
dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")

# Check if the directory exists
if os.path.isdir(dir_path):
    # get a list of all the sound files in the directory
    sound_files = [f for f in os.listdir(dir_path) if f.endswith('.wav')]

    # wait for the computer to finish startup, optional
    #time.sleep(1)

    # only proceed if there are sound files
    if sound_files:
        # randomly select a sound file from the list
        selected_sound = random.choice(sound_files)

        # play the selected sound file
        winsound.PlaySound(os.path.join(dir_path, selected_sound), winsound.SND_FILENAME)
