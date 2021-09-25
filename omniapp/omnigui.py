from kivy.uix.screenmanager import ScreenManager

# The screen manager for our app
class OmniGui(ScreenManager):
    def __init__(self, **kwargs):
        super(OmniGui, self).__init__(**kwargs)
        # start with the current screen as BootScreen
        self.current = 'BootScreen'
