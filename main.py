from tkinter import VERTICAL
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


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
