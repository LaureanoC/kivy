import kivy
from kivy.app import App
from kivy.uix.widget import Widget
#Para que funcione desde el my.kv los id
from kivy.properties import ObjectProperty
#Para designar la el directorio
from kivy.lang import Builder

#Designate our kv design file
Builder.load_file('register.kv')

class MyLayout(Widget):

    estadoUser = False
    estadoEmail = False
    estadoPassword = False
    estadoPasswordDos = False

    user = ObjectProperty(None)
    email = ObjectProperty(None)
    psw = ObjectProperty(None)
    pswdos = ObjectProperty(None)
    
    def validarIgualdad(self,a,b):
        return a == b

    def validarVacios(self,user,email,psw,pswdos):
        if len(user) == 0 or len(email) == 0 or len(psw) == 0 or len(pswdos) == 0:
            return False
        return True
    def sumarProgress(self):
        #Grab the current progress bar value
        current = self.ids.my_progress_bar.value
       
        current += .25
        #Update the progress bar
        self.ids.my_progress_bar.value = current

    def restarProgress(self):
        #Grab the current progress bar value
        current = self.ids.my_progress_bar.value
       
        current -= .25
        #Update the progress bar
        self.ids.my_progress_bar.value = current

    def press(self):
        #Asigno los valores de los inputs
        user = self.ids.user.text
        email = self.ids.email.text
        psw = self.ids.psw.text
        pswdos = self.ids.pswdos.text

    def changeLabel(self):
        #Grab the current progress bar value
        current = self.ids.my_progress_bar.value
        self.ids.label.text = f'{int(current*100)}% Progress'

        
    def changeUser(self):
        if(len(self.ids.user.text) != 0 and self.estadoUser == False):
            self.estadoUser = True
            self.sumarProgress()
        elif len(self.ids.user.text) == 0:
            self.estadoUser = False
            self.restarProgress()
        
    def changeEmail(self):
        if(len(self.ids.email.text) != 0 and self.estadoEmail == False):
            self.estadoEmail = True
            self.sumarProgress()
        elif len(self.ids.email.text) == 0:
            self.estadoEmail = False
            self.restarProgress()

    def changePassword(self):
        if(len(self.ids.psw.text) != 0 and self.estadoPassword == False):
            self.estadoPassword = True
            self.sumarProgress()
        elif len(self.ids.psw.text) == 0:
            self.estadoPassword = False
            self.restarProgress()
        
    def changeConfirmPassword(self):
        if self.validarIgualdad(self.ids.psw.text, self.ids.pswdos.text) and self.estadoPasswordDos == False:
            self.estadoPasswordDos = True
            self.sumarProgress()

        if(self.validarIgualdad(self.ids.psw.text, self.ids.pswdos.text) == False and self.estadoPasswordDos == True):
            self.estadoPasswordDos = False
            self.restarProgress()


        
        
        
class RegisterApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    RegisterApp().run()