from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


class BootScreen(Screen):
    """The screen that is shown on boot"""
    # Right now, we just wait half a second
    # and switch to the main screen;
    # however, we can extend this in the future
    # to support pre-loading any assets we need before
    # we boot into the GUI.

    def on_enter(self):
        Clock.schedule_once(self.changeToMain, 5)

    def changeToMain(self, dt):
        self.manager.logger.log(
            'Setting current screen manager screen to main_screen')

        self.manager.current = 'main_screen'
