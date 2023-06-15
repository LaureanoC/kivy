import kivy
from kivy.app import App
from kivy.uix.widget import Widget

#Para designar la el directorio
from kivy.lang import Builder

#Designate our kv design file
Builder.load_file('progress.kv')

#Para que funcione desde el my.kv los id
from kivy.properties import ObjectProperty

class MyLayout(Widget):
    
    def press_it(self):
        
        #Grab the current progress bar value
        current = self.ids.my_progress_bar.value
       
        if current == 1 :
            current = 0

        current += .25
        #Update the progress bar
        self.ids.my_progress_bar.value = current

        #Update the label
        self.ids.my_label.text = f'{int(current*100)}% Progress'


        

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()