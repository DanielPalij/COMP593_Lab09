from tkinter import *
from tkinter import ttk

# Create the window
root = Tk()
root.title("Poke Info Viewer")
# TODO: Additional window configuration
# TODO: Add widgets to window
# Loop until window is closed


frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1)

lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=(20,5), pady=(10,30))

btn_hello = ttk.Button(frm_top, text='Get Info')
btn_hello.grid(row=0, column=2, )

lbl_hello = ttk.Label(frm_btm_right)
lbl_hello.grid(padx=10, pady=10)


root.mainloop()