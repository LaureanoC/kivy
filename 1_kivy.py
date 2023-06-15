import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #Set columns
        self.cols = 2

        #Add widgets
        self.add_widget(Label(text="Name: "))

        #Add InputBox de una sola linea multiline=false
        self.name = TextInput(multiline=False)
        
        #Add widget Input name
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favourite Color: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        #Create submit button
        self.submit = Button(text="Submit", font_size=32)
        
        #Bind the button con una funcion llamada press
        self.submit.bind(on_press=self.press)

        self.add_widget(self.submit)

    def press(self, instance):
        #Asigno los valores de los inputs
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'Hello {name} you like {pizza} and your favorite color is {color}!')

        self.add_widget(Label(text=f'Hello {name} you like {pizza} and your favorite color is {color}!'))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()