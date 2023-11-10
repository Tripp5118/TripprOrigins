import json
from json import JSONEncoder

class DamageType:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Family:
    def __init__(self, name, description, subfamilies=None):
        self.name = name
        self.description = description
        self.subfamilies = subfamilies if subfamilies is not None else []

class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
class JsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Monster:
    def __init__(self, name, str, dex, con, wis, int, cha, description, parents, children, png="", vulnerabilities=None, resistances=None, immunities=None, families=None, rank="", abilities=None, id=""):
        self.name = name
        self.id = id
        self.str = str
        self.dex = dex
        self.con = con
        self.wis = wis
        self.int = int
        self.cha = cha
        self.description = description
        self.parents = parents if parents is not None else [] # list of monsters
        self.children = children if children is not None else [] # list of monsters
        self.png = png
        self.vulnerabilities = vulnerabilities if vulnerabilities is not None else []
        self.resistances = resistances if resistances is not None else []
        self.immunities = immunities if immunities is not None else []
        self.families = families if families is not None else []
        self.rank = rank
        self.abilities = abilities if abilities is not None else []

class MonsterList:
    def __init__(self):
        """
        Initializes an empty MonsterList with lists for vulnerabilities, resistances, immunities, families, monsters, and abilities.
        """
        self.damage_types = [] # List of DamageType objects
        self.families = []  # List of Family objects
        self.monsters = []  # List of Monster objects
        self.abilities = [] # List of Ability objects

    def load_data(self):
        """
        Loads data from JSON files into the MonsterList object. Loads vulnerabilities, resistances, immunities,
        families, and monsters. If the data files are not found, initializes with empty data.
        """
        try:
            with open('damageTypes.json', 'r') as file:
                damage_types_data = json.load(file)
            with open('families.json', 'r') as file:
                families_data = json.load(file)
            with open('monsterList.json', 'r') as file:
                monsters_data = json.load(file)
            with open('abilities.json', 'r') as file:
                abilities_data = json.load(file)

            # Instantiate the lists using the loaded data
            self.damage_types = [DamageType(item['name'], item['description']) for item in damage_types_data]
            self.families = [Family(item['name'], item['description'], item['subfamilies']) for item in families_data]
            self.monsters = [Monster(item['name'], item['str'], item['dex'], item['con'], item['wis'], item['int'], item['cha'], item['description'], item['parents'], item['children'], item['png'], item['vulnerabilities'], item['resistances'], item['immunities'], item['families'], item['rank'], item['abilities'], item['id']) for item in monsters_data]
            self.abilities = [Ability(item['name'], item['description']) for item in abilities_data]

        except FileNotFoundError:
            print("One or more data files not found. Initializing with empty data.")
            # Initialize empty lists
            self.damage_types = []
            self.families = []
            self.monsters = []
            self.abilities = []

    def save_data(self):
        """
        Saves the data from the MonsterList object into JSON files. Saves vulnerabilities, resistances, immunities,
        families, and monsters.
        """
        with open('damageTypes.json', 'w') as file:
            json.dump(self.damage_types, file, indent=4, cls=JsonEncoder)
        with open('families.json', 'w') as file:
            json.dump(self.families, file, indent=4, cls=JsonEncoder)
        with open('monsterList.json', 'w') as file:
            json.dump(self.monsters, file, indent=4, cls=JsonEncoder)
        with open('abilities.json', 'w') as file:
            json.dump(self.abilities, file, indent=4, cls=JsonEncoder)

    # ==== Monster Operations ====

    def add_monster(self, monster):
        """
        Adds a new monster to the MonsterList.

        Args:
            monster (Monster): The Monster object to be added.
        """
        for existing_monster in self.monsters:
            if existing_monster.id == monster.id:
                print("A monster with the same ID already exists.")
                return

        self.monsters.append(monster)
        print(f"Added {monster.name} to the MonsterList.")

    def update_monster(self, monster_id, new_attributes):
        """
        Updates a monster's attributes based on its ID.

        Args:
            monster_id (int): The ID of the monster to be updated.
            new_attributes (dict): A dictionary containing the new attributes to be updated.
        """
        for monster in self.monsters:
            if monster.id == monster_id:
                for key, value in new_attributes.items():
                    if hasattr(monster, key):
                        setattr(monster, key, value)
                print(f"Updated attributes for monster with ID {monster_id}.")
                return
        print(f"Monster with ID {monster_id} not found.")

    def delete_monster(self, monster_id):
        """
        Deletes a monster based on its ID.

        Args:
            monster_id (int): The ID of the monster to be deleted.
        """
        for monster in self.monsters:
            if monster.id == monster_id:
                self.monsters.remove(monster)
                print(f"Deleted monster with ID {monster_id}.")
                return
        print(f"Monster with ID {monster_id} not found.")

    # ==== Immunity Operations ====

    # Create (Add) a new immunity to the list
    def add_immunity(self, immunity):
        """
        Adds a new immunity to the MonsterList's immunities.

        Args:
            immunity (Immune): The Immune object to be added.
        """
        self.immunities.append(immunity)
        print(f"Added immunity: {immunity.name}")

    # Update an immunity's attributes based on its name
    def update_immunity(self, immunity_name, new_attributes):
        """
        Updates an immunity's attributes based on its name.

        Args:
            immunity_name (str): The name of the immunity to be updated.
            new_attributes (dict): A dictionary containing the new attributes to be updated.
        """
        for immunity in self.immunities:
            if immunity.name == immunity_name:
                for key, value in new_attributes.items():
                    if hasattr(immunity, key):
                        setattr(immunity, key, value)
                print(f"Updated attributes for immunity: {immunity_name}")
                return
        print(f"Immunity: {immunity_name} not found.")

    # Delete an immunity based on its name
    def delete_immunity(self, immunity_name):
        """
        Deletes an immunity based on its name.

        Args:
            immunity_name (str): The name of the immunity to be deleted.
        """
        for immunity in self.immunities:
            if immunity.name == immunity_name:
                self.immunities.remove(immunity)
                print(f"Deleted immunity: {immunity_name}")
                return
        print(f"Immunity: {immunity_name} not found.")

    # ==== Vuln Operations ====

    # Create (Add) a new vulnerability to the list
    def add_vulnerability(self, vulnerability):
        """
        Adds a new vulnerability to the MonsterList's vulnerabilities.

        Args:
            vulnerability (Vuln): The Vuln object to be added.
        """
        self.vulnerabilities.append(vulnerability)
        print(f"Added vulnerability: {vulnerability.name}")

    # Update a vulnerability's attributes based on its name
    def update_vulnerability(self, vulnerability_name, new_attributes):
        """
        Updates a vulnerability's attributes based on its name.

        Args:
            vulnerability_name (str): The name of the vulnerability to be updated.
            new_attributes (dict): A dictionary containing the new attributes to be updated.
        """
        for vulnerability in self.vulnerabilities:
            if vulnerability.name == vulnerability_name:
                for key, value in new_attributes.items():
                    if hasattr(vulnerability, key):
                        setattr(vulnerability, key, value)
                print(f"Updated attributes for vulnerability: {vulnerability_name}")
                return
        print(f"Vulnerability: {vulnerability_name} not found.")

    # Delete a vulnerability based on its name
    def delete_vulnerability(self, vulnerability_name):
        """
        Deletes a vulnerability based on its name.

        Args:
            vulnerability_name (str): The name of the vulnerability to be deleted.
        """
        for vulnerability in self.vulnerabilities:
            if vulnerability.name == vulnerability_name:
                self.vulnerabilities.remove(vulnerability)
                print(f"Deleted vulnerability: {vulnerability_name}")
                return
        print(f"Vulnerability: {vulnerability_name} not found.")

    # ==== Resist Operations ====

    # Create (Add) a new resistance to the list
    def add_resistance(self, resistance):
        """
        Adds a new resistance to the MonsterList's resistances.

        Args:
            resistance (Resist): The Resist object to be added.
        """
        self.resistances.append(resistance)
        print(f"Added resistance: {resistance.name}")

    # Update a resistance's attributes based on its name
    def update_resistance(self, resistance_name, new_attributes):
        """
        Updates a resistance's attributes based on its name.

        Args:
            resistance_name (str): The name of the resistance to be updated.
            new_attributes (dict): A dictionary containing the new attributes to be updated.
        """
        for resistance in self.resistances:
            if resistance.name == resistance_name:
                for key, value in new_attributes.items():
                    if hasattr(resistance, key):
                        setattr(resistance, key, value)
                print(f"Updated attributes for resistance: {resistance_name}")
                return
        print(f"Resistance: {resistance_name} not found.")

    # Delete a resistance based on its name
    def delete_resistance(self, resistance_name):
        """
        Deletes a resistance based on its name.

        Args:
            resistance_name (str): The name of the resistance to be deleted.
        """
        for resistance in self.resistances:
            if resistance.name == resistance_name:
                self.resistances.remove(resistance)
                print(f"Deleted resistance: {resistance_name}")
                return
        print(f"Resistance: {resistance_name} not found.")

    # ==== Family Operations ====

    # Create (Add) a new family to the list
    def add_family(self, family):
        """
        Adds a new family to the MonsterList's families.

        Args:
            family (Family): The Family object to be added.
        """
        self.families.append(family)
        print(f"Added family: {family.name}")

    # Update a family's attributes based on its name
    def update_family(self, family_name, new_attributes):
        """
        Updates a family's attributes based on its name.

        Args:
            family_name (str): The name of the family to be updated.
            new_attributes (dict): A dictionary containing the new attributes to be updated.
        """
        for family in self.families:
            if family.name == family_name:
                for key, value in new_attributes.items():
                    if hasattr(family, key):
                        setattr(family, key, value)
                print(f"Updated attributes for family: {family_name}")
                return
        print(f"Family: {family_name} not found.")

    # Delete a family based on its name
    def delete_family(self, family_name):
        """
        Deletes a family based on its name.

        Args:
            family_name (str): The name of the family to be deleted.
        """
        for family in self.families:
            if family.name == family_name:
                self.families.remove(family)
                print(f"Deleted family: {family_name}")
                return
        print(f"Family: {family_name} not found.")
            # Create (Add) a new family to the list

    def add_ability(self, ability):
        """
        Adds a new ability to the MonsterList's abilities.

        Args:
            ability (Ability): The Ability object to be added.
        """
        self.families.append(ability)
        print(f"Added family: {ability.name}")

    # Update a family's attributes based on its name
    def update_ability(self, ability_name, new_attributes):
        """
        Updates a ability's attributes based on its name.

        Args:
            family_name (str): The name of the ability to be updated.
            new_attributes (dict): A dictionary containing the new attributes to be updated.
        """
        for ability in self.abilities:
            if ability.name == ability_name:
                for key, value in new_attributes.items():
                    if hasattr(ability, key):
                        setattr(ability, key, value)
                print(f"Updated attributes for family: {ability_name}")
                return
        print(f"Ability: {ability_name} not found.")

    # Delete a family based on its name
    def delete_ability(self, ability_name):
        """
        Deletes a ability based on its name.

        Args:
            ability_name (str): The name of the ability to be deleted.
        """
        for ability in self.abilities:
            if ability.name == ability_name:
                self.abilities.remove(ability)
                print(f"Deleted ability: {ability_name}")
                return
        print(f"Ability: {ability_name} not found.")