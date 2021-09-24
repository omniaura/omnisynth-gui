from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.uix.image import Image
from kivy.graphics import Rotate

class IndicatorImage(Image):
    def __init__(self, name):
        super().__init__()
        self.knob_name = name

        # When user touches a knob and drags, that one should be updated
        self.updateMe = False
        self.hold_value = 0
        with self.canvas.before:
            PushMatrix()
            self.rot = Rotate()
            self.rot.origin = self.center
            self.rot.angle = 0
            self.rot.axis = (0, 0, 1)
        with self.canvas.after:
            PopMatrix()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.updateMe = True
  
    # When the user releases from the screen, none of the knobs should update
    def on_touch_up(self, touch):
        self.updateMe = False

    def on_touch_move(self, touch):
        if self.updateMe:
            self.rot.origin = self.center
            self.hold_value -= touch.dx + touch.dy
            if self.hold_value > 155:
                self.rot.angle = 155
            else:
                if self.hold_value < -155:
                    self.rot.angle = -155
                else:
                    self.rot.angle = self.hold_value