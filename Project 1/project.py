import tkinter as tk
from tkinter import messagebox

class PointOfSale:
    def __init__(self, master):
        self.master = master
        self.master.title("Point of Sale")
        
        # Variabel untuk menyimpan data pelanggan dan transaksi
        self.customer_name = tk.StringVar()
        self.phone_number = tk.StringVar()
        self.bill_number = tk.StringVar()
        self.baju_qty = tk.IntVar()
        self.sepatu_qty = tk.IntVar()
        self.celana_qty = tk.IntVar()
        self.jaket_qty = tk.IntVar()
        self.topi_qty = tk.IntVar()

        # Inisialisasi total
        self.total_amount = tk.StringVar()
        self.total_amount.set("Total: Rp 0")

        # Membuat label dan entry untuk input data pelanggan
        tk.Label(master, text="Customer Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.customer_name).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(master, text="Phone Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.phone_number).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(master, text="Bill Number:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.bill_number).grid(row=2, column=1, padx=10, pady=10)

        # Membuat label dan entry untuk input jumlah barang
        tk.Label(master, text="Baju:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.baju_qty).grid(row=3, column=1, padx=10, pady=10)

        tk.Label(master, text="Sepatu:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.sepatu_qty).grid(row=4, column=1, padx=10, pady=10)

        tk.Label(master, text="Celana:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.celana_qty).grid(row=5, column=1, padx=10, pady=10)

        tk.Label(master, text="Jaket:").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.jaket_qty).grid(row=6, column=1, padx=10, pady=10)

        tk.Label(master, text="Topi:").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(master, textvariable=self.topi_qty).grid(row=7, column=1, padx=10, pady=10)

        # Button untuk menambahkan transaksi
        tk.Button(master, text="Add Transaction", command=self.add_transaction).grid(row=8, column=0, columnspan=2, pady=10)

        # Label untuk menampilkan total
        tk.Label(master, textvariable=self.total_amount, font=("Helvetica", 16)).grid(row=9, column=0, columnspan=2, pady=10)

        # Button untuk mencetak dan membersihkan
        tk.Button(master, text="Print Bill", command=self.print_bill).grid(row=10, column=0, pady=10)
        tk.Button(master, text="Clear", command=self.clear_entries).grid(row=10, column=1, pady=10)

    def add_transaction(self):
        try:
            # Mengambil nilai dari entry dan menghitung total
            baju_qty = self.baju_qty.get()
            sepatu_qty = self.sepatu_qty.get()
            celana_qty = self.celana_qty.get()
            jaket_qty = self.jaket_qty.get()
            topi_qty = self.topi_qty.get()

            total = (baju_qty * 50000) + (sepatu_qty * 100000) + (celana_qty * 75000) + (jaket_qty * 120000) + (topi_qty * 30000)

            # Menampilkan total di label
            self.total_amount.set(f"Total: Rp {total}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def print_bill(self):
        # Mendapatkan semua nilai dari entry
        customer_name = self.customer_name.get()
        phone_number = self.phone_number.get()
        bill_number = self.bill_number.get()
        baju_qty = self.baju_qty.get()
        sepatu_qty = self.sepatu_qty.get()
        celana_qty = self.celana_qty.get()
        jaket_qty = self.jaket_qty.get()
        topi_qty = self.topi_qty.get()
        total = self.total_amount.get()

        # Menampilkan detail transaksi di messagebox
        bill_details = f"Customer Name: {customer_name}\nPhone Number: {phone_number}\nBill Number: {bill_number}\n\n"
        bill_details += f"Baju: {baju_qty} x Rp 50,000\n"
        bill_details += f"Sepatu: {sepatu_qty} x Rp 100,000\n"
        bill_details += f"Celana: {celana_qty} x Rp 75,000\n"
        bill_details += f"Jaket: {jaket_qty} x Rp 120,000\n"
        bill_details += f"Topi: {topi_qty} x Rp 30,000\n\n"
        bill_details += f"{total}"

        messagebox.showinfo("Bill Details", bill_details)

    def clear_entries(self):
        # Menghapus semua nilai entry
        self.customer_name.set("")
        self.phone_number.set("")
        self.bill_number.set("")
        self.baju_qty.set(0)
        self.sepatu_qty.set(0)
        self.celana_qty.set(0)
        self.jaket_qty.set(0)
        self.topi_qty.set(0)
        self.total_amount.set("Total: Rp 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = PointOfSale(root)
    root.mainloop()
