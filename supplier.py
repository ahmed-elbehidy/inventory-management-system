from tkinter import *
from tkinter import ttk

from tomlkit import value


def supplier_form(window):
    global back_image
    supplier_frame = Frame(window, width=1070, height=567, bg='white')
    supplier_frame.place(x=200, y=100)

    heading_label = Label(
        supplier_frame,
        text='Manage Supplier Details',
        font=('times new roman', 16, 'bold'),
        bg='#0f4d7d',
        fg='white'
    )
    heading_label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='assets/icons/back_button.png')
    back_button = Button(
        supplier_frame,
        image=back_image,
        bd=0,
        cursor='hand2',
        bg='white',
        command=lambda: supplier_frame.place_forget()
    )
    back_button.place(x=10, y=30)

    # Left Frame
    left_frame = Frame(supplier_frame, bg='white')
    left_frame.place(x=10,y=100)

    invoice_label = Label(left_frame, text='Invoice No.', font=('times new roman',14,'bold'), bg='white')
    invoice_label.grid(row=0,column=0,padx=(20,40), sticky='w')
    invoice_entry = Entry(left_frame, font=('times new roman',14,'bold'), bg='lightyellow')
    invoice_entry.grid(row=0,column=1)

    name_label = Label(left_frame, text='Supplier Name', font=('times new roman', 14, 'bold'), bg='white')
    name_label.grid(row=1, column=0, padx=(20,40), pady=25, sticky='w')
    name_entry = Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    name_entry.grid(row=1, column=1)

    contact_label = Label(left_frame, text='Supplier Contact', font=('times new roman', 14, 'bold'), bg='white')
    contact_label.grid(row=2, column=0, padx=(20,40), sticky='w')
    contact_entry = Entry(left_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    contact_entry.grid(row=2, column=1)

    description_label = Label(left_frame, text='Description', font=('times new roman', 14, 'bold'), bg='white')
    description_label.grid(row=3, column=0, padx=(20,40), sticky='nw', pady=25)
    description_text  = Text(left_frame, width=25, height=6, bd=2, bg='lightyellow')
    description_text.grid(row=3,column=1,pady=25)

    button_frame = Frame(left_frame, bg='white')
    button_frame.grid(row=4, columnspan=2, pady=20)
    add_button = Button(
        button_frame,
        text='Add',
        font=('times new roman', 14),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d'
    )
    add_button.grid(row=0, column=0, padx=20)

    update_button = Button(
        button_frame,
        text='Update',
        font=('times new roman', 14),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d'
    )
    update_button.grid(row=0, column=1)

    delete_button = Button(
        button_frame,
        text='Delete',
        font=('times new roman', 14),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d'
    )
    delete_button.grid(row=0, column=2, padx=20)

    clear_button = Button(
        button_frame,
        text='Clear',
        font=('times new roman', 14),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d'
    )
    clear_button.grid(row=0, column=3)

    # Right frame
    right_frame = Frame(supplier_frame, bg='white')
    right_frame.place(x=520,y=95,width=500,height=350)

    search_frame = Frame(right_frame, bg='white')
    search_frame.pack(pady=(0,20))
    num_label = Label(search_frame, text='Invoice No.', font=('times new roman', 14, 'bold'), bg='white')
    num_label.grid(row=0, column=0, padx=(0,15), sticky='w')
    search_entry = Entry(search_frame, font=('times new roman', 14, 'bold'), bg='lightyellow', width=12)
    search_entry.grid(row=0, column=1)

    search_button = Button(
        search_frame,
        text='Search',
        font=('times new roman', 14),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d'
    )
    search_button.grid(row=0, column=2, padx=15)

    show_button = Button(
        search_frame,
        text='Show All',
        font=('times new roman', 14),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d'
    )
    show_button.grid(row=0, column=3)

    scrolly = Scrollbar(right_frame, orient=VERTICAL)
    scrollx = Scrollbar(right_frame, orient=HORIZONTAL)
    treeview = ttk.Treeview(
        right_frame,
        column=('invoice','name','contact','description'),
        show='headings',
        yscrollcommand=scrolly.set,
        xscrollcommand=scrollx.set
    )
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.pack(side=BOTTOM,fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH,expand=1)
    treeview.heading('invoice',text='Invoice Id')
    treeview.heading('name',text='Supplier Name')
    treeview.heading('contact',text='Supplier Contact')
    treeview.heading('description',text='Description')

    treeview.column('invoice',width=80)
    treeview.column('name',width=160)
    treeview.column('contact',width=120)
    treeview.column('description',width=300)