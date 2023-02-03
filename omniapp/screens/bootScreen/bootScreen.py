from kivy.clock import Clock
from omniapp.logger import Logger
from kivy.uix.screenmanager import Screen
from omniapp.constants import OMNISYNTH_PATH


class BootScreen(Screen):
    """The screen that is shown on boot"""
    # Screen that is shown while we load assets

    def on_enter(self):
        # compile patches by calling omni#synth_sel on all patches
        Logger.log('Compiling patches...')

        sm.omni_instance.compile_patches("patches", OMNISYNTH_PATH)
        Clock.schedule_once(self.change_to_main, 10)

    def change_to_main(self, dt):
        Logger.log(
            'Setting current screen manager screen to main_screen')

        self.manager.current = 'main_screen'
