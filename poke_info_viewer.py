from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info

# Create the window
root = Tk()
root.title('Pokemon Info Viewer')
root.resizable(False, False)
root.configure(bg='#856ff8')


# Add frames to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20,10))

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0,padx=20, pady=20, sticky=N,)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=20, pady=20)

# Add widgets to frames
# Populate widget in the top frame 
lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0, padx=10, pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle_get_info():
    # Get pokemon name entered by user
    pname = ent_name.get().strip()
    if len(pname) == 0:
        return
    
    # Get pokemon info from pokeAPI
    pinfo = get_pokemon_info(pname)
    if pinfo is None:
        err_msg = f'Unable to fetch information for {pname} from PokeAPI.'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
        return
    
    # Populate info values
    lbl_height_val['text'] = f"{pinfo['height']} dm"
    lbl_weight_val['text'] = f"{pinfo['weight']} kg"
    
    # Different types
    diff_types = [df['type']['name'].title() for df in pinfo['types']]
    if len(diff_types) == 1:
        lbl_type_val['text'] = f'{diff_types[0]}'

    else:
        lbl_type_val['text'] = ' , '.join(diff_types)




    hp_bar['value'] = pinfo['stats'][0]['base_stat']
    attack_bar['value'] = pinfo['stats'][1]['base_stat']
    defense_bar['value'] = pinfo['stats'][2]['base_stat']
    spec_a_bar['value'] = pinfo['stats'][3]['base_stat']
    spec_d_bar['value'] = pinfo['stats'][4]['base_stat']
    speed_bar['value'] = pinfo['stats'][5]['base_stat']
    
    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)

# Populate widgets in info frame
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx=10, pady=10, sticky=E)

lbl_height_val = ttk.Label(frm_btm_left, text='TBD:')
lbl_height_val.grid(row=0, column=1, padx=10, pady=10, sticky=W)

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx=10, pady=10, sticky=E)

lbl_weight_val = ttk.Label(frm_btm_left, text='TBD:')
lbl_weight_val.grid(row=1, column=1, padx=10, pady=10, sticky=W)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx=10, pady=10, sticky=E)

lbl_type_val = ttk.Label(frm_btm_left, text='TBD:')
lbl_type_val.grid(row=2, column=1, padx=10, pady=10, sticky=W)

# Populate stats frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx=10, pady=10, sticky=E)
hp_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200)
hp_bar.grid(row=0, column=1)

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, padx=10, pady=10, sticky=E)
attack_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200)
attack_bar.grid(row=1, column=1)

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0, padx=10, pady=10, sticky=E)
defense_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200)
defense_bar.grid(row=2, column=1)

lbl_spec_a = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_spec_a.grid(row=3, column=0, padx=10, pady=10, sticky=E)
spec_a_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200)
spec_a_bar.grid(row=3, column=1)

lbl_spec_d = ttk.Label(frm_btm_right, text='Special Defense:')
lbl_spec_d.grid(row=4, column=0, padx=10, pady=10, sticky=E)
spec_d_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200)
spec_d_bar.grid(row=4, column=1)

lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, padx=10, pady=10, sticky=E)
speed_bar = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200)
speed_bar.grid(row=5, column=1)







# Loop until window is closed
root.mainloop()