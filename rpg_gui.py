import tkinter as tk

class Item:
     def __init__(self, name):
          self.name = name
          
health_potion = Item("Health Potion")
iron_sword = Item("Iron Sword")

class Player:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.hp = 100
        self.gold = 0
        self.inventory = [None] * 5  

player = Player()

player.inventory[0] = health_potion
player.inventory[1] = iron_sword



def start_game():
        welcome.pack_forget()
        start_button.pack_forget()
        name_label.pack()
        name_entry.pack()
        create_button.pack(pady=30)


def create_character():
    player.name = name_entry.get()

    name_entry.config(state="disabled")
    create_button.config(state="disabled")

    character_name_label.config(text=f"⚔ {player.name}")
    character_info_label.config(
        text=f"LEVEL: {player.level}    HP: {player.hp}    GOLD: {player.gold}"
    )
    character_name_label.pack()
    character_info_label.pack()

    name_label.pack_forget()
    name_entry.pack_forget()
    create_button.pack_forget()
    character_frame.pack()
    inventory_slot_1.pack(side="left", padx=10, pady=10)
    inventory_slot_1.pack(side="left", padx=10, pady=10)
    inventory_slot_2.pack(side="left", padx=10, pady=10)
    inventory_slot_3.pack(side="left", padx=10, pady=10)
    inventory_slot_4.pack(side="left", padx=10, pady=10)
    inventory_slot_5.pack(side="left", padx=10, pady=10)

window = tk.Tk()

window.title("RPG Character by VRU")
window.geometry("900x600")
window.configure(bg="#1a1a1a")


title = tk.Label(
    window,
    text="⚔ RPG CHARACTER ⚔",
    font=("Cinzel", 24),
    bg="#1a1a1a",
    fg="white"
)
title.pack(pady=40)


welcome = tk.Label(
    window,
    text="Welcome, adventurer!",
    font=("Cinzel", 16),
    bg="#1a1a1a",
    fg="white"
)
welcome.pack(pady=10)


name_label = tk.Label(
    window,
    text="Character Name:",
    font=("Cinzel", 16),
    bg="#1a1a1a",
    fg="white"
)
name_label.pack_forget()


name_entry = tk.Entry(
    window,
    font=("Arial", 14)
)
name_entry.pack_forget()


character_name_label = tk.Label(
      window,
      text="",
      font=("Cinzel", 16),
      bg="#1a1a1a",
      fg="white"
)
character_name_label.pack_forget()


character_info_label = tk.Label(
    window,
    text=f"LEVEL: {player.level}    HP: {player.hp}    GOLD: {player.gold}",
    font=("Cinzel", 14),
    bg="#1a1a1a",
    fg="white"
)
character_info_label.pack_forget()


start_button = tk.Button(
        window,
        text="⚔ START GAME ⚔",
        command=start_game
)
start_button.pack(pady=20)


character_frame = tk.Frame(
     window,
     bg="#1a1a1a"
)
character_frame.pack_forget()


inventory_title = tk.Label(
     character_frame,
     text="INVENTORY",
     font=("Cinzel", 16),
     bg="#1a1a1a",
     fg="white"
)


inventory_slot_1 = tk.Label(
    character_frame,
    text=f"Slot 1 : {player.inventory[0].name}",
    font=("Cinzel", 14),
    bg="#1a1a1a",
    fg="white",
    relief="solid",
    bd=2,
    highlightbackground="white",
    highlightthickness=1,
    padx=10,
    pady=10
)


inventory_slot_2 = tk.Label(
     character_frame,
     text=f"Slot 2 : {player.inventory[1].name}",
     font= ("Cinzel", 14),
     bg="#1a1a1a",
     fg="white",
     relief="solid",
     bd=2,
     highlightbackground="white",
     highlightthickness=1,
     padx=10,
     pady=10
)
inventory_slot_2.pack_forget()

inventory_slot_3 = tk.Label(
     character_frame,
     text="[EMPTY]",
     font= ("Cinzel", 14),
     bg="#1a1a1a",
     fg="white",
     relief="solid",
     bd=2,
     highlightbackground="white",
     highlightthickness=1,
     padx=10,
     pady=10
)
inventory_slot_3.pack_forget()

inventory_slot_4 = tk.Label(
     character_frame,
     text="[ EMPTY]",
     font= ("Cinzel", 14),
     bg="#1a1a1a",
     fg="white",
     relief="solid",
     bd=2,
     highlightbackground="white",
     highlightthickness=1,
     padx=10,
     pady=10
)
inventory_slot_4.pack_forget()


inventory_slot_5 = tk.Label(
     character_frame,
     text="[ EMPTY]",
     font= ("Cinzel", 14),
     bg="#1a1a1a",
     fg="white",
     relief="solid",
     bd=2,
     highlightbackground="white",
     highlightthickness=1,
     padx=10,
     pady=10
)
inventory_slot_5.pack_forget()


create_button = tk.Button(
        window,
        text="⚔ CREATE CHARACTER ⚔",
        command=create_character
)
create_button.pack_forget()


top_bar = tk.Frame(
     window,
     bg="#1a1a1a"
)
top_bar.pack(fill="x")


bottom_bar = tk.Frame(
     window,
     bg="#1a1a1a"
)
bottom_bar.pack(side="bottom", fill="x")


exit_button = tk.Button(
    bottom_bar,
    text="⚔ EXIT ⚔",
    command=window.destroy,
    font=("Cinzel", 12)
)
exit_button.pack(pady=10)


window.mainloop()