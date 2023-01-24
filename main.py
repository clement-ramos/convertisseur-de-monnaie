import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

#My sized fonts
DEFAULT_FONT_STYLE = ("Arial", 14)

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Def of my functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def convert():

    amount = amount_entry.get() #Amount (String)

    try:
        amount_float = float(amount) # amount in float

        first_currency = currency_in.get()    #name of the first currency
        last_currency = currency_out.get()        #name of the second currency

        amount_in_USD = (amount_float / float(rate_from_USD_to[first_currency]))
        amount_converted = round((amount_in_USD * float(rate_from_USD_to[last_currency])), 2)
        result_label.config(text=f"{amount} {first_currency} is equal to {amount_converted} {last_currency}")

        historic_list.insert(END, f"{amount} {first_currency} is equal to {amount_converted} {last_currency}")
        

    except ValueError: 
        print("The only available inputs are numbers")


def clear_historic():
    historic_list.delete(0, END)


def add_currency():
    
    new_currency = name_entry.get()
    new_rate = rate_entry.get()
        
    # Check if inputs are not completed
    if not new_currency or not new_rate:
        messagebox.showerror("Error", "Please enter a currency and rate.")
        return
    # Check if the name already exist
    if new_currency in rate_from_USD_to:
        messagebox.showerror("Error", "This name is already used.")
        return
    # Check if the new rate as a valid type
    if not re.match("^\d*\.\d+|\d+$", new_rate):
        messagebox.showerror("Error", "Please enter a valid decimal number for the rate.")
        return
    # add the new currency and rate to the rates dictionary
    rate_from_USD_to[new_currency] = float(new_rate)
    messagebox.showinfo("Success", "Currency added successfully.")
    
    # Update the currency_in and currency_out Combobox values
    currency_in['values'] = list(rate_from_USD_to.keys())
    currency_out['values'] = list(rate_from_USD_to.keys())
    
    #Update the JSON to keep it even if you close the window
    with open('data.json', 'w') as outfile:
        json.dump(rate_from_USD_to, outfile)

    # Clear the currency and rate Entry
    name_entry.delete(0, END)
    rate_entry.delete(0, END) 

  
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gui General ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
gui = Tk()
gui.title("Currencies Converter")
gui.geometry("400x550")
gui.resizable(False, False)

file = open('data.json')
rate_from_USD_to=json.load(file)
currencies = [i for i in rate_from_USD_to]

pages = ttk.Notebook(gui)
pages.pack()

#Create my 3 MAIN Frame
# Currency Frame
convert_frame = Frame(gui, width=480, height=480)
convert_frame.pack(fill="both", expand=1)

# Conversion Frame
add_currency_frame = Frame(gui, width=480, height=480)
add_currency_frame.pack(fill="both", expand=1)

# Historic Frame
historic_frame = Frame(gui, width=480, height=480)
historic_list = Listbox(historic_frame, font=DEFAULT_FONT_STYLE)
historic_list.pack(fill="both", expand=1)

clear_historic = Button(historic_frame, text="Clear History", command=clear_historic)
clear_historic.pack()

# Add the Tabs
pages.add(convert_frame, text="Convert")
pages.add(add_currency_frame, text="Add")
pages.add(historic_frame, text="Historic")


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frame Converter ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#Create my TOP Frame
amount_L_frame = LabelFrame(convert_frame , text="Amount to convert", font=DEFAULT_FONT_STYLE)
amount_L_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Create an entry for the amount to convert
amount_entry = Entry(amount_L_frame, font=DEFAULT_FONT_STYLE)
amount_entry.grid(row=1, column=0, padx=60, pady=20, sticky="nsew")


#Create my CENTER Frame
currencies_L_frame = LabelFrame(convert_frame, text="Currencies to convert", font=DEFAULT_FONT_STYLE)
currencies_L_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

#Combo box for the (inner currency)
currency_in = ttk.Combobox(currencies_L_frame, values=currencies, font=DEFAULT_FONT_STYLE, justify=RIGHT)
currency_in.grid(row=1, column=0, padx=50, pady=15)

#Combo box for the (output currency)
currency_out = ttk.Combobox(currencies_L_frame, values=currencies, font=DEFAULT_FONT_STYLE, justify=RIGHT)
currency_out.grid(row=2, column=0, padx=50, pady=15)

# Create a convert button
convert_button = ttk.Button(currencies_L_frame, text="Convert", command=convert)
convert_button.grid(row=3, column=0, padx=10, pady=10)


#Create my BOTTOM Frame
result_L_frame = LabelFrame(convert_frame, text="Result : ", font=DEFAULT_FONT_STYLE)
result_L_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

# Create a label to display the result
result_label = Label(result_L_frame, font=DEFAULT_FONT_STYLE)
result_label.grid(row=0, column=0, padx=50, pady=20, sticky="nsew")

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frame add currency ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#Create my Frame who contain my elements
add_currency_L_frame = LabelFrame(add_currency_frame, text="Add currency", font=DEFAULT_FONT_STYLE)
add_currency_L_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

#Inputs with his label to write the NAME of the currency
Label(add_currency_L_frame,text="Name").grid(row=0, column=0, padx=10)
name_entry = Entry(add_currency_L_frame, font=DEFAULT_FONT_STYLE)
name_entry.grid(row=0, column=1, pady=20, padx=40, sticky="nsew")

#Inputs with his label to write the RATE of the currency
Label(add_currency_L_frame,text="Rate").grid(row=1, column=0,padx=10)
rate_entry = Entry(add_currency_L_frame, font=DEFAULT_FONT_STYLE)
rate_entry.grid(row=1, column=1, pady=20, padx=40, sticky="nsew")

#Create the button who ADD the currency to JSON
add_currency_button = Button(add_currency_L_frame,text="Add", command=add_currency, font=DEFAULT_FONT_STYLE)
add_currency_button.grid(row=2, column=0, padx=60, pady=20, columnspan=2, sticky="nsew")

gui.mainloop()