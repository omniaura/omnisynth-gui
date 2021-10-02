import subprocess
from omniapp.constants import OMNISYNTH_PATH, SC_PROCESS_NAME, SC_SYNTH_PROCESS_NAME

from kivy.app import App
from kivy.lang.builder import Builder

import numpy as np

from kivy.uix.screenmanager import NoTransition

from kivy.clock import Clock
from kivy.properties import DictProperty, ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from omniapp.scdMatrix import SCDMatrix, SCDType
from omniapp.logger import Logger, LogLevel
from omniapp.screens.bootScreen.bootScreen import BootScreen
from omniapp.screens.mainScreen.mainScreen import MainScreen
from omnisynth import omni
from kivy.config import Config
from kivy.uix.label import Label
from kivy.lang import Builder
from pathlib import Path
from itertools import chain
import os
import datetime
import psutil


class Omni(ScreenManager):
    """A Kivy ScreenManager that has properties
    we need to persist throughout the manager's lifetime.
    """

    omni_instance = ObjectProperty()
    slots = ListProperty()
    knob_coords = DictProperty()
    pattern_matrix = ListProperty()
    pattern_list = ListProperty()
    patch_matrix = ListProperty()
    patch_list = ListProperty()
    logger = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__()

        self.omni_instance = omni.Omni()
        self.slots = [
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
            Label(size_hint=[1, 0.33], color=[0, 85, 255, 1]),
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
        ]

    def exit_app(self):
        process_names = [
            SC_PROCESS_NAME,
            SC_SYNTH_PROCESS_NAME
        ]
        for proc in psutil.process_iter():
            if proc.name() in process_names:
                proc.kill()

        exit()


class OmniApp(App):
    """The Kivy app that controls our process"""

    def __init__(self):
        super().__init__()

        # Initialize logger
        # TODO: default to :warn,
        #       but respect flags --debug (debug)
        #       or --verbose (:everything), etc
        self.logger = Logger()

        # Build KV components
        self.logger.log('Building .kv assets...')
        self.__init_kivy_components()

    def build(self):
        """Responsible for:
        Initializing Kivy config
        Initializing new OmniSynth instance
        Initializing global parameters such as patch / pattern list, and knob coordinates
        """

        self.__init_kivy_config()

        self.logger.log('Initializing screen manager...')
        sm = Omni(transition=NoTransition())

        self.logger.log('Initializing OmniSythn instance...')

        self.logger.log('Compiling synthdefs...')
        # Compile all synthDefs and select first patch
        sc_main = OMNISYNTH_PATH + "main.scd"
        subprocess.Popen(["sclang", sc_main])
        # compiles all synthDefs.
        sm.omni_instance.sc_compile("patches", OMNISYNTH_PATH)
        # selects first patch.
        sm.omni_instance.synth_sel("tone1", OMNISYNTH_PATH)

        # import pdb
        # pdb.set_trace()
        self.logger.log('Building patch and pattern matrices...')
        # initialize SCDMatrix classes for patches and patterns
        sm.patch_matrix = SCDMatrix(
            SCDType.patch, sm.omni_instance).get_matrix()
        sm.patch_list = np.array(sm.patch_matrix).flatten()
        sm.pattern_matrix = SCDMatrix(
            SCDType.pattern, sm.omni_instance).get_matrix()
        sm.pattern_list = np.array(sm.pattern_matrix).flatten()

        sm.logger = self.logger

        # self.logger.log('Setting current screen manager screen to boot_screen')
        # sm.current = 'boot_screen'

        sm.add_widget(BootScreen(name="boot_screen"))
        sm.add_widget(MainScreen(name="main_screen"))
        sm.current = "boot_screen"
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

    def __init_kivy_components(self):
        app_path = os.getcwd()

        screen_widgets = Path('omniapp/screens').rglob('*.kv')
        for screen_path in screen_widgets:
            self.logger.log('Adding screen ' + str(screen_path) + '...')
            Builder.load_file(app_path + '/' + str(screen_path))
        for widget_path in Path('omniapp/components').rglob('*.kv'):
            self.logger.log('Building asset ' + str(widget_path) + '...')
            Builder.load_file(
                app_path + '/' + str(widget_path))

    def __init_kivy_config(self):
        Config.set('kivy', 'keyboard_mode', 'system')
        Config.set('postproc', 'double_tap_time', '800')
