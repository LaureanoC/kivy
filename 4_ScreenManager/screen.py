from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty


class FormScreen(Screen):
    
    estadoUser = False
    estadoEmail = False
    estadoPass = False
    estadoConfirm = False

    def validarIgualdad(self,a,b):
        return a == b

    def validarVacios(self,user,email,psw,pswdos):
        if len(user) == 0 or len(email) == 0 or len(psw) == 0 or len(pswdos) == 0:
            return False
        return True

    def changeUser(self):
        text = self.ids.user.text

        if len(text) != 0 and self.estadoUser == False:
            self.estadoUser = True
            self.sumarProgress()
        elif self.estadoUser == True:
            self.estadoUser = False
            self.restarProgress()


    def changeEmail(self):
        text = self.ids.email.text

        if len(text) != 0 and self.estadoEmail == False:
            self.estadoEmail = True
            self.sumarProgress()
        elif self.estadoEmail == True:
            self.estadoEmail = False
            self.restarProgress()

    def changePass(self):
        text = self.ids.password.text

        if len(text) != 0 and self.estadoPass == False:
            self.estadoPass = True
            self.sumarProgress()
            
        elif self.estadoPass == True:
            self.estadoPass = False
            self.restarProgress()

    def changeConfirm(self):
        text = self.ids.confirm_password.text

        if self.validarIgualdad(text, self.ids.password.text):
            print("Son iguales")
            self.estadoConfirm = True
            self.sumarProgress()
        elif self.estadoConfirm == True:
            self.estadoConfirm = False
            self.restarProgress()
        



    def sumarProgress(self):
        current = self.ids.my_progress_bar.value
        current += .25
        self.ids.my_progress_bar.value = current

    def restarProgress(self):
        current = self.ids.my_progress_bar.value
        current -= .25
        self.ids.my_progress_bar.value = current

    def changeLabel(self):
        current = self.ids.my_progress_bar.value
        self.ids.label.text = f'{int(current*100)}% Progress'

    def changeScreen(self):
        
        if(self.estadoUser and self.estadoEmail and self.estadoPass and self.estadoConfirm):
            self.parent.current = 'home'
        


class HomeScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

    
kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()