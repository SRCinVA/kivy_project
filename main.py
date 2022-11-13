from curses.textpad import rectangle
from tkinter import VERTICAL
from tokenize import String
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy import metrics
from kivy.core.window import Window
# from kivy.lang import Builder
from kivy.uix.widget import Widget

# Builder.load_file("thelab.kv")

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):  # you could code a loop her to display many shapes in the canvas.
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:   # write the canvas instructions here
            Line(points=(100, 100, 400, 500), width=2)  # had to import Line up top.
            Color(0,1,0 )
            Line(circle=(400, 200, 80), width=2) # circle is a property, so it needs an equal sign
            Line(rectangle=(700, 500, 150, 100), width = 5)
            self.rect = Rectangle(pos=(700,200), size=(150,100)) # turn this into an instance variable, so you can use it in def on_button_a_click()

    def on_button_a_click(self):
        # print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size # size of the rectangle itself
        inc = dp(10) # the "increment" of movement
        
        diff = self.width - (x+w) # whatever the x position (bottom left corner) plus the lower base of the rectangle. self.width is for the entire screen and it always updates.
        if diff <= inc: # not sure I see how this one works
            inc = diff
        x += inc # with this change, we are constantly updating the tuple, because tuples are immutable
        self.rect.pos = (x, y)# goal is to change position of the rectangle.

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:   # write the canvas instructions here
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            Clock.schedule_interval(self.update, 1/60) # gets the ball to move automatically, wiht intervals by seconds.
    
    def on_size(self, *args):
        # print("on size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):  # 'dt' is delta time, which is required for all functions that use 'schedule'
        x, y = self.ball.pos # note that you defined 'self.ball.pos' in the previous function.
        
        x += self.vx
        y += self.vy
        
        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy  # this is the rebound from the wall.

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx 

        if y < 0:
            y = 0
            self.vy = -self.vy  # shouldn't this be "+ self.vy"?

        if x < 0:
            x = 0
            self.vx = -self.vx


        self.ball.pos = (x, y)

class WidgetsExample(GridLayout):       # don't know why he's passing GridLayout
    count = 1                           # need to put the counter first
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")       # a custom property, for which we just want to see "1"
    text_input_str = StringProperty("foo") # the default, which we can change later
    # slider_value_text = StringProperty("Value")  # this is just a default for before we start moving the slider.

    def on_button_click(self):          # we're doing this to manage the button click
        print("Button clicked")         # to test if the method is working
        if self.count_enabled == True:  # this has to actually be "ON" (changed to "True" down below) for 'count' to increment at all.
            self.count += 1                 # use self., b/c we want it to refer to the overall class, which is where we defined the variable.
            self.my_text = str(self.count)  # if you forgot 'self,' my_text would just be a local variable and (I suspect) would *not* be applied to Widget (which is what we prefer)

    def on_toggle_button_state(self, widget):   # remember to pass 'self' here as well
        print("toggle state: " + widget.state)  # above, 'self' refers to the Widget class; 'widget' refers to the toggle button from the kivy file (could have used 'toggle_button', as an example). We will do this frequently. 
                                                # above, this property will tell us if the toggle has been activated. 
        if widget.state == "normal":
            widget.text = "OFF"          # with .text property, we directly change the widget's text itself
            self.count_enabled = False   # this is change the Boolean one way or another
        else:
            widget.text = "ON"
            self.count_enabled = True    # this is change the Boolean one way or another

    def on_switch_active(self, widget): # 'self' refers to the Widget class; 'widget' refers to the switch from the kivy file.
        print("Switch:" + str(widget.active))  # the .active property of the widget is a Boolean, so we'll need to convert it into a string.

    def on_text_validate(self, widget):
        self.text_input_str = widget.text  # (possibly): the var tex_input_str is set equal to the input in the text box

    # def on_slider_value(self, widget):  with the ID in place fo the slider, we don't need this line anymore.
    #   print("Slider: " + str(int(widget.value)))  # it was a float, but we wanted an int.
    #   self.slider_value_text = str(int(widget.value))

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs): # this is the basic form for the constructor
        super().__init__(**kwargs)
        # self.orientation = "lr-bt" this overrides the rl-tb default pattern.
        for i in range(0,100):  # you can create buttons with a loop as well
            size = dp(100) # here, 'size' is just a local variable, not a property
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size)) # we ran __init__ for Z, so it displayed first; then, the other buttons display.
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#   pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #    super().__init__(**kwargs)  # he doesn't explain this line
    #    self.orientation = VERTICAL 
    #    b1 = Button(text='A') # the order is important
    #    b2 = Button(text='B')
    #    b3 = Button(text='C')
    #    self.add_widget(b1) # this says that we can add a widget inside this layout.
    #    self.add_widget(b2)
    #    self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

TheLabApp().run()
