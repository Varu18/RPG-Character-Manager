import tkinter as tk

def start_game():
        welcome.pack_forget()
        start_button.pack_forget()
        name_label.pack()
        name_entry.pack()
        name_entry.pack()
        create_button.pack(pady=30)


def create_character():
    name = name_entry.get()
    print("Character name:", name)

    name_entry.config(state="disabled")
    create_button.config(state="disabled")
    

window = tk.Tk()

window.title("RPG Character by VRU")
window.geometry("600x400")
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


start_button = tk.Button(
        window,
        text="⚔ START GAME ⚔",
        command=start_game
)
start_button.pack(pady=20)


create_button = tk.Button(
        window,
        text="⚔ CREATE CHARACTER ⚔",
        command=create_character
)
create_button.pack_forget()


window.mainloop()