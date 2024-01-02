from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Point Of Sale')
root.geometry('1280x720')
bg_color = '#202020'

# =================Variable=================
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
Rate = DoubleVar()
Quantity = IntVar()
bill_no = StringVar()
x = random.randint(1000, 9999)
bill_no.set(str(x))

# Globals
product_list = []  

# =================Function=================
def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t Welcome Mart Retails")
    textarea.insert(END, f'\n\n\nBill Number :\t\t{bill_no.get()}')
    textarea.insert(END, f'\n Customer Name :\t\t{cname_txt.get()}')  
    textarea.insert(END, f'\n Phone Number :\t\t{cphone_txt.get()}')  
    textarea.insert(END, f"\n======================================")
    textarea.insert(END, f'\n Product\t\t QTY\t\tPrice')
    textarea.insert(END, f"\n======================================")
    textarea.configure(font='arial 15 bold')

def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0.0)
    Quantity.set(0)
    textarea.delete(1.0, END)

def additm():
    n = Rate.get()
    m = Quantity.get() * n
    if item.get() == '' or n <= 0 or Quantity.get() <= 0:
        messagebox.showerror('Error', 'Please enter valid product details')
    else:
        product = {
            'name': item.get(),
            'quantity': Quantity.get(),
            'rate': n,
            'total': m
        }
        product_list.append(product)
        textarea.insert(END, f"{item.get()}\t\t{Quantity.get()}\t\t{m}\n")
        item.set('')
        Rate.set(0.0)
        Quantity.set(0)

def gbill():
    welcome()
    total_amount = 0.0
    for product in product_list:
        textarea.insert(END, f"{product['name']}\t\t{product['quantity']}\t\t{product['total']}\n")
        total_amount += product['total']

    textarea.insert(END, f"\n======================================")
    textarea.insert(END, f"Total Paybill Amount :\t\t\t{total_amount}")
    textarea.insert(END, f"\n======================================")

# =================Top section=================
title = Label(root, text='Point Of Sale', bg=bg_color, fg='white', font=('times new roman', 25, 'bold'),
              relief=GROOVE, bd=12)
title.pack(fill=X)

# =================Customer details===========
F1 = LabelFrame(root, text='Customer Details', font=('times new roman', 18, 'bold'), relief=GROOVE, bd=10, bg=bg_color,
                fg='gold')
F1.place(x=0, y=80, relwidth=1)

cname_lbl = Label(F1, text='Customer Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cname_lbl.grid(row=0, column=0, padx=10, pady=5)

cname_txt = Entry(F1, width=15, font='arial 15 bold', relief=SUNKEN, textvariable=c_name)
cname_txt.grid(row=0, column=1, padx=10, pady=5)

cphone_lbl = Label(F1, text='Phone', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cphone_lbl.grid(row=0, column=2, padx=10, pady=5)

cphone_txt = Entry(F1, width=15, font='arial 15 bold', relief=SUNKEN, textvariable=c_phone)
cphone_txt.grid(row=0, column=3, padx=10, pady=5)

# =================Product Detail=============
F2 = LabelFrame(root, text='Product Detail', font=('times new roman', 18, 'bold'), relief=GROOVE, bd=10, bg=bg_color,
                fg='gold')
F2.place(x=20, y=180, width=638, height=500)

itm = Label(F2, text='Product Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='lightgreen')
itm.grid(row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20, font='arial 15 bold', textvariable=item)
itm_txt.grid(row=0, column=1, padx=30, pady=20)

rate = Label(F2, text='Product Price', font=('times new roman', 18, 'bold'), bg=bg_color, fg='lightgreen')
rate.grid(row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=20, font='arial 15 bold', textvariable=Rate)
rate_txt.grid(row=1, column=1, padx=30, pady=20)

quantity = Label(F2, text='Product Quantity', font=('times new roman', 18, 'bold'), bg=bg_color, fg='lightgreen')
quantity.grid(row=2, column=0, padx=30, pady=20)
quantity_txt = Entry(F2, width=20, font='arial 15 bold', textvariable=Quantity)
quantity_txt.grid(row=2, column=1, padx=30, pady=20)

# =================Button=========
btn1 = Button(F2, text='Add item', font='arial 15 bold', padx=5, pady=10, bg='white', width=15, command=additm)
btn1.grid(row=3, column=0, padx=10, pady=30)

btn2 = Button(F2, text='Generate Bill', font='arial 15 bold', padx=5, pady=10, bg='white', width=15, command=gbill)
btn2.grid(row=3, column=1, padx=10, pady=30)

btn3 = Button(F2, text='Clear', font='arial 15 bold', padx=5, pady=10, bg='white', width=15, command=clear)
btn3.grid(row=4, column=0, padx=10, pady=30)

btn4 = Button(F2, text='Exit', font='arial 15 bold', padx=5, pady=10, bg='white', width=15)
btn4.grid(row=4, column=1, padx=30)

# ====================Bill Area===============
F3 = Frame(root, relief=GROOVE, bd=10)
F3.place(x=700, y=180, width=500, height=500)

bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7).pack(fill=X)
SCROLL_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, yscrollcommand=SCROLL_y)
SCROLL_y.pack(side=RIGHT, fill=Y)
SCROLL_y.config(command=textarea.yview)
textarea.pack()
welcome()

root.mainloop()
