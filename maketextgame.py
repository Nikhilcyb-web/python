import tkinter as tk

window = tk.Tk()
window.title("My Adventure Game")
window.configure(bg="#1a1a2e")

title = tk.Label(window, text="The Dark Forest", bg="#1a1a2e", fg="#e94560", font=("Arial", 20, "bold"))
title.pack(pady=10)

text_box = tk.Text(window, width=50, height=10, bg="#16213e", fg="#e0e0e0", font=("Arial", 12), relief="flat", padx=10, pady=10)
text_box.pack(pady=10)

text_box.insert("end", "You wake up in a dark forest.\nWhat do you do?")

def go_forest():
    text_box.delete("1.0", "end")
    text_box.insert("end", "You walk deeper into the forest.\nYou find a mysterious cave!")
    button1.config(text="Enter the cave", command=enter_cave)
    button2.config(text="Go back", command=restart)

def climb_tree():
    text_box.delete("1.0", "end")
    text_box.insert("end", "You climb high up.\nYou can see a village in the distance!")

def enter_cave():
    text_box.delete("1.0", "end")
    text_box.insert("end", "You enter the cave and find a huge treasure!\nYou WIN! Congratulations!")
    button1.config(text="Play Again", command=restart)
    button2.config(text="", state="disabled")

def restart():
    text_box.delete("1.0", "end")
    text_box.insert("end", "You wake up in a dark forest.\nWhat do you do?")
    button1.config(text="Go deeper into the forest", command=go_forest, state="normal")
    button2.config(text="Climb a tree to look around", command=climb_tree, state="normal")

button1 = tk.Button(window, text="Go deeper into the forest", width=30, command=go_forest, bg="#e94560", fg="white", font=("Arial", 11), relief="flat", cursor="hand2")
button1.pack(pady=5)

button2 = tk.Button(window, text="Go deeper into the forest", width=30, command=go_forest, bg="#e94560", fg="white", font=("Arial", 11), relief="flat", cursor="hand2")
button2.pack(pady=5)

window.mainloop()