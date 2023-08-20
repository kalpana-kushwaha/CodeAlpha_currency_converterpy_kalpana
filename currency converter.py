import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates


class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Currency Converter")
        root.geometry("400x400")
        root.resizable(False, False)
        root.configure(background="azure3")

        currency_rates = CurrencyRates()

        from_currency_var = tk.StringVar()
        to_currency_var = tk.StringVar()
        amount_var = tk.StringVar()
        result_var = tk.StringVar()

        self.setup_ui(root, currency_rates, from_currency_var, to_currency_var, amount_var, result_var)

    def setup_ui(self, root, currency_rates, from_currency_var, to_currency_var, amount_var, result_var):
        font = ("Helvetica", 15)

        from_label = tk.Label(root, text="From Currency:", font=font)
        from_label.pack()

        from_currency_combobox = ttk.Combobox(root, textvariable=from_currency_var, font=font)
        from_currency_combobox.pack()

        to_label = tk.Label(root, text="To Currency:", font=font)
        to_label.pack()

        to_currency_combobox = ttk.Combobox(root, textvariable=to_currency_var, font=font)
        to_currency_combobox.pack()

        amount_label = tk.Label(root, text="Amount:", font=font)
        amount_label.pack()

        amount_entry = tk.Entry(root, textvariable=amount_var, font=font)
        amount_entry.pack()

        def convert_currency():
            from_currency = from_currency_var.get()
            to_currency = to_currency_var.get()
            amount = float(amount_var.get())

            conversion_result = currency_rates.convert(from_currency, to_currency, amount)
            conversion_rate = currency_rates.get_rate(from_currency, to_currency)

            result_var.set(
                f"{amount:.2f} {from_currency} = {conversion_result:.2f} {to_currency}\nConversion Rate: 1 {from_currency} = {conversion_rate:.4f} {to_currency}")

        convert_button = tk.Button(root, text="Convert", command=convert_currency, font=font)
        convert_button.pack()

        result_label = tk.Label(root, text="Result:", font=font)
        result_label.pack()

        result_display = tk.Label(root, textvariable=result_var, font=font)
        result_display.pack()

        # Autocomplete for comboboxes
        self.populate_currency_combobox(from_currency_combobox, currency_rates)
        self.populate_currency_combobox(to_currency_combobox, currency_rates)

    def populate_currency_combobox(self, combobox, currency_rates):
        currencies = list(currency_rates.get_rates('').keys())
        combobox['values'] = currencies
        combobox.set("Select Currency")


def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

