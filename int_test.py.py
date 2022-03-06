# Code of Python Program

from kivymd.app import MDApp

class Myapp(MDApp):
    def build(self):
        return

Myapp().run()

MDScreen :
    md_bg_color : [1,0,0,1],
    radius : [25,0,25,0]
    MDLabel :
        text : "HELLO WORLD"
        halign : "center"
        theme_text_color : "Custom"
        text_color : [0,0,1,1]
        font_size : 50
        bold : True
        italic : True
