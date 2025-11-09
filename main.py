import tkinter as tk
from PIL import Image, ImageTk
import random
import os

root = tk.Tk()
root.title("🔥 STONE PAPER SCISSORS 🔥")
root.attributes("-fullscreen", True)
root.configure(bg="black")

bg_path = r"C:\Users\91620\Desktop\Python\STONE-PAPER\bg.png"

if not os.path.exists(bg_path):
    print("❌ Background image not found:", bg_path)
    root.destroy()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

bg_image = Image.open(bg_path)
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

choices = ["STONE", "PAPER", "SCISSOR"]
user_score = 0
comp_score = 0
draw_score = 0

start_frame = tk.Frame(root, bg="black")
game_frame = tk.Frame(root, bg="black")

def show_bg(frame):
    bg = tk.Label(frame, image=bg_photo)
    bg.place(x=0, y=0, relwidth=1, relheight=1)

def start_game():
    start_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    show_bg(game_frame)
    show_game_screen()

def exit_game():
    root.destroy()

def play(user_choice):
    global user_score, comp_score, draw_score
    comp_choice = random.choice(choices)

    player_choice_label.config(text=f"🧍 You: {user_choice}", fg="#00FFFF")
    computer_choice_label.config(text=f"💻 Computer: {comp_choice}", fg="#00FFFF")

    if user_choice == comp_choice:
        result = "It's a Draw 🤝"
        color = "#00FFFF"
        draw_score += 1
    elif (user_choice == "STONE" and comp_choice == "SCISSOR") or \
         (user_choice == "PAPER" and comp_choice == "STONE") or \
         (user_choice == "SCISSOR" and comp_choice == "PAPER"):
        result = "You Win 🎉"
        color = "#39FF14"
        user_score += 1
    else:
        result = "You Lose 💀"
        color = "#FF3131"
        comp_score += 1

    result_label.config(text=result, fg=color)
    score_label.config(
        text=f"🏆 Score — You: {user_score} | Computer: {comp_score} | Draws: {draw_score}"
    )

def restart_game():
    global user_score, comp_score, draw_score
    user_score = comp_score = draw_score = 0
    result_label.config(text="Make your move!", fg="#39FF14")
    player_choice_label.config(text="")
    computer_choice_label.config(text="")
    score_label.config(text="🏆 Score — You: 0 | Computer: 0 | Draws: 0")

show_bg(start_frame)

title_label = tk.Label(start_frame, text="🔥 STONE  PAPER  SCISSORS 🔥",
                       font=("Consolas", 50, "bold"),
                       bg="black", fg="#00FFFF")
title_label.pack(pady=200)

def animate_title():
    colors = ["#39FF14", "#00FFFF", "#FF00FF"]
    color = random.choice(colors)
    title_label.config(fg=color)
    root.after(300, animate_title)
animate_title()

play_btn = tk.Button(start_frame, text="▶ PLAY GAME", command=start_game,
                     font=("Consolas", 28, "bold"),
                     bg="#00FFFF", fg="black",
                     activebackground="#39FF14", activeforeground="black",
                     width=15, height=1, relief="flat", cursor="hand2")
play_btn.pack(pady=40)

exit_btn = tk.Button(start_frame, text="❌ EXIT", command=exit_game,
                     font=("Consolas", 20, "bold"),
                     bg="#FF3131", fg="white",
                     width=10, height=1, relief="flat", cursor="hand2")
exit_btn.pack()

start_frame.pack(fill="both", expand=True)

def show_game_screen():
    title = tk.Label(game_frame, text="🔥 STONE  PAPER  SCISSORS 🔥",
                     font=("Consolas", 40, "bold"),
                     bg="black", fg="#00FFFF")
    title.pack(pady=40)

    global player_choice_label, computer_choice_label, result_label, score_label

    player_choice_label = tk.Label(game_frame, text="", font=("Consolas", 24, "bold"),
                                   bg="black", fg="#00FFFF", pady=10)
    player_choice_label.pack()

    computer_choice_label = tk.Label(game_frame, text="", font=("Consolas", 24, "bold"),
                                     bg="black", fg="#00FFFF", pady=10)
    computer_choice_label.pack()

    frame = tk.Frame(game_frame, bg="black")
    frame.pack(pady=30)

    def on_enter(e): e.widget.config(bg="#00FFFF", fg="black")
    def on_leave(e): e.widget.config(bg="#111", fg="#00FFFF")

    button_style = {
        "font": ("Consolas", 24, "bold"),
        "width": 10,
        "height": 2,
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2",
        "bg": "#111",
        "fg": "#00FFFF",
        "activebackground": "#00FFFF",
        "activeforeground": "black"
    }

    for text in ["STONE", "PAPER", "SCISSOR"]:
        btn = tk.Button(frame, text=text, command=lambda t=text: play(t), **button_style)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(side="left", padx=30)

    result_label = tk.Label(game_frame, text="Make your move!",
                            font=("Consolas", 28, "bold"),
                            bg="black", fg="#39FF14", pady=20)
    result_label.pack(pady=20)

    score_label = tk.Label(game_frame, text="🏆 Score — You: 0 | Computer: 0 | Draws: 0",
                           font=("Consolas", 22, "bold"),
                           bg="black", fg="#00FFFF")
    score_label.pack(pady=10)

    control_frame = tk.Frame(game_frame, bg="black")
    control_frame.pack(pady=30)

    restart_btn = tk.Button(control_frame, text="🔁 RESTART", command=restart_game,
                            font=("Consolas", 20, "bold"), bg="#222", fg="#39FF14",
                            width=10, height=1, cursor="hand2", relief="flat")
    restart_btn.grid(row=0, column=0, padx=20)

    exit_btn = tk.Button(control_frame, text="❌ EXIT", command=exit_game,
                         font=("Consolas", 20, "bold"), bg="#FF3131", fg="white",
                         width=10, height=1, cursor="hand2", relief="flat")
    exit_btn.grid(row=0, column=2, padx=20)

root.mainloop()
