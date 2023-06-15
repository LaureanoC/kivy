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
        self.add_widget(Label(text="Username: "))

        #Add InputBox de una sola linea multiline=false
        self.name = TextInput(multiline=False)
        
        #Add widget Input name
        self.add_widget(self.name)

        #Email
        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        #Password
        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        

        #Create submit button
        self.submit = Button(text="Submit", font_size=32)
        
        #Bind the button con una funcion llamada press
        self.submit.bind(on_press=self.press)

        self.add_widget(self.submit)

    def press(self, instance):
        #Asigno los valores de los inputs
        user = self.name.text
        email = self.email.text
        psw = self.password.text

        if self.validarVacios(user,email,psw):
            print("Usuario registrado")
            
        
    def validarVacios(user,email,psw):
        if len(user) == 0 or len(email)== 0 or len(psw) == 0:
            print("Rellenar los campos")
            return False
        return True

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()