from gui import OmniSynthPath
import os

def is_valid_patch(patternFilename):
  return patternFilename.endswith('.scd')

# Find the user's OmniSynth install path,
# iterate through the dsp/patches directory,
# and return the patch names corresponding to the .scd files in that directory.
def get_patch_list():
  patches = os.listdir(OmniSynthPath + 'dsp/patches')
  return filter(is_valid_patch, patches)
