import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from monster import *  # Import the classes from monster.py

class MonsterListGUI:
    def __init__(self, root, monster_list):
        self.root = root
        self.monster_list = monster_list
        self.root.title("Monster List Editor")

        # Add Tabs Here

        self.tab_control = ttk.Notebook(self.root)
        self.view_tab = ttk.Frame(self.tab_control)
        self.damage_type_tab = ttk.Frame(self.tab_control)
        self.family_tab = ttk.Frame(self.tab_control)
        self.ability_tab = ttk.Frame(self.tab_control)
        self.monster_tab = ttk.Frame(self.tab_control)
        
        # Display Tabs Here
        
        self.tab_control.add(self.view_tab, text="View")
        self.tab_control.add(self.damage_type_tab, text="Damage Types")
        self.tab_control.add(self.family_tab, text="Families")
        self.tab_control.add(self.ability_tab, text="Abilities")
        self.tab_control.add(self.monster_tab, text="Monsters")
        self.tab_control.pack(expand=1, fill="both")
        
        # Tab Specifics
        
            # View Tab
        
        self.view_monster_label = tk.Label(self.view_tab, text="Monsters:")
        self.view_family_label = tk.Label(self.view_tab, text="Families:")
        self.view_ability_label = tk.Label(self.view_tab, text="Abilities:")
        self.view_damage_label = tk.Label(self.view_tab, text="Damage Types:")
        
        self.view_monsters = tk.Listbox(self.view_tab, selectmode=tk.NONE)
        self.view_families = tk.Listbox(self.view_tab, selectmode=tk.NONE)
        self.view_abilities = tk.Listbox(self.view_tab, selectmode=tk.NONE)
        self.view_damages = tk.Listbox(self.view_tab, selectmode=tk.NONE)

        for monster in self.monster_list.monsters:
            self.view_monsters.insert(tk.END, monster.name)
        for family in self.monster_list.families:
            self.view_families.insert(tk.END, family.name)
        for ability in self.monster_list.abilities:
            self.view_abilities.insert(tk.END, ability.name)
        for damage in self.monster_list.damage_types:
            self.view_damages.insert(tk.END, damage.name)
            
        self.view_monster_label.pack()
        self.view_monsters.pack()
        self.view_family_label.pack()
        self.view_families.pack()
        self.view_ability_label.pack()
        self.view_abilities.pack()
        self.view_damage_label.pack()
        self.view_damages.pack()
        
            # Damage Type
        self.damage_type_name_label = tk.Label(self.damage_type_tab, text="Name:")
        self.damage_type_name_entry = tk.Entry(self.damage_type_tab)
        self.damage_type_description_label = tk.Label(self.damage_type_tab, text="Description:")
        self.damage_type_description_entry = tk.Entry(self.damage_type_tab)
        self.damage_type_add_button = tk.Button(self.damage_type_tab, text="Add Damage Type", command=self.add_damage_type)

        self.damage_type_name_label.pack()
        self.damage_type_name_entry.pack()
        self.damage_type_description_label.pack()
        self.damage_type_description_entry.pack()
        self.damage_type_add_button.pack()
        
            # Family 
        
        self.family_name_label = tk.Label(self.family_tab, text="Name:")
        self.family_name_entry = tk.Entry(self.family_tab)
        self.family_description_label = tk.Label(self.family_tab, text="Description:")
        self.family_description_entry = tk.Entry(self.family_tab)
        self.family_subfamily_label = tk.Label(self.family_tab, text="Subfamilies:")
        
        self.family_listbox = tk.Listbox(self.family_tab, selectmode=tk.MULTIPLE)

        for family in self.monster_list.families:
            self.family_listbox.insert(tk.END, family.name)
            
        self.family_create_button = tk.Button(self.family_tab, text="Add Family", command=self.add_family)

        self.family_name_label.pack()
        self.family_name_entry.pack()
        self.family_description_label.pack()
        self.family_description_entry.pack()

        # Position the Family listbox and its label
        self.family_subfamily_label.pack()
        self.family_listbox.pack()
        self.family_create_button.pack()

            # Ability
        
        self.ability_name_label = tk.Label(self.ability_tab, text="Ability Name:")
        self.ability_name_entry = tk.Entry(self.ability_tab)
        self.ability_description_label = tk.Label(self.ability_tab, text="Ability Description:")
        self.ability_description_entry = tk.Entry(self.ability_tab)
        self.ability_create_button = tk.Button(self.ability_tab, text="Add Ability", command=self.add_ability)
        
        self.ability_name_label.pack()
        self.ability_name_entry.pack()
        self.ability_description_label.pack()
        self.ability_description_entry.pack()
        self.ability_create_button.pack()
            # Monster
        

        self.monster_name_label = tk.Label(self.monster_tab, text="Name:")
        self.monster_name_entry = tk.Entry(self.monster_tab)
        self.monster_Str_label = tk.Label(self.monster_tab, text="Str:")
        self.monster_Str_entry = tk.Entry(self.monster_tab)
        self.monster_Dex_label = tk.Label(self.monster_tab, text="Dex:")
        self.monster_Dex_entry = tk.Entry(self.monster_tab)
        self.monster_Con_label = tk.Label(self.monster_tab, text="Con:")
        self.monster_Con_entry = tk.Entry(self.monster_tab)
        self.monster_Wis_label = tk.Label(self.monster_tab, text="Wis:")
        self.monster_Wis_entry = tk.Entry(self.monster_tab)
        self.monster_Int_label = tk.Label(self.monster_tab, text="Int:")
        self.monster_Int_entry = tk.Entry(self.monster_tab)
        self.monster_Cha_label = tk.Label(self.monster_tab, text="Cha:")
        self.monster_Cha_entry = tk.Entry(self.monster_tab)
        self.monster_description_label = tk.Label(self.monster_tab, text="Description:")
        self.monster_description_entry = tk.Entry(self.monster_tab)
        self.monster_parents_label = tk.Label(self.monster_tab, text="Parents:")
        self.monster_parents_listbox = tk.Listbox(self.monster_tab, selectmode=tk.MULTIPLE)
        self.monster_children_label = tk.Label(self.monster_tab, text="Children:")
        self.monster_children_listbox = tk.Listbox(self.monster_tab, selectmode=tk.MULTIPLE)
        self.monster_png_label = tk.Label(self.monster_tab, text="png:")
        self.monster_png_entry = tk.Entry(self.monster_tab)
        self.monster_vulnerabilities_label = tk.Label(self.monster_tab, text="Vulnerabilities:")
        self.monster_vulnerabilities_listbox = tk.Listbox(self.monster_tab, selectmode=tk.MULTIPLE)
        self.monster_resistances_label = tk.Label(self.monster_tab, text="Resistances:")
        self.monster_resistances_listbox = tk.Listbox(self.monster_tab, selectmode=tk.MULTIPLE)
        self.monster_immunities_label = tk.Label(self.monster_tab, text="Immunities:")
        self.monster_immunities_listbox = tk.Listbox(self.monster_tab, selectmode=tk.MULTIPLE)
        self.monster_families_label = tk.Label(self.monster_tab, text="Families:")
        self.monster_families_listbox = tk.Listbox(self.monster_tab, selectmode=tk.MULTIPLE)
        self.monster_rank_label = tk.Label(self.monster_tab, text="Rank:")
        self.monster_rank_entry = tk.Entry(self.monster_tab)
        self.monster_abilities_label = tk.Label(self.monster_tab, text="Abilities:")
        self.monster_abilities_listbox = tk.Listbox(self.monster_tab, selectmode=tk.MULTIPLE)
        self.monster_submit_button = tk.Button(self.monster_tab, text="Add Monster", command=self.add_monster)
        
        for family in self.monster_list.families:
            self.monster_families_listbox.insert(tk.END, family.name)
        for monster in self.monster_list.monsters:
            self.monster_parents_listbox.insert(tk.END, monster.name)
            self.monster_children_listbox.insert(tk.END, monster.name)
        for ability in self.monster_list.abilities:
            self.monster_abilities_listbox.insert(tk.END, ability.name)
        for damage_type in self.monster_list.damage_types:
            self.monster_resistances_listbox.insert(tk.END, damage_type.name)
            self.monster_vulnerabilities_listbox.insert(tk.END, damage_type.name)
            self.monster_immunities_listbox.insert(tk.END, damage_type.name)
            
        self.monster_parents_listbox.bind("<<ListboxSelect>>", self.select_parent)
        self.monster_children_listbox.bind("<<ListboxSelect>>", self.select_child)
        self.monster_families_listbox.bind("<<ListboxSelect>>", self.select_family)
        self.monster_vulnerabilities_listbox.bind("<<ListboxSelect>>", self.select_vuln)
        self.monster_resistances_listbox.bind("<<ListboxSelect>>", self.select_resist)
        self.monster_immunities_listbox.bind("<<ListboxSelect>>", self.select_immune)
        self.monster_abilities_listbox.bind("<<ListboxSelect>>", self.select_abilities)
        
        self.monster_name_label.grid(row=0, column=0)
        self.monster_name_entry.grid(row=1, column=0, padx="2px")
        self.monster_Str_label.grid(row=0, column=1)
        self.monster_Str_entry.grid(row=1, column=1, padx="2px")
        self.monster_Dex_label.grid(row=2, column=1)
        self.monster_Dex_entry.grid(row=3, column=1, padx="2px")
        self.monster_Con_label.grid(row=4, column=1)
        self.monster_Con_entry.grid(row=5, column=1, padx="2px")
        self.monster_Wis_label.grid(row=0, column=2)
        self.monster_Wis_entry.grid(row=1, column=2, padx="2px")
        self.monster_Int_label.grid(row=2, column=2)
        self.monster_Int_entry.grid(row=3, column=2, padx="2px")
        self.monster_Cha_label.grid(row=4, column=2)
        self.monster_Cha_entry.grid(row=5, column=2, padx="2px")
        self.monster_description_label.grid(row=2, column=0)
        self.monster_description_entry.grid(row=3, column=0, padx="2px")
        self.monster_parents_label.grid(row=0, column=3)
        self.monster_parents_listbox.grid(row=1, column=3, padx="2px")
        self.monster_children_label.grid(row=2, column=3)
        self.monster_children_listbox.grid(row=3, column=3, padx="2px")
        self.monster_png_label.grid(row=4, column=0)
        self.monster_png_entry.grid(row=5, column=0, padx="2px")
        self.monster_vulnerabilities_label.grid(row=0, column=4)
        self.monster_vulnerabilities_listbox.grid(row=1, column=4, padx="2px")
        self.monster_resistances_label.grid(row=2, column=4)
        self.monster_resistances_listbox.grid(row=3, column=4, padx="2px")
        self.monster_immunities_label.grid(row=4, column=4)
        self.monster_immunities_listbox.grid(row=5, column=4, padx="2px")
        self.monster_families_label.grid(row=0, column=5)
        self.monster_families_listbox.grid(row=1, column=5, padx="2px")
        self.monster_rank_label.grid(row=6, column=0)
        self.monster_rank_entry.grid(row=7, column=0, padx="2px")
        self.monster_abilities_label.grid(row=2, column=5)
        self.monster_abilities_listbox.grid(row=3, column=5, padx="2px")

        self.monster_submit_button.grid(row=8, column=5, padx="2px")

        self.save_button = tk.Button(self.root, text="Save", command=self.save_monster_list)
        self.save_button.pack(side="bottom")

    def add_damage_type(self):
        name = self.damage_type_name_entry.get()
        description = self.damage_type_description_entry.get()
        
        if not name:
            messagebox.showerror("Error", "Please provide a name for the Damage Type.")
            return
        
        # Check if a DamageType with the same name already exists
        for existing_damage_type in self.monster_list.damage_types:
            if existing_damage_type.name == name:
                messagebox.showerror("Error", "A Damage Type with the same name already exists.")
                return
        
        damage_type = DamageType(name, description)
        self.monster_list.damage_types.append(damage_type)
        messagebox.showinfo("Success", "Damage Type added successfully.")
        self.damage_type_name_entry.delete(0, 'end')
        self.damage_type_description_entry.delete(0, 'end')

    def add_family(self):
        name = self.family_name_entry.get()
        description = self.family_description_entry.get()
        selected_items = self.family_listbox.curselection()  # Get selected items from the Listbox

        if not name:
            messagebox.showerror("Error", "Please provide a name for the Family.")
            return
        
        # Check if a Family with the same name already exists
        for existing_family in self.monster_list.families:
            if existing_family.name == name:
                messagebox.showerror("Error", "A Family with the same name already exists.")
                return

        family = Family(name, description)  # Create a Family object
        family.subfamilies = [self.family_listbox.get(index) for index in selected_items]  # Add selected items to "subfamilies"
        self.monster_list.families.append(family)  # Add the Family object to the list
        self.family_listbox.insert(tk.END, name)  # Update the Listbox
        messagebox.showinfo("Success", "Family added successfully.")
        self.family_name_entry.delete(0, 'end')
        self.family_description_entry.delete(0, 'end')

    def add_ability(self):
        name = self.ability_name_entry.get()
        description = self.ability_description_entry.get()
        
        if not name:
            messagebox.showerror("Error", "Please provide a name for the Ability.")
            return
        
        # Check if an Ability with the same name already exists
        for existing_ability in self.monster_list.abilities:
            if existing_ability.name == name:
                messagebox.showerror("Error", "An Ability with the same name already exists.")
                return
        
        ability = Ability(name, description)
        self.monster_list.abilities.append(ability)
        self.view_abilities.insert(tk.END, name)
        messagebox.showinfo("Success", "Ability Added successfully!")
        self.ability_name_entry.delete(0, 'end')
        self.ability_description_entry.delete(0, 'end')

    def add_monster(self):
        def hash_monster():
            if len(monster_list.monsters) > 0:
                Id = f"{int(monster_list.monsters[-1].id) + 1}"
            else:
                Id = "0"
            return Id
        
        name = self.monster_name_entry.get()
        for existing_monster in self.monster_list.monsters:
            if name == existing_monster.name:
                messagebox.showerror("Error", "A Monster with the same name already exists.")
                return
        Str = self.monster_Str_entry.get()
        Dex = self.monster_Dex_entry.get()
        Con = self.monster_Con_entry.get()
        Wis = self.monster_Wis_entry.get()
        Int = self.monster_Int_entry.get()
        Cha = self.monster_Cha_entry.get()
        description = self.monster_description_entry.get()
        png = self.monster_png_entry.get()
        rank = self.monster_rank_entry.get()
        Id = hash_monster()

        new_monster = Monster(name, Str, Dex, Con, Wis, Int, Cha, description, self.parents, self.children, png, self.vulns, self.resists, self.immunes, self.families, rank, self.abilities, Id)
        self.monster_list.monsters.append(new_monster)
        self.view_monsters.insert(tk.END, name) 

    def select_parent(self, event):
        parent_items = self.monster_parents_listbox.curselection()
        self.parents = [self.monster_parents_listbox.get(index) for index in parent_items]
    def select_child(self, event):
        children_items = self.monster_children_listbox.curselection()
        self.children = [self.monster_children_listbox.get(index) for index in children_items]
    def select_family(self, event):
        families_items = self.monster_families_listbox.curselection()
        self.families = [self.monster_families_listbox.get(index) for index in families_items]
    def select_vuln(self, event):
        vulns_items = self.monster_vulnerabilities_listbox.curselection()
        self.vulns = [self.monster_vulnerabilities_listbox.get(index) for index in vulns_items]
    def select_resist(self, event):
        resists_items = self.monster_resistances_listbox.curselection()
        self.resists = [self.monster_resistances_listbox.get(index) for index in resists_items]
    def select_immune(self, event):
        immunes_items = self.monster_immunities_listbox.curselection()
        self.immunes = [self.monster_immunities_listbox.get(index) for index in immunes_items]
    def select_abilities(self, event):
        ability_items = self.monster_abilities_listbox.curselection()
        self.abilities = [self.monster_abilities_listbox.get(index) for index in ability_items]
    

    def save_monster_list(self):
        monster_list.save_data()

# Create a MonsterList instance
monster_list = MonsterList()
monster_list.load_data()

# Create the Tkinter main window
root = tk.Tk()

# Create the MonsterListGUI instance and pass the MonsterList
monster_list_gui = MonsterListGUI(root, monster_list)

# Start the Tkinter main loop
root.mainloop()
