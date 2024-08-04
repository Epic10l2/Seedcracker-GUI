import customtkinter

nextIntCalls = 0
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
seedcracker = customtkinter.CTk()
seedcracker.title("Pillarseed Cracker")
seedcracker.geometry("900x900")

structure_entries = []

def add_structure_entry():
    if len(structure_entries) < 45:
        row = len(structure_entries) // 15
        col = len(structure_entries) % 15

        frame = customtkinter.CTkFrame(seedcracker)
        frame.place(x=50 + row * 238, y=95 + col * 30)

        combobox = customtkinter.CTkComboBox(frame, values=["Desert Pyramid", "Jungle Temple", "Igloo", "Swamp Hut", "Outpost", "Shipwreck"])
        combobox.grid(row=0, column=0)

        x_entry = customtkinter.CTkEntry(frame, width=50)
        x_entry.grid(row=0, column=1)

        z_entry = customtkinter.CTkEntry(frame, width=50)
        z_entry.grid(row=0, column=2)

        structure_entries.append((frame, combobox, x_entry, z_entry))

def remove_structure_entry():
    if structure_entries:
        frame, combobox, x_entry, z_entry = structure_entries.pop()
        frame.destroy()

def map_structure_name(name):
    return {
        "Desert Pyramid": "desert",
        "Jungle Temple": "jungle",
        "Igloo": "igloo",
        "Swamp Hut": "swamp",
        "Outpost": "outpost",
        "Shipwreck": "ship"
    }.get(name, "")

def generatelist():
    data = []

    if pillarseed_var.get():
        pillarseed = pillarseed_entry.get()
        data.append(f"{pillarseed}")
    else:
        data.append("-1")

    if gateway_var.get():
        gateway = gateway_entry.get()
        data.append(f"{gateway}")
    else:
        data.append("-1")

    for frame, combobox, x_entry, z_entry in structure_entries:
        structure = map_structure_name(combobox.get())
        x = x_entry.get()
        z = z_entry.get()
        data.append(f"{structure} {x} {z}")

    crack_structure_seed = crackstructureseed_var.get()
    print_to_file = printtofile_var.get()
    data.append(f"{crack_structure_seed}")
    data.append(f"{print_to_file}")

    with open("structure_data.txt", "w") as f:
        for item in data:
            f.write("%s\n" % item)

    print("Generated list: structure_data.txt")

add_button = customtkinter.CTkButton(seedcracker, text="Add Structure", command=add_structure_entry, width=50)
add_button.place(x=440, y=10)

remove_button = customtkinter.CTkButton(seedcracker, text="Remove Structure", command=remove_structure_entry, width=50)
remove_button.place(x=540, y=10)

pillarseed_var = customtkinter.BooleanVar()
pillarseed_checkbox = customtkinter.CTkCheckBox(seedcracker, text="Pillarseed: ", variable=pillarseed_var)
pillarseed_checkbox.place(x=50, y=10)

pillarseed_entry = customtkinter.CTkEntry(seedcracker, width=100)
pillarseed_entry.place(x=150, y=10)

gateway_var = customtkinter.BooleanVar()
gateway_checkbox = customtkinter.CTkCheckBox(seedcracker, text="First Gateway:", variable=gateway_var)
gateway_checkbox.place(x=50, y=40)

gateway_entry = customtkinter.CTkEntry(seedcracker, width=100)
gateway_entry.place(x=170, y=40)

crackstructureseed_var = customtkinter.BooleanVar()
crackstructureseed_checkbox = customtkinter.CTkCheckBox(seedcracker, text="Crack Structure Seed", variable=crackstructureseed_var)
crackstructureseed_checkbox.place(x=50, y=70)

printtofile_var = customtkinter.BooleanVar()
printtofile_checkbox = customtkinter.CTkCheckBox(seedcracker, text="Print to File", variable=printtofile_var)
printtofile_checkbox.place(x=200, y=70)

listgeneratebutton = customtkinter.CTkButton(seedcracker, text="Generate list for cracker", command=generatelist)
listgeneratebutton.place(x=665, y=10)

seedcracker.mainloop()
