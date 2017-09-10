'''
A program that stores the book information.
Title, author
year, ISBN

User can:
---------
View all records
Search an entry
Add entry
Update entry
Delete entry
Close
'''

from tkinter import *

window = Tk()

titleLabel = Label(window, text="Title")
titleLabel.grid(row=0, column=0)

authorLable = Label(window, text="Author")
authorLable.grid(row=0, column=2)

yearLabel = Label(window, text="Year")
yearLabel.grid(row=1, column=0)

isbnLabel = Label(window, text="ISBN")
isbnLabel.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# Create listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# create scrollbar
scrollBar1 = Scrollbar(window)
scrollBar1.grid(row=2, column=2, rowspan=6)

# Attach scrollbar with listbar
list1.configure(yscrollcommand=scrollBar1.set)
scrollBar1.configure(command=list1.yview)

# Create buttons
b1 = Button(window, text="View all", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)




window.mainloop()
