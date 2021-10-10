# Defining all the screens for ScreenManager
# from components.buttons.SlideButton import SlideButton
# from components.sliders.omniSlider import OmniSlider
# from components.images.indicatorImage import IndicatorImage
# from components.images.knobImage import KnobImage

from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

# The knob value page


class KnobValScreen(Screen):
    def on_pre_enter(self):
        self.manager.omni_instance.firstTime = False

    def slide_update(self, dt):
        # get all slider widgets
        children = self.walk()
        children_list = list(children)
        sliders = filter(lambda x: str(type(x)) == "<class 'kivy.factory.OmniSlider'>", children_list)

        for x in sliders:
            if x.name in self.manager.knob_coords:
                current_val = self.manager.omni_instance.omni_instance.knob_table[
                    self.manager.knob_coords[x.name]]
    # If the last value recorded by the gui slider movement event is different from the current value,
    # x.value should be set to current_val.
    # However, if the user moves the physical slider/knob and then attempts to set it back to that exact
    # value once again, the value would not be accurately depicted on the GUI.
    # This is why the "and not x.updateSliderOn" must be added
    #            if x.prev_val != current_val:
    #                x.value = current_val
                if x.prev_val != current_val and not x.update_slider_on:
                    x.update_slider_on = True
                if x.update_slider_on:
                    x.value = current_val

    def on_enter(self):
        self.slide_event = Clock.schedule_interval(self.slide_update, 1/60)
        self.manager.omni_instance.midi_learn_on = True
        self.manager.omni_instance.mapMode = False

    def on_pre_leave(self):
        self.slide_event.cancel()
        self.manager.omni_instance.midi_learn_on = False
        self.manager.omni_instance.mapMode = False

    def learn_midi(self):
        if self.manager.omni_instance.mapMode:
            self.manager.omni_instance.mapMode = False
        else:
            self.manager.omni_instance.mapMode = True
