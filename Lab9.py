from tkinter import *
from tkinter import ttk
from PokeAPI import get_pokemon_info
from tkinter import messagebox

# Create the window
root = Tk()
root.title("Pokemon Stat Tracker")
root.resizable(False, False)

frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=10, pady=10, sticky=N)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=10, pady=10)

lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=1)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0, padx=10, pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10, pady=10)

def handle_get_info():
    #Get entered pokemon name
    poke_name = ent_name.get().strip()
    if len(poke_name) ==0:
           return


    #Get the info from the API
    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
          err_message = f'Unable to fetch information for {poke_name.capitalize()} from the PokeAPI'
          messagebox.showinfo(title='Error', message=err_message, icon='error')
          return
    #Populate the info frame
    lbl_height_value['text'] = f"{poke_info['height']} dm"
    lbl_weight_value['text'] = f"{poke_info['weight']} lb"
    get_type = [m['type']['name'] for m in poke_info['types']]
    
    lbl_type_value['text'] = ', '.join(get_type)

    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_atk['value'] = poke_info['stats'][1]['base_stat']
    bar_def['value'] = poke_info['stats'][2]['base_stat']
    bar_spatk['value'] = poke_info['stats'][3]['base_stat']
    bar_spdef['value'] = poke_info['stats'][4]['base_stat']
    bar_spe['value'] = poke_info['stats'][5]['base_stat']
    
    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)
btn_get_info = ttk.Label(frm_top)
btn_get_info.grid(padx=10, pady=10)

#Populate info frame
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0,padx=0, pady=0, sticky=E)
lbl_height_value = ttk.Label(frm_btm_left, text='  dm')
lbl_height_value.grid(row=0, column=1, padx=3, pady=0, sticky=W)

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0,padx=0, pady=0, sticky=E)
lbl_weight_value = ttk.Label(frm_btm_left, text='  lb')
lbl_weight_value.grid(row=1, column=1, padx=3, pady=0, sticky=W)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0,padx=0, pady=0, sticky=E)
lbl_type_value = ttk.Label(frm_btm_left, text=' ')
lbl_type_value.grid(row=2, column=1, padx=3, pady=0, sticky=W)

#Populate stats frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0,padx=0, pady=0, sticky=E)
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1,padx=0, pady=0)

lbl_atk = ttk.Label(frm_btm_right, text='Attack:')
lbl_atk.grid(row=1, column=0,padx=0, pady=0, sticky=E)
bar_atk = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_atk.grid(row=1, column=1,padx=0, pady=0)

lbl_def = ttk.Label(frm_btm_right, text='Defence:')
lbl_def.grid(row=2, column=0,padx=0, pady=0, sticky=E)
bar_def = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_def.grid(row=2, column=1,padx=0, pady=0)

lbl_spatk = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_spatk.grid(row=3, column=0,padx=0, pady=0, sticky=E)
bar_spatk = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spatk.grid(row=3, column=1,padx=0, pady=0)

lbl_spdef = ttk.Label(frm_btm_right, text='Special Defence:')
lbl_spdef.grid(row=4, column=0,padx=0, pady=0)
bar_spdef = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spdef.grid(row=4, column=1,padx=0, pady=0)

lbl_spe = ttk.Label(frm_btm_right, text='Speed:')
lbl_spe.grid(row=5, column=0,padx=0, pady=0, sticky=E)
bar_spe = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_spe.grid(row=5, column=1,padx=0, pady=0)


# Loop until window is closed
root.mainloop()