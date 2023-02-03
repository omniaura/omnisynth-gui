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
from omniapp.screens.soundScreen.soundScreen import SoundScreen
from omniapp.screens.knobValScreen.knobValScreen import KnobValScreen
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


def stop_sc_processes():
    Logger.log(
        'Stopping currently running Supercollider and ScSynth processes...')
    process_names = [
        SC_PROCESS_NAME,
        SC_SYNTH_PROCESS_NAME
    ]
    for proc in psutil.process_iter():
        if proc.name() in process_names:
            proc.kill()
            Logger.log(f'Stopped process {proc.name()}.')


class Omni(ScreenManager):
    """A Kivy ScreenManager that has properties
    we need to persist throughout the manager's lifetime.
    """

    omni_instance = ObjectProperty()
    slots = ListProperty()
    knob_coords = DictProperty()

    def __init__(self, **kwargs):
        super().__init__()

        stop_sc_processes()
        Logger.log('Initializing OmniSynth instance...')
        self.omni_instance = omni.Omni()
        self.slots = [
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
            Label(size_hint=[1, 0.33], color=[0, 85, 255, 1]),
            Label(size_hint=[1, 0.33], color=[1, 1, 50, 1]),
        ]

    def exit_app(self):
        stop_sc_processes()
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

        sc_main = OMNISYNTH_PATH + "main.scd"

        if platform.system() == 'Darwin':
            subprocess.Popen(
                ["/Applications/SuperCollider.app/Contents/MacOS/sclang", sc_main])
        else:
            subprocess.Popen(["sclang", sc_main])
        sm.omni_instance.open_stream
        Clock.schedule_interval(sm.omni_instance.open_stream, 0.016)
        Clock.schedule_interval(lambda dt: self.set_attributes_from_sc(sm), 1)

        sm.omni_instance.set_active_patch("tone1")

        Logger.log('Building patch and pattern matrices...')
        sm.patch_matrix = SCDMatrix(
            SCDType.patch, sm.omni_instance).get_matrix()
        sm.patch_list = np.array(sm.patch_matrix).flatten()
        sm.pattern_matrix = SCDMatrix(
            SCDType.pattern, sm.omni_instance).get_matrix()
        sm.pattern_list = np.array(sm.pattern_matrix).flatten()

        sm.logger = Logger

        Logger.log('Adding main, boot, and knob screens...')
        sm.add_widget(BootScreen(name="boot_screen"))
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(KnobValScreen(name="knob_val_screen"))

        Logger.log('Adding patch screens...')

        patch_count = sm.omni_instance.osc_interface.patches.patch_count()

        for i in range(patch_group_count):
            screen_number = i + 1
            next_screen_number = screen_number + 1
            prev_screen_number = i

            screen_name = f'patch_screen_{screen_number}'
            next_screen_name = ''
            prev_screen_name = ''
            if patch_group_count > 1 and screen_number != patch_group_count:
                next_screen_name = f'patch_screen_{next_screen_number}'
            if screen_number != 1:
                prev_screen_name = f'patch_screen_{prev_screen_number}'

            screen = SoundScreen(
                name=screen_name, sound_names=sm.patch_matrix[i], page_number=screen_number, next_screen=next_screen_name, prev_screen=prev_screen_name)

            Logger.log(f'Adding screen {screen_name}...')
            sm.add_widget(screen)

            Logger.log('Adding patch screens...')

        # add pattern screens
        pattern_group_count = len(sm.pattern_matrix)

        for i in range(pattern_group_count):
            screen_number = i + 1
            next_screen_number = screen_number + 1
            prev_screen_number = i

            screen_name = f'pattern_screen_{screen_number}'
            next_screen_name = ''
            prev_screen_name = ''
            if pattern_group_count > 1 and screen_number != pattern_group_count:
                next_screen_name = f'pattern_screen_{next_screen_number}'
            if screen_number != 1:
                prev_screen_name = f'pattern_screen_{prev_screen_number}'

            screen = SoundScreen(sound_type='Pattern', name=screen_name, sound_names=sm.pattern_matrix[
                i], page_number=screen_number, next_screen=next_screen_name, prev_screen=prev_screen_name)

            Logger.log(f'Adding screen {screen_name}...')
            sm.add_widget(screen)
        sm.current = "boot_screen"

        return sm

    def set_attributes_from_sc(self, manager):
        self.set_device_table(manager)
        self.set_patch_param_table(manager)

    def set_device_table(self, manager):
        manager.device_table = manager.omni_instance.sc.out_dev_table

    def set_patch_param_table(self, manager):
        manager.patch_param_table = manager.omni_instance.sc.patch_param_table

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
