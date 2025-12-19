import random
import time
import graphics
import entities

# --- CORE MATH ---
def init_stats(player, choice):
    if choice in player.stats:
        player.stats[choice] += 1
    # Fill randoms (Logic)
    for k in player.stats:
        if player.stats[k] == 0:
            player.stats[k] = random.randint(1, 4)

def calculate_damage(stats_dict):
    base = random.randint(3, 7)
    str_b = stats_dict["Strength"] * random.randint(1, 3)
    cld_b = round(stats_dict["Cold"] * 0.5)
    int_b = random.randint(0, stats_dict["Intelligence"])
    total = base + str_b + cld_b + int_b
    return total, f"Base:{base}+Bonus:{total-base}"

# --- INVENTORY SYSTEM ---
def show_inventory(player):
    graphics.clear_screen()
    graphics.instant_print("=== BACKPACK ===", graphics.YELLOW)
    if not player.inventory:
        print("Empty.")
    else:
        for i, item in enumerate(player.inventory):
            print(f"{i+1}. {item.name} ({item.desc})")
    print("-" * 30)
    input("Press Enter to close...")

def use_item_in_combat(player, enemy):
    graphics.clear_screen()
    print("Select item to use:")
    for i, item in enumerate(player.inventory):
        print(f"{i+1}. {item.name}")
    print("0. Cancel")
    
    try:
        choice = int(input("> "))
        if choice == 0: return False
        
        item = player.inventory[choice - 1]
        
        if item.item_type == "heal":
            player.hp += item.value
            if player.hp > player.max_hp: player.hp = player.max_hp
            graphics.slow_print(f"Used {item.name}. HP: {player.hp}", 0.02, graphics.GREEN)
            player.inventory.pop(choice - 1)
            return True
            
        elif item.item_type == "damage":
            enemy.hp -= item.value
            if enemy.hp < 0: enemy.hp = 0
            graphics.slow_print(f"BOOM! {item.name} dealt {item.value} DMG!", 0.02, graphics.RED)
            player.inventory.pop(choice - 1)
            return True
    except:
        print("Invalid choice.")
    return False

