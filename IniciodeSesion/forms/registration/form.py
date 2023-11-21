from forms.registration.fomr_registration import FormRegisterDesigner
from persistence.repository.auth_user_repository import Auth_User_Repository
from persistence.model import Auth_User
from tkinter import messagebox
import until.encoding_decoding as end_cod
import tkinter as tk

class FromRegister(FormRegisterDesigner):

    def __init__(self):
        self.auth_repository = Auth_User_Repository()
        super().__init__()

    def register(self):
        if(self.isConfirmationPassword()):
            user = Auth_User()
            user.username = self.usuario.get()
            user_db:Auth_User = self.auth_repository.getUserByUserName(self.usuario.get())
            if not (self.isUserRegister(user_db)):
                user.password = end_cod.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showerror(message="Se registro el usuario", title="Registro Usuario")
                self.ventana.destroy()

    def isConfirmationPassword(self):
        status:bool = True
        if(self.password.get() != self.confirmation.get()):
            status = False
            messagebox.showerror(message="La contraseñas no coinciden por favor verificar el registro", title="No coinciden")
            self.password.delete(0, tk.END)
            self.confirmation.delete(0, tk.END)
        return status
    
    def isUserRegister(self, user:Auth_User):
        status:bool = False
        if(user != None):
            status = True
            messagebox.showerror(message="El usuario ya existe", title="Ya existe")
        return status