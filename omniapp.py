from util.getPatternList import get_pattern_list
from util.getPatchList import get_patch_list
from gui import OmniGui, OmniSynth, OmniSynthPath
import os
import subprocess

import numpy as np

from kivy.app import App
from kivy.uix.screenmanager import NoTransition


from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

# used for triggering events
from kivy.clock import Clock

class OmniApp(App):
    def build(self):
        global sm, patch1to12, patch13to24, patch25to36, patch37to48, pattern1to12, pattern13to24, pattern25to36, pattern37to48
        patch1to12 = []
        patch13to24 = []
        patch25to36 = []
        patch37to48 = []

        pattern1to12 = []
        pattern13to24 = []
        pattern25to36 = []
        pattern37to48 = []
   
        sc_main = OmniSynthPath + "dsp/main.scd"
        subprocess.Popen(["sclang", sc_main])
        OmniSynth.sc_compile("patches", OmniSynthPath) # compiles all synthDefs.
        OmniSynth.synth_sel("tone1", OmniSynthPath) # selects first patch.

        sm = OmniGui(transition=NoTransition())
        tempPatchList = get_patch_list()
        tempPatchList = np.sort(np.array(tempPatchList)).tolist()
        num_patches = len(tempPatchList)
        if num_patches > 36:
            patch1to12 = tempPatchList[0:12]
            patch13to24 = tempPatchList[12:24]
            patch25to36 = tempPatchList[24:36]
            patch37to48 = tempPatchList[36:]
        else:
            if num_patches > 24:
                patch1to12 = tempPatchList[0:12]
                patch13to24 = tempPatchList[12:24]
                patch25to36 = tempPatchList[24:]
            else:
                if num_patches > 12:
                    patch1to12 = tempPatchList[0:12]
                    patch13to24 = tempPatchList[12:]
                else:
                    patch1to12 = tempPatchList

        # Same thing for patterns
        tempPatternList = get_pattern_list()
        tempPatternList = np.sort(np.array(tempPatternList)).tolist()
        num_patterns = len(tempPatternList)
        if num_patterns > 36:
            pattern1to12 = tempPatternList[0:12]
            pattern13to24 = tempPatternList[12:24]
            pattern25to36 = tempPatternList[24:36]
            pattern37to48 = tempPatternList[36:]
        else:
            if num_patterns > 24:
                pattern1to12 = tempPatternList[0:12]
                pattern13to24 = tempPatternList[12:24]
                pattern25to36 = tempPatternList[24:]
            else:
                if num_patterns > 12:
                    pattern1to12 = tempPatternList[0:12]
                    pattern13to24 = tempPatternList[12:]
                else:
                    pattern1to12 = tempPatternList
        return sm

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})
    def build_settings(self, settings):
        settings.add_json_panel('Settings Template', self.config, filename = OmniSynthPath + '/gui/settings.json')

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)