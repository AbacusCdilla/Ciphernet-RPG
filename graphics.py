import sys
import time
import os
import random
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Colors
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

# --- SCENE ART ---

TITLE_ART = r"""
   ______ ____  ____   __  __ ______ ____   _   __ ______ ________
  / ____//  _/ / __ \ / / / // ____// __ \ / | / // ____//__  ___/
 / /     / /  / /_/ // /_/ // __/  / /_/ //  |/ // __/     / /   
/ /___ _/ /  / ____// __  // /___ / _, _// /|  // /___    / /    
\____//___/ /_/    /_/ /_//_____//_/ |_|/_/ |_//_____/   /_/     
"""

PORT_SCENE = r"""
      |    |
  ___|____|___
  \  O  O  O /   [ SECTOR 7: THE PORT ]
~~~~~~~~~~~~~~~~
"""

NEON_DISTRICT = r"""
   | |   | |
  _|_|_ _|_|_    [ NEON DISTRICT ]
  |___| |___|
  |___| |___|
"""

CORP_TOWER = r"""
      /|\
     | | |
     | | |       [ SOULNET TOWER ]
     | | |       Target: Server Room
     | | |
    /_____\
"""

WAREHOUSE_ART = r"""
   _________________
  |   ___________   |
  |  |           |  |    [ THE SAFE HOUSE ]
  |  |   [BED]   |  |     Rest & Upgrade
  |__|___________|__|
"""

MARKET_ART = r"""
      _.._
    .' .-'`
   /  /
   |  |    [ BLACK MARKET ]
   \  \    Weapons & Stims
    '._'-._
       ```
"""

# --- CHARACTER VISUALS ---

GUARD_ART = r"""
      ▄▄▄▄▄▄▄
     ██░░░░░██
     ██░▀░▀░██   [ CORP GUARD ]
      ██████
     ▄██████▄
"""

DRONE_ART = r"""
      \ /
    -- O --      [ SECURITY DRONE ]
      / \
     /   \
"""

NETRUNNER_ART = r"""
    __  __
   (  )(  )      [ ROGUE NETRUNNER ]
   __||||__
  / _    _ \
"""

ENFORCER_ART = r"""
    ,_____,
    | ___ |
    |[_ _]|      [ ELITE ENFORCER ]
    |  L  |
    /`---'\
"""

GAME_OVER_ART = r"""
  ____                           ___                 
 / ___|  __  _ _ __ ___    ___  / _ \ __   __ ___  _ ___
| |  _  / _`  | '_ ` _ \  / _ \| | | \\ \ / // _ \|  '__|
| |_| || (_|  | | | | | ||  __/| |_| | \ V /|  __/|  |   
 \____| \__,_ |_| |_| |_| \___| \___/   \_/  \___||__| 
"""

# --- ANIMATION FUNCTIONS ---

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, speed=0.03, color=GREEN):
    """
    Creates a typewriter effect by printing character by character.
    
    Technical Note:
    - sys.stdout.write is used instead of print() to avoid automatic new lines.
    - sys.stdout.flush() is critical because Python buffers text by default. 
      Flush forces each character to the screen immediately for a smooth animation.
    """
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print() # New line at the end

def instant_print(text, color=GREEN):
    print(color + text + RESET)

def matrix_rain():
    chars = "010101XYZ"
    for i in range(10):
        line = ""
        for j in range(60):
            line += random.choice(chars)
        print(GREEN + line)
        time.sleep(0.05)
    clear_screen()

def screen_shake():
    for i in range(2):
        print("\n")
        time.sleep(0.05)
        clear_screen()
        time.sleep(0.05)
