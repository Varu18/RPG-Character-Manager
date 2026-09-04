import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import subprocess


class RPGGame:
    def __init__(self):
        self.app_directory = Path(__file__).resolve().parent
        self.process = subprocess.Popen(
            [str(self.app_directory / "rpg_core")],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1,
            cwd=self.app_directory,
        )

        self.player_name = ""
        self.player_class = ""
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.gold = 0
        self.xp = 0

        self.inventory = [None] * 5

        self.monster_name = ""
        self.monster_hp = 0
        self.monster_max_hp = 0
        self.in_battle = False

        self.item_action_mode = ""

        self.window = tk.Tk()
        self.window.title("RPG Character by VRU")
        self.window.geometry("900x600")
        self.window.configure(bg="#1a1a1a")

        self.build_gui()

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.exit_game
        )

    def send_command(self, command, extra=None):
        self.process.stdin.write(command + "\n")

        if extra:
            for value in extra:
                self.process.stdin.write(value + "\n")

        self.process.stdin.flush()

    def read_line(self):
        line = self.process.stdout.readline()
        if not line:
            raise RuntimeError("The C++ game engine stopped unexpectedly.")
        return line.strip()

    def show_error(self, message):
        messagebox.showerror("RPG Character", message, parent=self.window)

    def build_gui(self):
        self.title = tk.Label(
            self.window,
            text="⚔ RPG CHARACTER ⚔",
            font=("Cinzel", 24),
            bg="#1a1a1a",
            fg="white"
        )
        self.title.pack(pady=40)

        self.welcome = tk.Label(
            self.window,
            text="Welcome, adventurer!",
            font=("Cinzel", 16),
            bg="#1a1a1a",
            fg="white"
        )
        self.welcome.pack(pady=10)

        self.start_button = tk.Button(
            self.window,
            text="⚔ START GAME ⚔",
            command=self.start_game,
            font=("Cinzel", 12)
        )
        self.start_button.pack(pady=20)

        self.create_screen = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )

        self.name_label = tk.Label(
            self.create_screen,
            text="Character Name:",
            font=("Cinzel", 16),
            bg="#1a1a1a",
            fg="white"
        )

        self.name_entry = tk.Entry(
            self.create_screen,
            font=("Arial", 14)
        )

        self.class_label = tk.Label(
            self.create_screen,
            text="Character Class:",
            font=("Cinzel", 16),
            bg="#1a1a1a",
            fg="white"
        )

        self.class_entry = tk.Entry(
            self.create_screen,
            font=("Arial", 14)
        )

        self.create_button = tk.Button(
            self.create_screen,
            text="⚔ CREATE CHARACTER ⚔",
            command=self.create_character,
            font=("Cinzel", 12)
        )

        self.character_frame = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )

        self.stats_frame = tk.Frame(
            self.character_frame,
            bg="#1a1a1a"
        )

        self.character_name_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Cinzel", 16),
            bg="#1a1a1a",
            fg="white"
        )

        self.character_info_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Cinzel", 14),
            bg="#1a1a1a",
            fg="white"
        )

        self.inventory_frame = tk.Frame(
            self.character_frame,
            bg="#1a1a1a",
            highlightbackground="white",
            highlightthickness=1
        )

        self.inventory_title = tk.Label(
            self.inventory_frame,
            text="INVENTORY",
            font=("Cinzel", 16),
            bg="#1a1a1a",
            fg="white"
        )

        self.inventory_slots = []

        for i in range(5):
            slot = tk.Label(
                self.inventory_frame,
                text=f"Slot {i + 1}: EMPTY",
                font=("Cinzel", 12),
                bg="#1a1a1a",
                fg="white",
                relief="solid",
                bd=2,
                highlightbackground="white",
                highlightthickness=1,
                padx=10,
                pady=10
            )

            self.inventory_slots.append(slot)

        self.menu_frame = tk.Frame(
            self.character_frame,
            bg="#1a1a1a"
        )

        self.battle_button = tk.Button(
            self.menu_frame,
            text="⚔ BATTLE ⚔",
            font=("Cinzel", 12),
            command=self.start_battle
        )

        self.inventory_button = tk.Button(
            self.menu_frame,
            text="🎒 INVENTORY 🎒",
            font=("Cinzel", 12),
            command=self.open_inventory
        )

        self.heal_button = tk.Button(
            self.menu_frame,
            text="❤️ HEAL ❤️",
            font=("Cinzel", 12),
            command=self.heal
        )

        self.inventory_screen = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )

        self.inventory_screen_title = tk.Label(
            self.inventory_screen,
            text="🎒 INVENTORY 🎒",
            font=("Cinzel", 20),
            bg="#1a1a1a",
            fg="white"
        )

        self.inventory_screen_slots_frame = tk.Frame(
            self.inventory_screen,
            bg="#1a1a1a"
        )

        self.inventory_screen_slots = []

        for i in range(5):
            slot = tk.Label(
                self.inventory_screen_slots_frame,
                text=f"Slot {i + 1}: EMPTY",
                font=("Cinzel", 13),
                bg="#1a1a1a",
                fg="white",
                relief="solid",
                bd=2,
                highlightbackground="white",
                highlightthickness=1,
                padx=20,
                pady=15
            )

            self.inventory_screen_slots.append(slot)

        self.inventory_actions_frame = tk.Frame(
            self.inventory_screen,
            bg="#1a1a1a"
        )

        self.use_item_button = tk.Button(
            self.inventory_actions_frame,
            text="🧪 USE ITEM",
            font=("Cinzel", 12),
            command=self.open_use_item
        )

        self.remove_item_button = tk.Button(
            self.inventory_actions_frame,
            text="🗑 REMOVE ITEM",
            font=("Cinzel", 12),
            command=self.open_remove_item
        )

        self.inventory_back_button = tk.Button(
            self.inventory_actions_frame,
            text="← BACK",
            font=("Cinzel", 12),
            command=self.show_character_screen
        )

        self.item_action_screen = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )

        self.item_action_title = tk.Label(
            self.item_action_screen,
            text="",
            font=("Cinzel", 20),
            bg="#1a1a1a",
            fg="white"
        )

        self.item_action_label = tk.Label(
            self.item_action_screen,
            text="Select inventory slot:",
            font=("Cinzel", 14),
            bg="#1a1a1a",
            fg="white"
        )

        self.item_slot_entry = tk.Entry(
            self.item_action_screen,
            font=("Arial", 14),
            width=5
        )

        self.item_action_button = tk.Button(
            self.item_action_screen,
            text="CONFIRM",
            font=("Cinzel", 12),
            command=self.confirm_item_action
        )

        self.item_action_back_button = tk.Button(
            self.item_action_screen,
            text="← BACK",
            font=("Cinzel", 12),
            command=self.open_inventory
        )

        self.battle_screen = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )

        self.battle_title = tk.Label(
            self.battle_screen,
            text="⚔ BATTLE ⚔",
            font=("Cinzel", 22),
            bg="#1a1a1a",
            fg="white"
        )

        self.monster_label = tk.Label(
            self.battle_screen,
            text="",
            font=("Cinzel", 18),
            bg="#1a1a1a",
            fg="white"
        )

        self.monster_hp_label = tk.Label(
            self.battle_screen,
            text="",
            font=("Cinzel", 14),
            bg="#1a1a1a",
            fg="white"
        )

        self.battle_player_label = tk.Label(
            self.battle_screen,
            text="",
            font=("Cinzel", 16),
            bg="#1a1a1a",
            fg="white"
        )

        self.battle_player_hp_label = tk.Label(
            self.battle_screen,
            text="",
            font=("Cinzel", 14),
            bg="#1a1a1a",
            fg="white"
        )

        self.battle_message_label = tk.Label(
            self.battle_screen,
            text="",
            font=("Cinzel", 13),
            bg="#1a1a1a",
            fg="white"
        )

        self.battle_actions = tk.Frame(
            self.battle_screen,
            bg="#1a1a1a"
        )

        self.attack_button = tk.Button(
            self.battle_actions,
            text="⚔ ATTACK",
            font=("Cinzel", 12),
            command=self.attack
        )

        self.battle_item_button = tk.Button(
            self.battle_actions,
            text="🧪 USE ITEM",
            font=("Cinzel", 12),
            command=self.open_battle_item
        )

        self.run_button = tk.Button(
            self.battle_actions,
            text="🏃 RUN",
            font=("Cinzel", 12),
            command=self.run_from_battle
        )


        self.battle_back_button = tk.Button(
            self.battle_actions,
            text="← BACK",
            font=("Cinzel", 12),
            command=self.back_from_battle
        )

        self.battle_item_screen = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )

        self.battle_item_title = tk.Label(
            self.battle_item_screen,
            text="🧪 USE ITEM",
            font=("Cinzel", 20),
            bg="#1a1a1a",
            fg="white"
        )

        self.battle_item_label = tk.Label(
            self.battle_item_screen,
            text="Select inventory slot:",
            font=("Cinzel", 14),
            bg="#1a1a1a",
            fg="white"
        )

        self.battle_item_entry = tk.Entry(
            self.battle_item_screen,
            font=("Arial", 14),
            width=5
        )

        self.battle_item_confirm = tk.Button(
            self.battle_item_screen,
            text="USE",
            font=("Cinzel", 12),
            command=self.confirm_battle_item
        )

        self.battle_item_back = tk.Button(
            self.battle_item_screen,
            text="← BACK",
            font=("Cinzel", 12),
            command=self.show_battle_screen
        )

        self.result_screen = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )

        self.result_title = tk.Label(
            self.result_screen,
            text="",
            font=("Cinzel", 22),
            bg="#1a1a1a",
            fg="white"
        )

        self.result_message = tk.Label(
            self.result_screen,
            text="",
            font=("Cinzel", 14),
            bg="#1a1a1a",
            fg="white",
            justify="center"
        )

        self.result_back_button = tk.Button(
            self.result_screen,
            text="← CHARACTER",
            font=("Cinzel", 12),
            command=self.show_character_screen
        )

        self.bottom_bar = tk.Frame(
            self.window,
            bg="#1a1a1a"
        )
        self.bottom_bar.pack(
            side="bottom",
            fill="x"
        )

        self.exit_button = tk.Button(
            self.bottom_bar,
            text="⚔ EXIT ⚔",
            command=self.exit_game,
            font=("Cinzel", 12)
        )
        self.exit_button.pack(pady=10)

    def hide_all_screens(self):
        self.create_screen.pack_forget()
        self.character_frame.pack_forget()
        self.inventory_screen.pack_forget()
        self.item_action_screen.pack_forget()
        self.battle_screen.pack_forget()
        self.battle_item_screen.pack_forget()
        self.result_screen.pack_forget()

    def start_game(self):
        self.welcome.pack_forget()
        self.start_button.pack_forget()

        self.create_screen.pack(pady=20)

        self.name_label.pack(pady=5)
        self.name_entry.pack(pady=5)

        self.class_label.pack(pady=5)
        self.class_entry.pack(pady=5)

        self.create_button.pack(pady=30)

    def create_character(self):
        name = self.name_entry.get().strip()
        player_class = self.class_entry.get().strip()

        if not name or not player_class:
            self.show_error("Enter both a character name and class.")
            return

        self.send_command(
            "CREATE",
            [name, player_class]
        )

        self.read_line()

        state = self.read_line()
        inventory = self.read_line()

        self.parse_state(state)
        self.parse_inventory(inventory)

        self.show_character_screen()

    def parse_state(self, data):
        parts = data.split("|")

        if len(parts) < 8:
            return

        if parts[0] != "STATE":
            return

        self.player_name = parts[1]
        self.player_class = parts[2]
        self.level = int(parts[3])
        self.hp = int(parts[4])
        self.max_hp = int(parts[5])
        self.gold = int(parts[6])
        self.xp = int(parts[7])

    def parse_inventory(self, data):
        parts = data.split("|")

        if not parts or parts[0] != "INVENTORY":
            return

        self.inventory = []

        for item in parts[1:6]:
            if item == "EMPTY":
                self.inventory.append(None)
            else:
                values = item.split(",")

                self.inventory.append({
                    "name": values[0],
                    "type": values[1],
                    "value": int(values[2])
                })

        while len(self.inventory) < 5:
            self.inventory.append(None)

        self.update_inventory_widgets()

    def update_inventory_widgets(self):
        for i in range(5):
            if self.inventory[i] is None:
                text = f"Slot {i + 1}: EMPTY"
            else:
                text = f"Slot {i + 1}: {self.inventory[i]['name']}"

            self.inventory_slots[i].config(text=text)
            self.inventory_screen_slots[i].config(text=text)

    def update_character_widgets(self):
        self.character_name_label.config(
            text=f"⚔ {self.player_name}"
        )

        self.character_info_label.config(
            text=(
                f"LEVEL: {self.level}    "
                f"CLASS: {self.player_class}    "
                f"HP: {self.hp} / {self.max_hp}    "
                f"GOLD: {self.gold}    "
                f"XP: {self.xp}"
            )
        )

    def show_character_screen(self):
        self.hide_all_screens()

        self.update_character_widgets()
        self.update_inventory_widgets()

        self.character_frame.pack(pady=10)

        self.stats_frame.pack(pady=10)

        self.character_name_label.pack()
        self.character_info_label.pack()

        self.inventory_frame.pack(
            pady=10,
            padx=10
        )

        self.inventory_title.pack(pady=20)

        for slot in self.inventory_slots:
            slot.pack(
                side="left",
                padx=10,
                pady=10
            )

        self.menu_frame.pack(pady=20)

        self.battle_button.pack(
            side="left",
            padx=10
        )

        self.inventory_button.pack(
            side="left",
            padx=10
        )

        self.heal_button.pack(
            side="left",
            padx=10
        )

    def open_inventory(self):
        self.send_command("INVENTORY")

        inventory = self.read_line()
        self.parse_inventory(inventory)

        self.hide_all_screens()

        self.inventory_screen.pack(
            pady=20,
            fill="both",
            expand=True
        )

        self.inventory_screen_title.pack(pady=30)

        self.inventory_screen_slots_frame.pack(pady=20)

        for slot in self.inventory_screen_slots:
            slot.pack(
                side="left",
                padx=10
            )

        self.inventory_actions_frame.pack(pady=30)

        self.use_item_button.pack(
            side="left",
            padx=10
        )

        self.remove_item_button.pack(
            side="left",
            padx=10
        )

        self.inventory_back_button.pack(
            side="left",
            padx=10
        )

    def open_use_item(self):
        self.item_action_mode = "use"

        self.hide_all_screens()

        self.item_action_screen.pack(pady=30)

        self.item_action_title.config(
            text="🧪 USE ITEM"
        )

        self.item_action_title.pack(pady=30)
        self.item_action_label.pack(pady=10)
        self.item_slot_entry.pack(pady=10)
        self.item_action_button.pack(pady=20)
        self.item_action_back_button.pack(pady=10)

    def open_remove_item(self):
        self.item_action_mode = "remove"

        self.hide_all_screens()

        self.item_action_screen.pack(pady=30)

        self.item_action_title.config(
            text="🗑 REMOVE ITEM"
        )

        self.item_action_title.pack(pady=30)
        self.item_action_label.pack(pady=10)
        self.item_slot_entry.pack(pady=10)
        self.item_action_button.pack(pady=20)
        self.item_action_back_button.pack(pady=10)

    def confirm_item_action(self):
        value = self.item_slot_entry.get().strip()

        if not value.isdigit():
            return

        slot = int(value)

        if slot < 1 or slot > 5:
            return

        if self.item_action_mode == "use":
            self.send_command(
                "USE_ITEM",
                [str(slot)]
            )

            result = self.read_line()

            if result.startswith("ITEM_RESULT|SUCCESS"):
                state = self.read_line()
                self.parse_state(state)

                next_line = self.read_line()

                if next_line.startswith("BATTLE|"):
                    self.parse_battle_state(next_line)

                elif next_line.startswith("INVENTORY|"):
                    self.parse_inventory(next_line)

                if self.in_battle:
                    inventory = self.read_line()

                    if inventory.startswith("INVENTORY|"):
                        self.parse_inventory(inventory)
            else:
                self.show_error(result.split("|", 2)[-1])
                self.item_slot_entry.delete(0, tk.END)
                return

        elif self.item_action_mode == "remove":
            self.send_command(
                "REMOVE_ITEM",
                [str(slot)]
            )

            result = self.read_line()

            if result.startswith("REMOVE_RESULT|SUCCESS"):
                inventory = self.read_line()
                self.parse_inventory(inventory)
            else:
                self.show_error(result.split("|", 2)[-1])
                self.item_slot_entry.delete(0, tk.END)
                return

        self.item_slot_entry.delete(0, tk.END)
        self.open_inventory()

    def start_battle(self):
        self.send_command("BATTLE_START")

        result = self.read_line()

        if result.startswith("ERROR|"):
            self.show_result(
                "⚠ ERROR",
                result.split("|", 1)[1]
            )
            return

        if not result.startswith("BATTLE_STARTED|"):
            self.show_error("The game engine returned an unexpected response.")
            return

        self.in_battle = True
        self.monster_name = result.split("|", 1)[1]

        self.read_battle_state()
        self.show_battle_screen()

    def read_battle_state(self):
        data = self.read_line()

        if data.startswith("BATTLE|"):
            self.parse_battle_state(data)

    def parse_battle_state(self, data):
        parts = data.split("|")

        if len(parts) < 6:
            return

        if parts[1] == "NONE":
            self.in_battle = False
            return

        self.in_battle = True
        self.monster_name = parts[1]
        self.monster_hp = int(parts[2])
        self.monster_max_hp = int(parts[3])
        self.hp = int(parts[4])
        self.max_hp = int(parts[5])

    def show_battle_screen(self):
        self.hide_all_screens()

        self.battle_screen.pack(pady=30)

        self.battle_title.pack(pady=20)

        self.monster_label.config(
            text=f"👹 {self.monster_name}"
        )
        self.monster_label.pack(pady=10)

        self.monster_hp_label.config(
            text=f"❤️ HP: {self.monster_hp} / {self.monster_max_hp}"
        )
        self.monster_hp_label.pack(pady=10)

        self.battle_player_label.config(
            text=f"👤 {self.player_name}"
        )
        self.battle_player_label.pack(pady=20)

        self.battle_player_hp_label.config(
            text=f"❤️ HP: {self.hp} / {self.max_hp}"
        )
        self.battle_player_hp_label.pack(pady=10)

        self.battle_message_label.pack(pady=20)

        self.battle_actions.pack(pady=20)

        self.attack_button.pack(
            side="left",
            padx=10
        )

        self.battle_item_button.pack(
            side="left",
            padx=10
        )

        self.run_button.pack(
            side="left",
            padx=10
        )

        self.battle_back_button.pack(
            side="left",
            padx=10
        )


    def update_battle_widgets(self):
        self.monster_label.config(
            text=f"👹 {self.monster_name}"
        )

        self.monster_hp_label.config(
            text=f"❤️ HP: {self.monster_hp} / {self.monster_max_hp}"
        )

        self.battle_player_label.config(
            text=f"👤 {self.player_name}"
        )

        self.battle_player_hp_label.config(
            text=f"❤️ HP: {self.hp} / {self.max_hp}"
        )

    def attack(self):
        self.send_command("ATTACK")

        result = self.read_line()

        if not result.startswith("ATTACK_RESULT|"):
            if result.startswith("ERROR|"):
                self.show_error(result.split("|", 1)[1])
            return

        parts = result.split("|")

        damage = int(parts[1])
        result_type = parts[2]
        gold = int(parts[3])
        xp = int(parts[4])
        level_up = int(parts[5])

        if result_type == "CONTINUE":
            battle_state = self.read_line()
            self.parse_battle_state(battle_state)

            state = self.read_line()
            self.parse_state(state)

            self.battle_message_label.config(
                text=f"⚔ You dealt {damage} damage!"
            )

            self.update_battle_widgets()

        elif result_type == "DEFEATED":
            self.in_battle = False

            state = self.read_line()
            self.parse_state(state)

            message = (
                f"💀 {self.monster_name} has been defeated!\n\n"
                f"💰 Gold: +{gold}\n"
                f"✨ XP: +{xp}"
            )

            if level_up:
                message += "\n\n⭐ LEVEL UP!"

            self.show_result(
                "🏆 VICTORY",
                message
            )

        elif result_type == "GAME_OVER":
            self.in_battle = False

            state = self.read_line()
            self.parse_state(state)

            self.show_result(
                "💀 GAME OVER",
                "You have been defeated!"
            )

    def open_battle_item(self):
        self.hide_all_screens()

        self.battle_item_screen.pack(pady=30)

        self.battle_item_title.pack(pady=30)
        self.battle_item_label.pack(pady=10)
        self.battle_item_entry.pack(pady=10)
        self.battle_item_confirm.pack(pady=20)
        self.battle_item_back.pack(pady=10)

    def confirm_battle_item(self):
        value = self.battle_item_entry.get().strip()

        if not value.isdigit():
            return

        slot = int(value)

        if slot < 1 or slot > 5:
            return

        self.send_command(
            "USE_ITEM",
            [str(slot)]
        )

        result = self.read_line()

        if not result.startswith("ITEM_RESULT|SUCCESS"):
            self.show_error(result.split("|", 2)[-1])
            self.battle_item_entry.delete(0, tk.END)
            return

        state = self.read_line()
        self.parse_state(state)

        battle_state = self.read_line()

        if battle_state.startswith("BATTLE|"):
            self.parse_battle_state(battle_state)

        inventory = self.read_line()

        if inventory.startswith("INVENTORY|"):
            self.parse_inventory(inventory)

        self.battle_item_entry.delete(0, tk.END)

        self.show_battle_screen()

        self.battle_message_label.config(
            text="🧪 Item used successfully!"
        )

        self.update_battle_widgets()

    def heal(self):
        self.send_command("HEAL")

        result = self.read_line()

        if result.startswith("HEAL_RESULT|"):
            state = self.read_line()
            self.parse_state(state)

            self.show_character_screen()
        elif result.startswith("ERROR|"):
            self.show_error(result.split("|", 1)[1])

    def run_from_battle(self):
        if not self.in_battle:
            self.show_character_screen()
            return

        self.send_command("RUN")

        result = self.read_line()

        if result.startswith("RUN_RESULT|SUCCESS"):
            self.in_battle = False
            self.show_character_screen()
        elif result.startswith("ERROR|"):
            self.show_error(result.split("|", 1)[1])

    def back_from_battle(self):
        if self.in_battle:
            self.send_command("RUN")
            result = self.read_line()

            if result.startswith("RUN_RESULT|SUCCESS"):
                self.in_battle = False

        self.show_character_screen()

    def show_result(self, title, message):
        self.hide_all_screens()

        self.result_screen.pack(pady=50)

        self.result_title.config(
            text=title
        )
        self.result_title.pack(pady=30)

        self.result_message.config(
            text=message
        )
        self.result_message.pack(pady=20)

        self.result_back_button.pack(pady=30)

    def exit_game(self):
        try:
            self.send_command("EXIT")
            self.process.stdin.close()
            self.process.stdout.close()
            self.process.wait(timeout=2)
        except:
            try:
                self.process.kill()
            except:
                pass

        self.window.destroy()

    def start(self):
        self.window.mainloop()


game = RPGGame()
game.start()
