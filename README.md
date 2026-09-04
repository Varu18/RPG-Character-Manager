# RPG Character Manager

My first C++/Python console RPG project built while learning software development and C++/Python fundamentals.

This project is part of my learning journey and is developed with AI assisted guidance. Every feature is implemented step by step with the goal of understanding the underlying programming concepts rather than simply copying code.

## Current Version

Version 0.9

## Project Roadmap

### ✅ Current Milestone

Version 0.9

Focus:
- Improved the console interface.
- Added visual elements using ASCII characters and emojis.
- Added an interactive battle loop.
- Added Attack, Use Item, and Run battle options.
- Added `showBattle()` for battle information.
- Added `attackMenu()` for player actions.
- Started the Python GUI version using Tkinter.
- Added an RPG themed graphical window.
- Added Cinzel font.
- Added dark background.
- Added START GAME button.
- Added character name input.
- Added CREATE CHARACTER button.
- Practiced GUI widgets, events, functions, and user input.


### 🎯 Next Milestone

Version 1.0

Focus:
- Continue developing the Python GUI.
- Build the character creation screen.
- Add character class selection.
- Display character statistics.
- Add the inventory interface.
- Begin integrating RPG functionality into the GUI.

## Technologies

- C++
- Python
- Tkinter
- Git
- GitHub
- Visual Studio Code
- Fedora Linux

## Run the GUI

From the project folder, build the C++ engine and start the Tkinter interface:

```bash
make run
```

The GUI starts `rpg_core` as a child process and exchanges one command or game
state message per line through standard input/output. Keep the executable next
to `rpg_gui.py`; the Makefile creates it there automatically.

## Learning Goals

- Learn C++ fundamentals.
- Learn Python fundamentals.
- Practice problem solving.
- Learn Git and GitHub workflow.
- Build a complete RPG project from scratch.
- Learn to organize code using structs and functions.
- Learn GUI development using Python and Tkinter.
- Build a strong programming foundation for future languages and technologies.
- Gain hands on experience with Linux development using Fedora.
- Practice making small, focused Git commits.
- Learn how different technologies can work together inside a larger project.

## Features

- Create a custom RPG character.
- Fight random monsters.
- Heal your character.
- Earn gold from battles.
- Gain experience (XP).
- Level up your character.
- View character statistics.
- Manage an inventory of items.
- Add items to the inventory.
- Remove items from the inventory.
- Use consumable items.
- Fight monsters through an interactive battle loop.
- Attack monsters.
- Use items during battles.
- Run from battles.
- Receive rewards after defeating monsters.
- Track player and monster HP.
- Detect player death and monster defeat.
- Display battle information through a dedicated battle interface.
- Python GUI prototype with Tkinter.
- RPG themed graphical interface.
- Character name input through the GUI.

## Current Progress

Implemented features:

- ✅ Character creation
- ✅ Character statistics
- ✅ Battle system
- ✅ Interactive battle loop
- ✅ Attack option
- ✅ Use Item option
- ✅ Run option
- ✅ Healing system
- ✅ Gold system
- ✅ Experience (XP) system
- ✅ Level up system
- ✅ Random monster encounters
- ✅ Monster struct
- ✅ Monster HP and max HP
- ✅ Monster specific damage
- ✅ Player damage
- ✅ Monster death detection
- ✅ Game over handling
- ✅ Battle rewards
- ✅ Item system
- ✅ Player inventory
- ✅ Inventory display
- ✅ Add item system
- ✅ Remove item system
- ✅ Consumable items
- ✅ `showBattle()` function
- ✅ `attackMenu()` function
- ✅ Python Tkinter GUI prototype
- ✅ RPG themed GUI window
- ✅ Cinzel RPG font
- ✅ Dark GUI background
- ✅ GUI title screen
- ✅ START GAME button
- ✅ Character name input
- ✅ CREATE CHARACTER button
- ✅ GUI screen transitions
- ✅ Reading GUI input with `get()`
- ✅ Changing widget state with `config()`

## Planned Features

### C++ RPG

- Different monster stats
- Monster attacks and abilities
- More consumable items
- Save and load game
- Shop system
- Equipment system
- Boss battles

### Python GUI

- Character creation screen
- Character class selection
- Character statistics screen
- Inventory interface
- Battle interface
- Interactive battle buttons
- Health and XP displays
- Improved RPG styling
- Connect GUI functionality with RPG mechanics

### Future Project Direction

- Connect the graphical interface with the RPG logic.
- Explore communication between different programming languages.
- Experiment with local hosting.
- Eventually allow friends to interact with the game.

## Version History

### Version 0.9

- Improved the console interface.
- Added an interactive battle loop.
- Added Attack, Use Item, and Run options.
- Added monster HP tracking.
- Added player damage.
- Added monster defeat detection.
- Added game over handling.
- Added battle rewards.
- Added `showBattle()` function.
- Added `attackMenu()` function.
- Started Python GUI development using Tkinter.
- Added RPG themed graphical interface.
- Added Cinzel font.
- Added dark background.
- Added START GAME button.
- Added character name input.
- Added CREATE CHARACTER button.

### Version 0.8

- Added `useItem()` functionality.
- Added consumable item support.
- Added item effect values.
- Added Health Potion healing.
- Added automatic removal of consumed items.
- Added validation for usable items.
- Practiced boolean conditions, references, and function logic.

### Version 0.7

- Introduced the Item struct.
- Added a 5 slot inventory to the Player struct.
- Added Health Potion, Iron Sword, and Mana Potion items.
- Added inventory display.
- Added an `addItem()` function.
- Added inventory full handling.
- Practiced arrays of custom types.
- Practiced loops, conditions, references, `break`, and boolean return values.

### Version 0.6

- Refactored player data using a struct.
- Improved code organization.

### Version 0.5

- Added XP system.
- Added level up system.
- Improved battle output.
- Added random monster encounters.

### Version 0.4

- Added healing system.
- Added gold rewards.

### Version 0.3

- Initial RPG Character Manager.

## About This Project

This project is part of my journey to learn software development.

The goal is not only to build a simple RPG game, but also to learn fundamental programming concepts in C++ and Python. Every feature is implemented step by step to better understand programming, problem solving, software design, software architecture, and software development practices.

The project started as a C++ console RPG and is now expanding toward a graphical application using Python and Tkinter.

This project is developed in a Linux environment using Fedora Linux, helping me build practical experience with Linux based software development alongside C++ and Python.

This project is AI assisted. I use ChatGPT as a learning mentor to understand concepts, review my code, and improve my programming skills. All code is written, tested, and committed by me as part of the learning process.

## Feedback

I'm building this project to improve my programming skills. If you have suggestions or ideas for new features, feel free to open an issue or share your feedback.
