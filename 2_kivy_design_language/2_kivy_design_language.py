import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

#Para que funcione desde el my.kv los id
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    
    #Inicializo
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    #No necesito el instance como parametro
    def press(self):
        #Asigno los valores de los inputs
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'Hello {name} you like {pizza} and your favorite color is {color}!')

        # Clear
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()