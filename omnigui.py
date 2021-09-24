from kivy.uix.screenmanager import ScreenManager

class OmniGui(ScreenManager):
    def __init__(self):
        # selecting the Main GUI screen for startup
        self.current = 'BootScreen'
