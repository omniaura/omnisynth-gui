from screens.baseScreen import BaseScreen
from omniapp import PatchMatrix, PatternMatrix
from screens.soundPage import SoundPage

# This layout file contains all page definitions
# for pages specified in omni.kv
class PatchPage1(SoundPage):
    def __init__(self):
        super().__init__(PatchMatrix[0])
        if len(PatchMatrix[1]) > 0:
            self.next_screen = 'PatchPage2'

class PatchPage2(SoundPage):
    def __init__(self):
        super().__init__(PatchMatrix[1])
        if len(PatchMatrix[2]) > 0:
            self.next_screen = 'PatchPage3'

class PatchPage3(SoundPage):
    def __init__(self):
        super().__init__(PatchMatrix[2])
        if len(PatchMatrix[3]) > 0:
            self.next_screen = 'PatchPage4'

class PatchPage4(SoundPage):
    def __init__(self):
        super().__init__(PatchMatrix[3])

class LedPage1(SoundPage):
    def __init__(self):
        super().__init__(PatternMatrix[0])
        if len(PatternMatrix[1]) > 0:
            self.next_screen = 'PatternPage2'

class LedPage2(SoundPage):
    def __init__(self):
        super().__init__(PatternMatrix[1])
        if len(PatternMatrix[2]) > 0:
            self.next_screen = 'PatternPage3'

class LedPage3(SoundPage):
    def __init__(self):
        super().__init__(PatternMatrix[2])
        if len(PatternMatrix[3]) > 0:
            self.next_screen = 'PatternPage4'

class LedPage3(SoundPage):
    def __init__(self):
        super().__init__(PatternMatrix[3])

class WaveFormPage(BaseScreen):
    pass
class MidiLearnPage(BaseScreen):
    pass
