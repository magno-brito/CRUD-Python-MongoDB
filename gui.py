
import customtkinter

app = customtkinter.CTk()
app.geometry("600x600")
app.title("CRUD Using Python and MongoDB")
app.configure(fg_color="green")
# app.resizable(height=False, width=False)

canvas = customtkinter.CTkCanvas(
    app,
    width=200,
    height=200,
    bg="red"

)

def diz_ola():
    print("OLá")

button = customtkinter.CTkButton(app, width=100, height=100, text="Button", command=diz_ola, anchor="nw")
button.grid()

label = customtkinter.CTkLabel(app, text="Olá", fg_color="transparent")
label.grid()

entry = customtkinter.CTkEntry(app, placeholder_text="Input data")
entry.grid()

checkbox = customtkinter.CTkCheckBox(app, text="CheckBox", onvalue="on", offvalue="off")
checkbox.grid()


combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"])
combobox.grid()

frame = customtkinter.CTkFrame(master=app, width=200, height=200, fg_color="red")
frame.grid()

option_menu = customtkinter.CTkOptionMenu(app, values=["A","B","C","D"])
option_menu.grid()

progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal")
progressbar.grid()

radio_button = customtkinter.CTkRadioButton(app, text="Radio Button ")
radio_button.grid()

scroll_bar_frame = customtkinter.CTkScrollableFrame(app, width=20, height=20)
scroll_bar_frame.grid()

scroll_bar = customtkinter.CTkScrollbar(app)
scroll_bar.grid(row=0,column=1)

segmentation_button = customtkinter.CTkSegmentedButton(app, values=["1","2","3"])
segmentation_button.grid(row=1, column=2)

slider = customtkinter.CTkSlider(app, from_=0, to=100)
slider.grid(row=0,column=3)

switch_var = customtkinter.CTkSwitch(app, text="Switch", onvalue="on", offvalue="off")
switch_var.grid(row=0, column=4)

tabview = customtkinter.CTkTabview(master=app)
tabview.grid(row=0,column=5)
tabview.add("tab 1")
tabview.add("tab 2")
tabview.add("tab 3")

textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0","Funcionando")
textbox.grid(row=0, column=6)



app.mainloop()



