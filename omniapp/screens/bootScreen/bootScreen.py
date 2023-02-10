from kivy.clock import Clock
from omniapp.logger import Logger
from kivy.uix.screenmanager import Screen


class BootScreen(Screen):
    """The screen that is shown on boot"""
    # Screen that is shown while we load assets

    def on_enter(self):
        Logger.log('Booting Omnisynth...')
        Clock.schedule_once(self.check_boot_status, 0.5)

    def check_boot_status(self):
        if self.manager.OmniSynth.sc_server_booted():
            self.manager.current = 'main_screen'
        else:
            Clock.schedule_once(self.check_boot_status, 0.5)
