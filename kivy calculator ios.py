from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton, MDRoundFlatButton, MDRectangleFlatButton, MDRaisedButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.scrollview import MDScrollView

class IOS(MDApp):
    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray" 
        scr = MDScreen()
        
        self.button1 = MDRectangleFlatButton(text = '*', _text_color = 'red', md_bg_color =  (100/255,100/255,100/255,1),
                                        pos_hint = {'center_x':0.88, 'center_y': 0.557},
                                        font_size = '30sp',theme_text_color = None,
                                        text_color = (1,1,1,1),
                                        on_press = self.vurma)

        
        self.button2 = MDRectangleFlatButton(text = '/', _text_color = 'red',  md_bg_color =  (100/255,100/255,100/255,1),
                                        pos_hint = {'center_x':0.66, 'center_y': 0.557},
                                        font_size = '30sp',theme_text_color = None,
                                        text_color = (1,1,1,1),
                                        on_press = self.bolme)
        
        self.button3 = MDRectangleFlatButton(text = '+', _text_color = 'red',  md_bg_color =  (100/255,100/255,100/255,1),
                                        pos_hint = {'center_x':0.44, 'center_y': 0.557},
                                        font_size = '30sp',theme_text_color = None,
                                        text_color = (1,1,1,1),
                                        on_press = self.toplama)
        
        self.button4 = MDRaisedButton(text = 'AC', _text_color = 'red',
                                        pos_hint = {'center_x':0.17, 'center_y': 0.57},
                                        font_size = '50sp',
                                        text_color = (1,163/255,19/255,1),
                                        md_bg_color=(245/255, 135/255, 15/255, 1),
                                        theme_text_color="Primary",
                                        on_press = self.dele)
        
        self.button5 = MDRectangleFlatButton(text = '-', _text_color = 'red',  md_bg_color =  (100/255,100/255,100/255,1),
                                        pos_hint = {'center_x':0.875, 'center_y': 0.44},
                                        font_size = '30sp',theme_text_color = None,
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        on_press = self.ferq)
        
        self.button6 = MDRectangleFlatButton(text = '=', _text_color = 'red',
                                        pos_hint = {'center_x':0.875, 'center_y': 0.205},
                                        font_size = '30sp',
                                        size_hint = (0.21,0.3),
                                         md_bg_color =  (245/255, 135/255, 15/255, 1),
                                        theme_text_color = 'Primary',
                                        text_color = (1,1,1,1),
                                        on_press = self.beraber)
        
        self.button0_ = MDRectangleFlatButton(text = '0', _text_color = 'red',md_bg_color = (146/255,146/255,146/255,1),
                                        pos_hint = {'center_x':0.28, 'center_y': 0.09},
                                        font_size = '30sp',theme_text_color = None,
                                        text_color = (1,1,1,1),
                                        size_hint = (0.5,0.01),
                                        on_press = self.func0)
        
        self.button_vergul = MDRectangleFlatButton(text = '.', _text_color = 'red',  md_bg_color =  (100/255,100/255,100/255,1),
                                        pos_hint = {'center_x':0.65, 'center_y': 0.09},
                                        font_size = '30sp',theme_text_color = None,
                                        text_color = (1,1,1,1),
                                        size_hint = (0.05,0.05),
                                        on_press = self.vergul)
        
        self.button1_ = MDRectangleFlatButton(text = '1', _text_color = 'red',
                                        pos_hint = {'center_x':0.15, 'center_y': 0.2},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func1)
        
        self.button2_ = MDRectangleFlatButton(text = '2', _text_color = 'red',
                                        pos_hint = {'center_x':0.39, 'center_y': 0.2},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func2)
        
        self.button3_ = MDRectangleFlatButton(text = '3', _text_color = 'red',
                                        pos_hint = {'center_x':0.63, 'center_y': 0.2},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func3)
        
        
        self.button4_ = MDRectangleFlatButton(text = '4', _text_color = 'red',
                                      pos_hint = {'center_x':0.15, 'center_y': 0.32},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func4)  
        self.button5_ = MDRectangleFlatButton(text = '5', _text_color = 'red',
                                        pos_hint = {'center_x':0.39, 'center_y': 0.32},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func5)
        
        self.button6_ = MDRectangleFlatButton(text = '6', _text_color = 'red',
                                        pos_hint = {'center_x':0.63, 'center_y': 0.32},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func6)
        
        self.button7_ = MDRectangleFlatButton(text = '7', _text_color = 'red',
                                      pos_hint = {'center_x':0.15, 'center_y': 0.44},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func7)  
        
        self.button8_ = MDRectangleFlatButton(text = '8', _text_color = 'red',
                                      pos_hint = {'center_x':0.39, 'center_y': 0.44},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func8) 
        
        self.button9_ = MDRectangleFlatButton(text = '9', _text_color = 'red',
                                      pos_hint = {'center_x':0.63, 'center_y': 0.44},
                                        font_size = '30sp',
                                        text_color = (1,1,1,1),
                                        size_hint = (0.2,0.1),
                                        md_bg_color = (146/255,146/255,146/255,1),
                                        on_press = self.func9) 

        self.Screen = MDTextField(pos_hint = {'center_x':0.5, 'center_y': 0.7},
                                  font_size = '50sp',
                                  line_color_normal = (19/255,19/255,19/255,1),
                                  line_color_focus = (19/255,19/255,19/255,1),
                                  opacity = '5')
        self.buton_icon = MDIconButton(icon = 'delete-empty-outline',
                                       pos_hint = {'center_x' : 0.94, 'center_y': 0.62},
                                       on_press = self.backspace)
        
        scr.add_widget(self.buton_icon)
        scr.add_widget(self.Screen)    
        scr.add_widget(self.button2)
        scr.add_widget(self.button1)
        scr.add_widget(self.button3)
        scr.add_widget(self.button4)
        scr.add_widget(self.button5)
        scr.add_widget(self.button6)
        scr.add_widget(self.button0_)
        scr.add_widget(self.button_vergul)
        scr.add_widget(self.button1_)
        scr.add_widget(self.button2_)
        scr.add_widget(self.button3_)
        scr.add_widget(self.button4_)
        scr.add_widget(self.button5_)
        scr.add_widget(self.button6_)
        scr.add_widget(self.button7_)
        scr.add_widget(self.button8_)
        scr.add_widget(self.button9_)
        
        return scr
    def func9(self,obj):
       self.Screen.insert_text(self.button9_.text)
        
    def func8(self,obj):
      self.Screen.insert_text(self.button8_.text)
      
    def func7(self,obj):
      self.Screen.insert_text(self.button7_.text) 
      
    def func6(self,obj):
      self.Screen.insert_text(self.button6_.text) 
      
    def func5(self,obj):
      self.Screen.insert_text(self.button5_.text) 
      
    def func4(self,obj):
      self.Screen.insert_text(self.button4_.text) 
      
    def func3(self,obj):
      self.Screen.insert_text(self.button3_.text) 
      
    def func2(self,obj):
      self.Screen.insert_text(self.button2_.text) 
      
    def func1(self,obj):
      self.Screen.insert_text(self.button1_.text) 
      
    def func0(self,obj):
      self.Screen.insert_text(self.button0_.text) 
      
    def vurma(self,obj):
      self.Screen.insert_text(self.button1.text)
      
    def vergul(self,obj):
      self.Screen.insert_text(self.button_vergul.text) 
      
    def beraber(self,obj):
      
      try:
        result = eval(str(self.Screen.text))
        self.Screen.select_all()
        self.Screen.delete_selection()
        self.Screen.insert_text(str(result))
        
      except:
        self.Screen.select_all()
        self.Screen.delete_selection()
        self.Screen.insert_text('Error')
      
      
    def ferq(self,obj):
      self.Screen.insert_text(self.button5.text)
      
    def dele(self,obj):
      self.Screen.select_all()
      self.Screen.delete_selection()
      
    def toplama(self,obj):
      self.Screen.insert_text(self.button3.text)
      
    def bolme(self,obj):
      self.Screen.insert_text(self.button2.text)
      
    def backspace(self,obj):
      try:
        str1 = list(self.Screen.text)
        del str1[-1]
        str2 = ''.join(str1)
        self.Screen.select_all()
        self.Screen.delete_selection()
        self.Screen.insert_text(str(str2))
      except:
        self.Screen.insert_text('Error')
      
      if self.Screen.text == 'Error':
        self.Screen.select_all()
        self.Screen.delete_selection()
        
if __name__ == '__main__':
    Window.size = (350,700)
    IOS().run() 