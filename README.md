# 🌐 CIPHERNET: The Resistance

A Cyberpunk-themed Text RPG built with Python, focusing on modularity, Object-Oriented Programming (OOP), and immersive terminal aesthetics.

🎓 Reflections & Learning Journey

🚀 Challenges Faced
- Transitioning to OOP: The biggest hurdle was moving away from simple procedural dictionaries to a Class-based architecture. Designing the Character and Enemy classes required me to think about data as objects with state and behavior, which was a significant shift in my programming mindset.
- Code Modularity: Managing three separate files (game.py, entities.py, graphics.py) was a challenge in organization. I had to learn how to handle imports correctly to ensure the logic remained clean and decoupled from the visual assets.
- Terminal Animation (The Typewriter Effect): During development, I encountered an issue where text would appear all at once instead of character-by-character. I had to research how Python handles output buffering and learned why sys.stdout.flush() is critical for forcing the terminal to render characters immediately.

💡 What I Learned & Gained
- Encapsulation: I discovered how much more robust code becomes when using Classes. Methods like take_damage() and heal_full() allowed me to control how character data is modified, preventing bugs that common global variables often cause.
- User Experience (UX) Design: I learned that even in a text-based environment, visual feedback (ASCII art, colors, and timing) drastically changes how a user interacts with the software.
- Professional Engineering Standards: This project taught me the importance of documentation (README.md) and dependency management (requirements.txt), which are essential skills for real-world development.

📜 Key Features
- OOP Core: Robust class-based system for Characters, Enemies, and Items.
- Mission Progression: Gather Intel in different districts to unlock the final "Soulnet Tower" assault.
- Interactive Hub: Visit the Safe House for stat upgrades or the Black Market for equipment.
- Immersive FX: Typewriter animations and "screen shake" effects using standard Python libraries.

🛠️ Tech Stack
- Language: Python 3.x
- Libraries: colorama (for cross-platform terminal colors), sys, os, time, random.

📂 File Structure
- game.py: The main game loop and mission logic.
- entities.py: The OOP blueprints for characters and items.
- graphics.py: The visual engine and animation handlers.

🎮 Setup & Play
1. Install dependencies:
pip install -r requirements.txt

3. Launch the game:
python game.py

Developed by: Muhammad Sharjeel Zahid
