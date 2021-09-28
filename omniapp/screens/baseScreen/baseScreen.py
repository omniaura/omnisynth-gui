from kivy.uix.screenmanager import Screen


class BaseScreen(BaseScreen):
    """A Kivy screen that implements various omniSynth-related

    methods that we want each screen to share.
    """

    def toneSel(self, tone):
        """Performs OmniSynth#synth_sel via a tone"""

        self.root.omnisynth_instance.synth_sel(tone, OMNISYNTH_PATH)

    def exitSel(self):
        """Performs OmniSynth#exit_sel"""

        self.root.omnisynth_instance.exit_sel()
        exit()
