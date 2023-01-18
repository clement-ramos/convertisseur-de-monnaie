from tkinter import *
from tkinter import ttk

#My sized fonts
MAIN_CALC_FONT = ("Arial", 40, "bold")
SUB_CALC_FONT = ("Arial", 16)
BUTTONS_FONT = ("Arial", 20, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

#Colors that I use
WHITE = "#FFFFFF"
LIGHT_PURPLE = "#5764DD"
LIGHT_GRAY = "#F8F9FB"
GRAY = "#C8C8C8"
DARK_GRAY = "#38444B"


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Def of my functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def convert():

    validate_amount = amount.get()  #Amount (String)

    try:
        validate_amount_float = float(validate_amount) # amount in float

        first_currency = starting_currency.get()    #name of the first currency
        last_currency = final_currency.get()        #name of the second currency

        USD_amount = (validate_amount_float / float(rate_from_USD_to[first_currency]))
        result.set(str(USD_amount * float(rate_from_USD_to[last_currency])))

        add_to_historic(validate_amount_float, first_currency, last_currency, (USD_amount * float(rate_from_USD_to[last_currency])))
        

    except ValueError: 
        print("The only available inputs are numbers")

def add_to_historic(validate_amount_float, first_currency, last_currency, result):
    historic.append((validate_amount_float, first_currency, result, last_currency))
    print(historic)
    update_historic_display()


def update_historic_display():
    sub.delete(0, END)
    for element in historic:
        #string_insert = historic[element][0] + historic[element][1] + " worth " + historic[element][3] + historic[element][2]
        sub.insert(END, element)
        

def clear_historic():
    global historic
    historic = []
    update_historic_display()
#     
#     for validate_amount_float, first_currency, last_currency in historic:
#         sub.insert(END, validate_amount_float + first_currency + " worth " + result + last_currency)
#     sub.config(yscrollcommand=scrollbar.set)
#     scrollbar.config(command=sub.yview)
    
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Driver Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# create a GUI window
gui = Tk()
# set the configuration of GUI window
gui.geometry("400x720")             # set a default size
gui.resizable(False, False)
gui.config(bg=DARK_GRAY)
gui.title("Currency Converter")      # set the title of GUI window

result = StringVar()
historic = []

#Displaying my historic
sub = Listbox(gui)
sub.pack(side = TOP, fill=BOTH)
scrollbar = Scrollbar(sub)
scrollbar.pack(side=RIGHT, fill='both')

labelChoix = Label(gui, text = "Select an amount and your currencies!", pady=10)
labelChoix.pack()

amount = Entry(gui)     #Text input box
amount.pack(side = TOP)

#Create the list with all the currencies and ther ratio (USD to "the currency")
rate_from_USD_to={"USD":1, "EUR":1.08, "GBP":0.8171, "JPY":128.525, "AED":3.67244}
currencies = [i for i in rate_from_USD_to]
    
#Create the 2 combo boxes to choose currencies
starting_currency = ttk.Combobox(gui, values=currencies)
starting_currency.pack(side = TOP)
starting_currency.current(0)
starting_currency.bind("<<ComboboxSelected>>")
starting_currency.pack()

final_currency = ttk.Combobox(gui, values=currencies)
final_currency.pack(side = TOP)
final_currency.current(0)
final_currency.bind("<<ComboboxSelected>>")

#Convert button who call convert()
convert_button = Button(gui, text="Convert !", command=convert)
convert_button.pack(side=TOP)

#Displaying the result
label_result_title = Label(gui, text = "Result :")
label_result_title.pack()

label_result = Label(gui, textvariable=result)
label_result.pack(side=TOP)

#Convert button who call convert()
convert_button = Button(gui, text="Clear historic", command=clear_historic)
convert_button.pack(side=TOP)

#Display GUI
gui.mainloop()