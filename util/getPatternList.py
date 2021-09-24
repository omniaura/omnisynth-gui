from gui import OmniSynthPath
import os

def is_valid_pattern(patternFilename):
  return patternFilename.endswith('.scd')

# Find the user's OmniSynth install path,
# iterate through the dsp/patterns/songs/song1 directory,
# and return the pattern names corresponding to the .scd files in that directory.
def get_pattern_list():
  patches = os.listdir(OmniSynthPath + 'dsp/patterns/songs/song1')
  return filter(is_valid_pattern, patches)
