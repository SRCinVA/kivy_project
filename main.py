from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class BoxLayoutExample(BoxLayout):
    def __init__(slef, **kwargs):
        super().__init__(**kwargs)  # he doesn't explain this line
        b1 = Button(text='A')
        b2 = Button(text='B')
        self.add_widget(b1)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
