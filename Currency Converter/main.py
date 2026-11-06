import tkinter as tk
from tkinter import ttk
import requests

def convert_currency(amount, from_currency, to_currency):
    #API
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if to_currency in data['rates']:
            rate = data['rates'][to_currency]
            converted_amount = amount * rate
            return converted_amount
        else:
            raise ValueError("Invalid target currency.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def on_click():
    #input values
    amount = float(entry.get())
    from_currency = currencychosen.get()
    to_currency = currencychosen2.get()

    #conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)

    #display result
    if converted_amount is not None:
        label2.config(text=f"{converted_amount:.2f} {to_currency}")
    else:
        label2.config(text="Error: Invalid currency or conversion failed.")

#main window
root = tk.Tk()
root.title("Currency Converter")  #title
root.geometry("300x200")  # Width x Height

#label
label = ttk.Label(root, text="Input Amount:", font=("Arial", 14))
label.pack(pady=20)  # Position with vertical padding

#convert button
button = ttk.Button(root, text="Convert", command=on_click)
button.pack(pady=10)

#entry textbox
entry = ttk.Entry(root, width=15)
entry.pack(pady=10)

#currency chosen combobox
n = tk.StringVar()
currencychosen = ttk.Combobox(root, width = 10, textvariable = n)

currencychosen['values'] = ('USD', 'EUR', 'GBP', 'JPY', 'MXN')  # Example currency options
currencychosen.pack(pady=10)

#2currrency chosen combobox
a = tk.StringVar()
currencychosen2 = ttk.Combobox(root, width = 10, textvariable = a)

currencychosen2['values'] = ('USD', 'EUR', 'GBP', 'JPY', 'MXN')  # Example currency options
currencychosen2.pack(pady=10)

#return converted value
label2 = tk.Label(root, text="", font=("Arial", 10), bg="white")
label2.pack(pady=10)

#placements
button.place(x=210, y=148)
label.place(x=20, y=20)
entry.place(x=20, y=80)
currencychosen.place(x=120, y=80)
currencychosen2.place(x=120, y=150)
label2.place(x=20, y=150)

#loop
root.mainloop()