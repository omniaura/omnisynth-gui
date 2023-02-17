import subprocess

from kivy.app import App
from kivy.lang.builder import Builder

import numpy as np

from kivy.uix.screenmanager import NoTransition

from kivy.clock import Clock
from kivy.properties import DictProperty, ListProperty, ObjectProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from omniapp.logger import Logger, LogLevel
from omniapp.screens.bootScreen.bootScreen import BootScreen
from omniapp.screens.mainScreen.mainScreen import MainScreen
from omniapp.screens.knobValScreen.knobValScreen import KnobValScreen
from .screens.patchSelectionScreen.patchSelectionScreen import PatchSelectionScreen
from .screens.patternSelectionScreen.patternSelectionScreen import PatternSelectionScreen
from omnisynth import omni
from kivy.config import Config
from kivy.uix.label import Label
from kivy.lang import Builder
from pathlib import Path
from itertools import chain
import os
import datetime
import psutil
import platform


class Omni(ScreenManager):
    """A Kivy ScreenManager that has properties
    we need to persist throughout the manager's lifetime.
    """

    OmniSynth = ObjectProperty()
    midi_map_mode_on = BooleanProperty(False)
    slots = ListProperty()

    def __init__(self, **kwargs):
        super().__init__()

        Logger.log('Initializing OmniSynth instance...')
        self.OmniSynth = omni.Omni()
        self.slots = [
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
            Label(size_hint=[1, 0.33], color=[0, 85, 255, 1]),
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
        ]

    def exit_app(self):
        self.OmniSynth.stop_sc_processes()
        exit()


class OmniApp(App):
    """The Kivy app that controls our process"""

    def __init__(self):
        super().__init__()

        # Build KV components
        Logger.log('Building .kv assets...')
        self.__init_kivy_components()

    def build(self):
        """Responsible for:
        Initializing Kivy config
        Initializing new OmniSynth instance
        Initializing global parameters such as patch / pattern list, and knob coordinates
        """

        self.__init_kivy_config()

        Logger.log('Initializing screen manager...')
        sm = Omni(transition=NoTransition())

        Logger.log('Compiling synthdefs...')

        sm.OmniSynth.stop_sc_processes()
        sm.OmniSynth.start_sc_process()
        sm.OmniSynth.open_stream
        Clock.schedule_interval(sm.OmniSynth.open_stream, 0.016)

        Logger.log('Adding screens...')
        sm.add_widget(BootScreen(name="boot_screen"))
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(KnobValScreen(name="knob_val_screen"))
        sm.add_widget(PatchSelectionScreen(name="patch_selection_screen"))
        sm.add_widget(PatternSelectionScreen(name="pattern_selection_screen"))

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
        app_path = os.getcwd()
        settings.add_json_panel(
            'Settings Template', self.config, filename=app_path + '\settings.json')

    def __init_kivy_components(self):
        app_path = os.getcwd()

        asset_directories = ['omniapp/screens', 'omniapp/components']
        for asset_directory in asset_directories:
            for asset_path in Path(asset_directory).rglob('*.kv'):
                Logger.log('Building asset ' + str(asset_path) + '...')
                Builder.load_file(
                    app_path + '/' + str(asset_path))

    def __init_kivy_config(self):
        Config.set('kivy', 'keyboard_mode', 'system')
        Config.set('postproc', 'double_tap_time', '800')
