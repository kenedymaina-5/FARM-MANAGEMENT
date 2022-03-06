from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class About(MDApp):
    def flip(self):
        print("working>>>>>>>>>>")
    def build(self):
        screen = MDScreen()
        
        #top toolbar
        self.toolbar = MDToolbar(title=" FARM MANAGER")
        self.toolbar.pos_hint ={"top":1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)
        
        #LOGO
        screen.add_widget(Image(
            source="logo fm.png",
            pos_hint = {"center_x": 0.5, "center_y": 0.7}
        ))
        
        #COLLECT USER INPUT
        self.input = MDTextField(
            text ="Enter you Email Adress",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.45},
             font_size=22
        
        )
        self.inputU =MDTextField(
            text = "Enter your Username",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5,  "center_y": 0.35},
            font_size=22
            
        )
        self.inputP = MDTextField(
            text = "Enter your Password",
            halign = "center",
            size_hint =(0.8 ,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.25},
            font_size = 22
        )
       
        screen.add_widget(self.input)
        screen.add_widget(self.inputU)
        screen.add_widget(self.inputP)
        return screen
    
    
if __name__ == '__main__':
    About().run()