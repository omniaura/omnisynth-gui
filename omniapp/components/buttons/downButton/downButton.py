from kivy.uix.button import Button

from constants import OMNISYNTH_PATH


class DownButton(Button):
    def on_release(self):
        self.moveDown()

    def moveDown(self):
        if self.manager.omni_instance.patchIndex != (self.manager.omni_instance.numPatch-1):
            self.manager.slots[0].text = str(
                self.manager.patch_list[self.manager.omni_instance.patchIndex])
            self.manager.omni_instance.patchIndex += 1
            self.manager.slots[1].text = str(
                self.manager.patch_list[self.manager.omni_instance.patchIndex])
            if self.manager.omni_instance.patchIndex+1 != self.manager.omni_instance.numPatch:
                self.manager.slots[2].text = str(
                    self.manager.patch_list[self.manager.omni_instance.patchIndex + 1])
            else:
                self.manager.slots[2].text = ''
            self.manager.omni_instance.synth_sel(
                self.manager.slots[1].text, OMNISYNTH_PATH)
