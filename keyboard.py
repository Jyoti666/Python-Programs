import tkinter as tk
#from tkinter import ttk
def down(event): print('down')
def up(event): print('up')
def dbtn(event):print('Double button')
def leave(event):print('Mouse left from widget')

def fin(event):print('Focus In')
def sup(event):print('Shift-Up')
def akey(event):print('a-key pressed')
def anykey(event):print('one of the key is pressed')

app = tk.Tk()
app.bind('<Button-1>', down)
app.bind('<ButtonRelease-1>', up)
app.bind('<Double-Button-1>', dbtn)
app.bind('<Leave>', leave)

app.bind('<FocusIn>', fin)
app.bind('<Shift-Up>', sup)
app.bind('<a>', akey)
app.bind('<Key>', anykey)

tk.mainloop()


