import tkinter as tk
from tkinter import messagebox


class PointOfSaleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Point of Sale App")

        self.customer_name_label = tk.Label(master, text="Customer Name:")
        self.customer_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.customer_name_entry = tk.Entry(master)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.product_label = tk.Label(master, text="Product:")
        self.product_label.grid(row=1, column=0, padx=10, pady=10)

        self.product_entry = tk.Entry(master)
        self.product_entry.grid(row=1, column=1, padx=10, pady=10)

        self.price_label = tk.Label(master, text="Price:")
        self.price_label.grid(row=2, column=0, padx=10, pady=10)

        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=3, column=0, padx=10, pady=10)

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=4, column=0, padx=10, pady=10)

        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.print_button = tk.Button(master, text="Print Bill", command=self.print_bill)
        self.print_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_cart)
        self.clear_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.cart_label = tk.Label(master, text="Cart:")
        self.cart_label.grid(row=8, column=0, columnspan=2, pady=10)

        self.cart_text = tk.Text(master, height=10, width=40)
        self.cart_text.grid(row=9, column=0, columnspan=2, pady=10)

        self.total_label = tk.Label(master, text="Total:")
        self.total_label.grid(row=10, column=0, padx=10, pady=10)

        self.total_amount_label = tk.Label(master, text="")
        self.total_amount_label.grid(row=10, column=1, padx=10, pady=10)

        self.total_amount = 0
        self.cart_items = []

    def add_to_cart(self):
        try:
            product = self.product_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for price and quantity.")
            return

        total_price = price * quantity
        self.cart_items.append(f"{product} - {quantity} x {price} = {total_price}")

        self.cart_text.config(state=tk.NORMAL)
        self.cart_text.delete(1.0, tk.END)
        for item in self.cart_items:
            self.cart_text.insert(tk.END, item + "\n")
        self.cart_text.config(state=tk.DISABLED)

        self.total_amount += total_price
        self.total_amount_label.config(text=f"Total: {self.total_amount:.2f}")

        # Clear entry fields
        self.product_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def print_bill(self):
        customer_name = self.customer_name_entry.get()
        if not customer_name:
            messagebox.showwarning("Warning", "Please enter the customer's name before printing the bill.")
            return

        phone_number = self.phone_entry.get()
        if not phone_number:
            messagebox.showwarning("Warning", "Please enter a phone number before printing the bill.")
            return

        bill_message = f"Customer Name: {customer_name}\nPhone: {phone_number}\n\nItems in Cart:\n"
        for item in self.cart_items:
            bill_message += f"{item}\n"
        bill_message += f"\nTotal Amount: {self.total_amount:.2f}"

        messagebox.showinfo("Bill", bill_message)

    def clear_cart(self):
        self.cart_items = []
        self.cart_text.config(state=tk.NORMAL)
        self.cart_text.delete(1.0, tk.END)
        self.cart_text.config(state=tk.DISABLED)

        self.total_amount = 0
        self.total_amount_label.config(text="Total: 0.00")

if __name__ == "__main__":
    root = tk.Tk()
    app = PointOfSaleApp(root)
    root.mainloop()
