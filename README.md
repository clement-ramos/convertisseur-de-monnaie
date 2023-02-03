# Currency Converter

This is a Python script that creates a GUI currency converter application using Tkinter. The currency rates are stored in a JSON file, which is loaded into the script and saved to the same file whenever a new currency and rate are added to the converter. The application has three tabs: "Convert", "Add", and "Historic".

    The "Convert" tab has an entry field to input the amount of money to be converted and two dropdown menus to select the currencies to be converted from and to. The conversion is done by dividing the amount by the rate of the first currency to USD, then multiplying that amount by the rate of the second currency to USD. The result of the conversion is displayed on the tab.

    The "Add" tab has two entry fields for the currency name and rate, and a button to add the currency to the converter. The user can only add a currency if the name and rate fields are filled and if the rate is a valid decimal number. The names of the currencies in the converter are updated in the dropdown menus in the "Convert" tab.

    The "Historic" tab shows the history of all conversions made and has a button to clear the history.

The script uses the re library to check if the rate entered is a valid decimal number, the tkinter library for the GUI, and the tkinter.ttk library for the notebook widget that displays the tabs.
