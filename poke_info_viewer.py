from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon
# Create the window
root = Tk()
root.title("Poke Info Viewer")
# TODO: Additional window configuration
# TODO: Add widgets to window
# Loop until window is closed


frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0,padx=(20,10), pady=(10,20))

# populate info frame
lbl_height = ttk.Label(frm_top, text='Height:')
lbl_height.grid(row=0, column=0)

lbl_height_value = ttk.Label(frm_top, text='Height:')
lbl_height_value.grid(row=1, column=1)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1)

hp_bar = ttk.Label(frm_btm_right, text='HP:')
hp_bar.grid(row=0, column=1)
hp_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length = 200)
hp_bar.grid(row=0, column=2)

# TODO: Add weight and height

# populate weight in stats
lbl_hp = ttk.Label(frm_top, text='Height:')
lbl_hp.grid(row=0, column=1)




lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1,padx=(20,10), pady=(10,20))

def handle_get_info():
    # get the pokemon name entered by the user
    pname = ent_name.get()

    
    
    return

btn_hello = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_hello.grid(row=0, column=2,padx=(10,20), pady=(10,20))

lbl_hello = ttk.Label(frm_btm_right)
lbl_hello.grid(padx=10, pady=10)


root.mainloop()