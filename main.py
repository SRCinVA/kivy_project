from tkinter import VERTICAL
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):       # don't know why he's passing GridLayout
    count = 1                           # need to put the counter first
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")       # a custom property, for which we just want to see "1"
    
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

TheLabApp().run()
