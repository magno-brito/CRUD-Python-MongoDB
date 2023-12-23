
import customtkinter
from PIL import Image


#Color's pallet
#

red = "#FF0000"
dark_red = "#CC0000"
blue = "#3B4CCA"
yellow = "#FFDE00"
golden = "#B3A125"

app = customtkinter.CTk()
app.geometry("600x600")
app.title("CRUD Using Python and MongoDB")
app.configure(fg_color=blue)
# app.resizable(height=False, width=False)

my_image = customtkinter.CTkImage(light_image=Image.open("assets/pokeball.png"), size=(200,200))

my_image_label = customtkinter.CTkLabel(app, text="", image=my_image)
my_image_label.pack(pady=100)

def input():
    input_page = customtkinter.CTkToplevel(app)
    input_page.geometry("300x400")
    input_page.title("Login")
    input_page.configure(fg_color=red)

    username = customtkinter.CTkLabel(input_page,text="Username")
    username.pack()
    username_input = customtkinter.CTkEntry(input_page)
    username_input.pack()

    password = customtkinter.CTkLabel(input_page,text="password")
    password.pack()
    password_input = customtkinter.CTkEntry(input_page)
    password_input.pack()

    confirm = customtkinter.CTkButton(input_page, text="Login",
                                      hover_color="#ffcb05",
                                      text_color="black")
    confirm.pack()

    

#Testing popup
button = customtkinter.CTkButton(app, text="Click me", command=input)
button.pack(pady=20)






app.mainloop()