# --- COMBAT ---
def run_combat(player, enemy):
    graphics.clear_screen()
    if "Drone" in enemy.name: graphics.instant_print(graphics.DRONE_ART, graphics.CYAN)
    elif "Netrunner" in enemy.name: graphics.instant_print(graphics.NETRUNNER_ART, graphics.MAGENTA)
    elif "Enforcer" in enemy.name: graphics.instant_print(graphics.ENFORCER_ART, graphics.RED)
    else: graphics.instant_print(graphics.GUARD_ART, graphics.RED)
        
    graphics.instant_print(f"WARNING: {enemy.name} DETECTED", graphics.RED)
    time.sleep(1)

    while player.is_alive() and enemy.hp > 0:
        print("-" * 40)
        graphics.instant_print(f"{player.name}: {player.hp}/{player.max_hp} HP", graphics.CYAN)
        graphics.instant_print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP", graphics.RED)
        print("-" * 40)
        print("1. Attack")
        print("2. Use Item")
        print("3. Run")
        
        choice = input(graphics.CYAN + "> " + graphics.RESET)
        action_taken = False
        
        if choice == "1":
            dmg, breakdown = calculate_damage(player.stats)
            enemy.hp -= dmg
            if enemy.hp < 0: enemy.hp = 0
            graphics.slow_print(f"You hit for {dmg}! ({breakdown})", 0.01, graphics.GREEN)
            action_taken = True
        elif choice == "2":
            action_taken = use_item_in_combat(player, enemy)
        elif choice == "3":
            if random.random() > 0.5: return True
            else:
                graphics.slow_print("Escape Failed!", 0.02, graphics.RED)
                action_taken = True
        
        if enemy.hp == 0: return True
        
        if action_taken:
            edmg, ebreak = calculate_damage(enemy.stats)
            edmg = max(1, edmg // 2)
            player.take_damage(edmg)
            graphics.slow_print(f"{enemy.name} attacks for {edmg}!", 0.01, graphics.MAGENTA)
            graphics.screen_shake()
            
        if not player.is_alive(): return False

    return True

# --- LOCATIONS ---
def visit_warehouse(player):
    while True:
        graphics.clear_screen()
        graphics.instant_print(graphics.WAREHOUSE_ART, graphics.CYAN)
        print(f"Stats: STR {player.stats['Strength']} | INT {player.stats['Intelligence']} | CLD {player.stats['Cold']}")
        print(f"Credits: {player.credits}")
        print("-" * 40)
        print("1. Sleep/Heal (Free)")
        print("2. Train Strength (100c)")
        print("3. Train Intelligence (100c)")
        print("4. Train Cold (100c)")
        print("5. Exit")
        
        c = input("> ")
        if c == "1":
            player.heal_full()
            graphics.slow_print("Restored full HP.", 0.03, graphics.GREEN)
            time.sleep(1)
        elif c == "2":
            if player.upgrade_stat("Strength"): graphics.slow_print("Strength UP!", 0.03, graphics.YELLOW)
        elif c == "3":
            if player.upgrade_stat("Intelligence"): graphics.slow_print("Intelligence UP!", 0.03, graphics.YELLOW)
        elif c == "4":
            if player.upgrade_stat("Cold"): graphics.slow_print("Cold UP!", 0.03, graphics.YELLOW)
        elif c == "5": break

def visit_black_market(player):
    while True:
        graphics.clear_screen()
        graphics.instant_print(graphics.MARKET_ART, graphics.MAGENTA)
        print(f"Credits: {player.credits}")
        print("1. Stimpack (50c)")
        print("2. EMP Grenade (80c)")
        print("3. Medkit (120c)")
        print("4. Exit")
        
        c = input("> ")
        item = None
        if c == "1": item = entities.create_item("stimpack")
        elif c == "2": item = entities.create_item("grenade")
        elif c == "3": item = entities.create_item("medkit")
        elif c == "4": break
        
        if item and player.credits >= item.cost:
            player.credits -= item.cost
            player.add_item(item)
            graphics.slow_print(f"Bought {item.name}.", 0.03, graphics.GREEN)
            time.sleep(1)

def mission_location(player, location_name):
    graphics.clear_screen()
    if location_name == "Port": graphics.instant_print(graphics.PORT_SCENE, graphics.BLUE)
    else: graphics.instant_print(graphics.NEON_DISTRICT, graphics.MAGENTA)
    
    graphics.slow_print(f"Scanning {location_name}...", 0.03, graphics.WHITE)
    print("1. Gather Intel (Risk of Combat)")
    print("2. Attack Patrol (Loot/XP)")
    print("3. Leave")
    
    c = input("> ")
    if c == "1":
        roll = random.randint(1, 10) + (player.stats["Intelligence"] // 2)
        if roll > 8:
            graphics.slow_print("Hacked terminal. Intel found!", 0.03, graphics.GREEN)
            player.intel += 1
            graphics.slow_print(f"Intel Progress: {player.intel}/3", 0.03, graphics.YELLOW)
        else:
            graphics.slow_print("Hack failed! They traced you!", 0.03, graphics.RED)
            enemy = entities.create_enemy("drone")
            run_combat(player, enemy)
    elif c == "2":
        enemy = entities.create_enemy("guard")
        if run_combat(player, enemy):
            loot = random.randint(30, 60)
            player.credits += loot
            graphics.slow_print(f"Looted {loot} credits.", 0.03, graphics.YELLOW)
    time.sleep(1)

def mission_finale(player):
    graphics.clear_screen()
    graphics.instant_print(graphics.CORP_TOWER, graphics.RED)
    graphics.slow_print("Target: Soulnet Mainframe. This is for Jax.", 0.05, graphics.RED)
    graphics.slow_print("Breaching front gates...", 0.04)
    time.sleep(1)
    
    # Wave 1
    if not run_combat(player, entities.create_enemy("guard")): return
    
    graphics.slow_print("Entering Server Room...", 0.04)
    # Wave 2 (Boss)
    boss = entities.create_enemy("enforcer")
    boss.name = "Head of Security"
    boss.hp = 80
    
    if run_combat(player, boss):
        graphics.clear_screen()
        graphics.matrix_rain()
        graphics.instant_print("ACCESS GRANTED", graphics.GREEN)
        graphics.slow_print("Uploading Virus... Soulnet Servers Destroyed.", 0.05, graphics.GREEN)
        graphics.slow_print(f"Jax is avenged. Well done, {player.name}.", 0.05, graphics.CYAN)
        input("Press Enter to End Game...")
        player.hp = 0 # End game loop cleanly
    else:
        print("Mission Failed.")

# --- PROLOGUE & MAIN ---
def play_prologue(player):
    graphics.clear_screen()
    graphics.slow_print(f"Welcome to 2065, {player.name}.", 0.05, graphics.CYAN)
    graphics.slow_print("The neon sky is silent. Too silent.", 0.04)
    time.sleep(1)
    
    graphics.slow_print("\nYour neural link buzzes. It's Jax, your childhood friend.", 0.04)
    graphics.instant_print("MSG: 'R U Ready? We hit Soulnet tonight. Meet me at my place. :D'", graphics.WHITE)
    time.sleep(2)
    
    graphics.slow_print("\nYou rush to his apartment in Sector 4.", 0.04)
    graphics.slow_print("But you're too late.", 0.06, graphics.RED)
    graphics.screen_shake()
    
    graphics.slow_print("\nThe door is kicked in. His gear is smashed.", 0.04, graphics.RED)
    graphics.slow_print("A message on the wall: 'SOULNET SEES ALL'.", 0.04, graphics.RED)
    graphics.slow_print("Jax is gone. Executed by the Corps.", 0.05, graphics.RED)
    time.sleep(1)
    
    graphics.instant_print("\n[ NEW OBJECTIVE: AVENGE JAX ]", graphics.YELLOW)
    graphics.slow_print("Your mission: Gather 3 Intel, find the Server Room, burn them down.", 0.04, graphics.WHITE)
    time.sleep(2)

def main():
    graphics.matrix_rain()
    graphics.instant_print(graphics.TITLE_ART, graphics.GREEN)
    name = input("\nEnter Name: ") or "Runner"
    p = entities.Character(name, 100)
    p.add_item(entities.create_item("stimpack"))
    
    # Run Expanded Prologue
    play_prologue(p)
    
    # Class Selection
    graphics.clear_screen()
    graphics.instant_print("CHOOSE YOUR PATH", graphics.CYAN)
    print("1. Brawler (+Strength)")
    print("2. Hacker (+Intelligence)")
    print("3. Ghost (+Cold)")
    c = input("> ")
    bonus = "Strength"
    if c == "2": bonus = "Intelligence"
    if c == "3": bonus = "Cold"
    init_stats(p, bonus)
    graphics.slow_print(f"Stats Initialized. Style: {bonus}", 0.03, graphics.YELLOW)
    time.sleep(1)
    
    # HUB LOOP
    while p.is_alive():
        graphics.clear_screen()
        graphics.instant_print("--- RESISTANCE HUB ---", graphics.MAGENTA)
        print(f"Credits: {p.credits} | HP: {p.hp}")
        graphics.instant_print(f"INTEL GATHERED: {p.intel}/3", graphics.YELLOW)
        print("-" * 30)
        print("1. Sector 7: Port (Mission)")
        print("2. Neon District (Mission)")
        print("3. Black Market (Shop)")
        print("4. Safe House (Heal/Upgrade)")
        
        if p.intel >= 3:
            print(graphics.RED + "5. ASSAULT CORP TOWER (FINAL)" + graphics.RESET)
        else:
            print(graphics.WHITE + "5. [LOCKED] Need more Intel" + graphics.RESET)
            
        print("6. Backpack")
        print("7. Quit")
        
        choice = input("> ")
        
        if choice == "1": mission_location(p, "Port")
        elif choice == "2": mission_location(p, "Neon")
        elif choice == "3": visit_black_market(p)
        elif choice == "4": visit_warehouse(p)
        elif choice == "5":
            if p.intel >= 3: mission_finale(p)
            else: print("Locked.")
        elif choice == "6": show_inventory(p)
        elif choice == "7": break
            
    graphics.instant_print(graphics.GAME_OVER_ART, graphics.RED)

if __name__ == "__main__":
    main()