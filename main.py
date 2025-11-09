"""."""

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainScreen(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MainApp().run()
