from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.text import LabelBase
from kivy.lang import Builder


Window.size = (400, 500)

LabelBase.register(
    name='raleway',
    fn_regular='fonts/raleway.ttf',
    fn_italic='fonts/raleway_italic.ttf',
    fn_bold='fonts/raleway_bold.ttf',
    fn_bolditalic='fonts/raleway_bold_italic.ttf'
)

class CryptoBox(AnchorLayout):
    
    crypto_name = StringProperty('')
    crypto_short_name = StringProperty('')
    image_path = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class FirstScreen(Screen):    
    pass

class MainContentFirst(BoxLayout):

    def add_crypto(self):
        a = CryptoBox()
        a.crypto_name = 'Misha'
        a.crypto_short_name = 'MSH'
        self.ids.crypto_slider.add_widget(a)
    

class OptionScreen(Screen):
    pass


class OptionCrypto(AnchorLayout):

    def update_state(self, widget):
        pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition(duration=0.2)
       

Builder.load_file('styles/firstscreen.kv')
Builder.load_file('styles/secondscreen.kv')
Builder.load_file('styles/thirdscreen.kv')
Builder.load_file('styles/optionscreen.kv')
        
main_app = Builder.load_file('styles/main.kv')

class MainApp(App):

    def build(self):
        return main_app

if __name__ == '__main__':
    MainApp().run()