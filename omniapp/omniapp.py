import subprocess
from omniapp.constants import OMNISYNTH_PATH

from kivy.app import App
from kivy.lang.builder import Builder

import numpy as np

from omniapp.omnigui import OmniGui
from kivy.uix.screenmanager import NoTransition

from kivy.clock import Clock
from kivy.properties import DictProperty, ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from scdMatrix import SCDMatrix, SCDType
from screens.bootScreen.bootScreen import BootScreen
from omnisynth import omni
from kivy.config import Config
from kivy.uix.label import Label


class OmniApp(App):
    """The Kivy app that controls our process"""

    omni_instance = ObjectProperty()
    slots = ListProperty()
    knob_coords = DictProperty()
    pattern_matrix = ListProperty()
    pattern_list = ListProperty()
    patch_matrix = ListProperty()
    patch_list = ListProperty()

    def build(self):
        """Responsible for:
        Initializing Kivy config
        Initializing new OmniSynth instance
        Initializing global parameters such as patch / pattern list, and knob coordinates
        """

        # Initialize Kivy config
        Config.set('kivy', 'keyboard_mode', 'system')
        Config.set('postproc', 'double_tap_time', '800')

        # initialize slot labels
        self.slots = [
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
            Label(size_hint=[1, 0.33], color=[0, 85, 255, 1]),
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
        ]

        # initialize omnisynth instance
        self.omni_instance = omni.Omni()

        # Compile all synthDefs and select first patch
        sc_main = OMNISYNTH_PATH + "main.scd"
        subprocess.Popen(["sclang", sc_main])
        # compiles all synthDefs.
        self.omni_instance.sc_compile("patches", OMNISYNTH_PATH)
        # selects first patch.
        self.omni_instance.synth_sel("tone1", OMNISYNTH_PATH)

        # initialize SCDMatrix classes for patches and patterns
        self.patch_matrix = SCDMatrix(SCDType.patch).get_matrix()
        self.patch_list = np.array(self.patch_matrix).flatten()
        self.pattern_matrix = SCDMatrix(SCDType.pattern).get_matrix()
        self.pattern_list = np.array(self.pattern_matrix).flatten()

        # initialize screen manager
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(boot_screen)

        return sm

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})

    def build_settings(self, settings):
        settings.add_json_panel(
            'Settings Template', self.config, filename=OMNISYNTH_PATH + '/gui/settings.json')

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)
