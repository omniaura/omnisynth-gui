from kivy.uix.button import Button

from constants import OMNISYNTH_PATH


class UpButton(Button):
    def move_up(self):
        if self.manager.omni_instance.patchIndex != 0:
            if self.manager.omni_instance.patchIndex == 1:
                self.manager.slots[0].text = ''
                self.manager.slots[1].text = str(self.manager.patch_list[0])
                self.manager.slots[2].text = str(self.manager.patch_list[1])
                self.manager.omni_instance.patchIndex = 0
                self.manager.omni_instance.synth_sel(
                    self.manager.slots[1].text, OMNISYNTH_PATH)
            else:
                self.manager.slots[2].text = str(
                    self.manager.patch_list[self.manager.omni_instance.patchIndex])
                self.manager.omni_instance.patchIndex -= 1
                self.manager.slots[1].text = str(
                    self.manager.patch_list[self.manager.omni_instance.patchIndex])
                self.manager.slots[0].text = str(
                    self.manager.patch_list[self.manager.omni_instance.patchIndex - 1])
                self.manager.omni_instance.synth_sel(
                    self.manager.slots[1].text, OMNISYNTH_PATH)
