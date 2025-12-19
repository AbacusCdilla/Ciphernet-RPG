import random

class Item:
    def __init__(self, name, item_type, value, desc, cost):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.desc = desc
        self.cost = cost

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.inventory = [] 
        self.credits = 100
        self.intel = 0  # <--- NEW: Tracks progress towards Corp Tower
        
        # Stats Logic
        self.stats = {
            "Strength": 10, 
            "Cold": 10, 
            "Intelligence": 10
        }
        
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0: self.hp = 0
            
    def is_alive(self):
        return self.hp > 0
    
    def add_item(self, item):
        self.inventory.append(item)

    def upgrade_stat(self, stat_name):
        if self.credits >= 100:
            self.credits -= 100
            self.stats[stat_name] += 1
            return True
        return False

    def heal_full(self):
        self.hp = self.max_hp

class Enemy:
    def __init__(self, name, hp, min_dmg, max_dmg):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        # Random stats for Tahir's logic
        self.stats = {
            "Strength": random.randint(1,4),
            "Cold": random.randint(1,4),
            "Intelligence": random.randint(1,4)
        }

# --- FACTORY FUNCTIONS ---

def create_enemy(etype):
    if etype == "drone":
        return Enemy("Security Drone", 30, 4, 8)
    elif etype == "netrunner":
        return Enemy("Rogue Netrunner", 45, 8, 12)
    elif etype == "enforcer":
        return Enemy("Elite Enforcer", 60, 10, 15)
    else:
        return Enemy("Corp Guard", 40, 3, 7)

def create_item(itype):
    if itype == "stimpack":
        return Item("Stimpack", "heal", 30, "Restores 30 HP", 50)
    elif itype == "medkit":
        return Item("Mil-Spec Medkit", "heal", 80, "Full Heal", 120)
    elif itype == "grenade":
        return Item("EMP Grenade", "damage", 25, "Deals 25 DMG", 80)
