import kivy

from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
# from twilio.rest import Client
Window.size = (310, 580)

Login='''

'''

class KivyApp(MDApp):
    def build(self):
        return Builder.load_file("front.kv")

    def call_otp_page(self):
        print('hey')
        text = self.root.ids.textbox.text
        if len(text) != 0:
            print('The text box should not be empty')
        # elif len(text)==10:
        else:
            self.root.current = 'loginotp'

    def verify_otp(self):

        self.root.current = 'front_page'

    # def logger(self):

    def on_start(self):
        print("this method on start is fire!!!!")
    #
    # def on_stop(self):
    #     print("this method is called after the app is closed")

#
KivyApp().run()





