from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior

from kivy.uix.gridlayout import GridLayout
from kivy.loader import Loader
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import platform
import json
import requests
import os
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

# import certifi
# import os

# # Here's all the magic !
# os.environ['SSL_CERT_FILE'] = certifi.where()

if platform == 'ios':
    from pyobjus import autoclass, objc_dict
    root_folder = App().user_data_dir
    CACHE_DIR = os.path.join(root_folder, 'cache')
    cache_folder = os.path.join(root_folder, 'cache')
    CACHE_DIR = cache_folder
    #CACHE_DIR = "Library/Caches"
    jsonDir = os.path.join(CACHE_DIR, "json")
    alternativeDir = "fonts"
    databaseDir = ""
else:
    CACHE_DIR = "cache"
    jsonDir = os.path.join(CACHE_DIR, "json")

    # IOS
    # databaseDir = ""
    # alternativeDir = "fonts"

class ImageButton(ButtonBehavior, AsyncImage):
    pass

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        # icon = AsyncImage(source='https://firebasestorage.googleapis.com/v0/b/crossplatform-44b4f.appspot.com/o/images%2Fbottle.jpg?alt=media&token=f560138d-0d19-452b-9d95-8f399cbca9f9')
        # self.add_widget(ImageButton(source= icon, allow_stretch=True, keep_ratio=False))
        pass


class GetWords(TextInput):
    def __init__(self, **kwargs):
        super(GetWords, self).__init__(**kwargs)
        pass


class CenteredAsyncImage(AsyncImage):
    def __init__(self, **kwargs):
        super(CenteredAsyncImage, self).__init__(**kwargs)
        # icon = 'https://firebasestorage.googleapis.com/v0/b/crossplatform-44b4f.appspot.com/o/images%2Fbottle.jpg?alt=media&token=f560138d-0d19-452b-9d95-8f399cbca9f9'
        pass


KV = Builder.load_string ("""

ScreenManager:
    id: manager
    Screen:
        MainWindow:
            orientation: 'vertical'

            GridLayout:
                cols:1
                size_hint: 1, 0.4


                # ImageButton:
                CenteredAsyncImage:
                    id: image_taken
                    text: ""
                    # size_hint_y: .9
                    source: ""
                    # size_hint: 0.5, None #width, height
                    back_color: (0, 0, 0, 1)
                    allow_stretch: True
                    keep_ratio: False
                        
                TextInput:
                    # size_hint_y: .1
                    text: '{"Robot A": {"List1": "Your Command1", "List2": "Your Command2"}}'
                    hint_text: '{"Parent": {"Child1": "Value", "Child2": "Value"}}'
                    id: JSON
                    back_color: 1,1,1,1
                    hint_text_color: 1,1,1,1
                    # background_color:(1,1,1,1)

            
            GridLayout:
                cols:1
                Button:
                    
                    text: "Your robot has found a bottle."
                    font_size: 32
                Button:
                    color: 0,0,0,5
                    font_size: 24

                    background_color:(1,1,1,1)
                    text: 'Command A'
                    on_release: app.patch(JSON.text)
                Button:
                    color: 0,0,0,5
                    background_color:(1,1,1,1)
                    font_size: 24

                    text: 'Command B'
                    on_release: app.post(JSON.text)
                Button:
                    color: 0,0,0,5
                    background_color:(1,1,1,1)
                    font_size: 24

                    text: 'Command C'
                    on_release: app.put(JSON.text)
                Button:
                    color: 0,0,0,5
                    background_color:(1,1,1,1)
                    font_size: 24

                    text: 'Command D'
                    on_release: app.delete(JSON.text)
                Button:
                    color: 0,0,0,5
                    background_color:(1,1,1,1)
                    font_size: 24

                    text: 'Command E'
                    on_release: app.get()
                GridLayout:
                    cols:1
                    Button:
                        
                        text: "Would you like to keep finding other bottles?"
                        font_size: 32
                GridLayout:
                    cols:2
                    
                    Button:
                        color: 0,0,0,5
                        background_color:(1,1,1,1)
                        font_size: 24

                        text: 'Yes'
                        on_release: 
                            app.order_yes()
                    Button:
                        color: 0,0,0,5
                        background_color:(1,1,1,1)
                        font_size: 24

                        text: 'No'
                        on_release: 
                            app.order_no()
                    
""")
#{"Parent": {"Child1": "Value", "Child2": "Value"}}
class MyApp(App):

    url = 'https://crossplatform-44b4f.firebaseio.com/users/xBjjv6LcanbE7BE8wpC7lJhwssC2/details/.json'
    auth_key = 'q2l2mXYVKGPUvGLISiGKECmOVPqyceS1QlVFPWNw' # Refer to the YouTube video on where to find this.

    


    def build(self):
        if platform == 'ios':
            Clock.schedule_once(self.finish_ios_init)

        return KV


    
    def on_start(self):
        # response = requests.get('https://firebasestorage.googleapis.com/v0/b/crossplatform-44b4f.appspot.com/o/images%2Fbottle.jpg?alt=media&token=f560138d-0d19-452b-9d95-8f399cbca9f9')
        # image = Loader.image('https://firebasestorage.googleapis.com/v0/b/crossplatform-44b4f.appspot.com/o/levy2.jpg?alt=media&token=54a4d612-26a3-4dee-b31e-7600debe4e2b')
        icon = 'https://firebasestorage.googleapis.com/v0/b/crossplatform-44b4f.appspot.com/o/images%2Fbottle.jpg?alt=media&token=f560138d-0d19-452b-9d95-8f399cbca9f9'
        # print("icon", icon)
        robotTaken = self.root.ids["image_taken"]
        robotTaken.source = icon
        # pass

    def finish_ios_init(self, *args):
        self.onesignal_object = autoclass("OneSignal")
        mock_launch_options = objc_dict({})
        self.onesignal_object.initWithLaunchOptions_appId_(mock_launch_options, "e180a14f-927a-40d1-87bf-4090c1118d76")

    def patch(self, JSON):
        to_database = json.loads(JSON)
        requests.patch(url = self.url, json = to_database)

    def post(self, JSON):
        to_database = json.loads(JSON)
        requests.post(url = self.url, json = to_database)

    def put(self, JSON):
        to_database = json.loads(JSON)
        requests.put(url = self.url, json = to_database)

    def delete(self, JSON):
        requests.delete(url = self.url[:-5] + JSON + ".json")

    def get(self):
        request = requests.get(self.url + '?auth=' + self.auth_key)
        print(request.json())

    def order_yes(self):

        print(1)

    def order_no(self):
        print(2)

    def text_taken(self):
        textJSON = self.root.ids["JSON"]
        haveText = textJSON.text
        print(haveText)

if __name__ == '__main__':
    MyApp().run()
