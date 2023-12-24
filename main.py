import customtkinter
from PIL import Image

# Color's pallet
red = "#FF0000"
dark_red = "#CC0000"
blue = "#3B4CCA"
yellow = "#FFDE00"
golden = "#B3A125"
dark_green = "#0C3348"

app = customtkinter.CTk()
app.geometry("600x600")
app.title("CRUD Using Python and MongoDB")
app.configure(fg_color=blue)

my_image = customtkinter.CTkImage(light_image=Image.open("assets/pokeball.png"), size=(200, 200))
my_image_label = customtkinter.CTkLabel(app, text="", image=my_image)


def input():
    input_page = customtkinter.CTkToplevel(app)
    input_page.geometry("250x250")
    input_page.title("Login")
    input_page.configure(fg_color=dark_green)
    input_page.resizable(False, False)

    # Center the window both horizontally and vertically
    input_page.columnconfigure(0, weight=1)
    input_page.rowconfigure(0, weight=1)

    username = customtkinter.CTkLabel(input_page, text="Username")
    username.grid(row=1, padx=25, sticky="nsew")

    username_input = customtkinter.CTkEntry(input_page)
    username_input.grid(row=2, padx=25, sticky="nsew")

    password = customtkinter.CTkLabel(input_page, text="Password")
    password.grid(row=3, padx=25, sticky="nsew")

    password_input = customtkinter.CTkEntry(input_page)
    password_input.grid(row=4, padx=25, sticky="nsew")

    confirm = customtkinter.CTkButton(input_page, text="Login", hover_color="#ffcb05", text_color="black",
                                      border_spacing=2)

    # Center the button both horizontally
    confirm.grid(row=5, pady=25, padx=25, sticky="nsew")

# Testing popup
button = customtkinter.CTkButton(app, text="Click me", command=input)
button.grid()

app.mainloop()
