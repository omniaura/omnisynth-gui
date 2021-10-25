from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


class BootScreen(Screen):
    """The screen that is shown on boot"""
    # Screen that is shown while we load assets

    def on_enter(self):
        Clock.schedule_once(self.change_to_main, 10)

    def change_to_main(self, dt):
        self.manager.logger.log(
            'Setting current screen manager screen to main_screen')

        self.manager.current = 'main_screen'
