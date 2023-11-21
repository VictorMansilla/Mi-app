import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import until.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import Form_Login_Designer
from persistence.repository.auth_user_repository import Auth_User_Repository
from persistence.model import Auth_User
import until.encoding_decoding as end_cod
from forms.registration.form import FromRegister

class FormLogin(Form_Login_Designer):

    def __init__(self):
        self.auth_repository = Auth_User_Repository()
        super().__init__()

    def verificar(self):
        user_db:Auth_User=self.auth_repository.getUserByUserName(
            self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)

    def User_Register(self):
        FromRegister().mainloop()

    def isUser(self, user:Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(message="El usuario no existe, por favor registrarlo", title="No existe")
        return status
    
    def isPassword(self, password:str, user:Auth_User):
        b_password = end_cod.decrypt(user.password)
        if(password == b_password):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Contraseña incorrecta")
