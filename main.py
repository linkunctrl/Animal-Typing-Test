import customtkinter as ctk
import tkinter
from PIL import Image, ImageTk
import random
import time

start_time = None

paragraphs = [
    "The quick brown fox jumps over the lazy dog. It’s a phrase you’ve probably seen before, but did you ever stop to think about how weird it sounds? Still, it’s a great warm-up for your fingers.",
    "On rainy nights, the sound of water tapping the windows is oddly comforting. Some say it's the universe telling you to slow down and breathe. Others just put on headphones and type faster.",
    "Coffee is the programmer’s best friend. Not because it solves bugs, but because it keeps you awake while you solve them. Just don’t spill any on your keyboard, or you’ll have real problems.",
    "Typing is like casting spells with your fingers. The better you get, the more powerful your magic becomes. Eventually, you’ll summon full apps from thin air — or at least from a blinking cursor.",
    "A cat walks across your keyboard and accidentally opens Task Manager. Somehow, it types better than your friend. Maybe you should let the cat take the test and see if it gets a higher WPM."
]
rndm_para = random.choice(paragraphs)
start_time = time.time()

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create app window
app = ctk.CTk()
app.iconbitmap("assets/app_icon.ico")
app.title("Animal Typing Coach")
app.geometry("600x550")

# Load images
cat_img = ImageTk.PhotoImage(Image.open("assets/cat.png").resize((150, 150)))
dino_img = ImageTk.PhotoImage(Image.open("assets/dino.png").resize((150, 150)))
tiger_img = ImageTk.PhotoImage(Image.open("assets/tiger.png").resize((150, 150)))

# Current image
img_label = ctk.CTkLabel(app, image=cat_img, text="")
img_label.pack(pady=20)

# Text label for feedback
feedback = ctk.CTkLabel(app, text="Start typing and I’ll judge you :3", font=("Consolas", 16, "bold"))
feedback.pack(pady=10)

# Paragraph
para_label = ctk.CTkLabel(app, text=rndm_para, wraplength=500, justify="left", font=("Courier New", 16, "bold"), text_color="yellow")
para_label.pack(pady=10)

# Typing box
typing_box = ctk.CTkTextbox(app, width=450, height=180, font=("Consolas", 14))
typing_box.pack(pady=10)

# Enter Button
def button_function():
    global start_time
    typed_text = typing_box.get("1.0", "end").strip()
    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60
    word_count = len(typed_text.split())
    wpm = int(word_count / elapsed_time)
    mistakes = 0
    for typed_char, correct_char in zip(typed_text, rndm_para): #zip() makes sure it compares only up to the length of the shorter string, avoiding index errors.
        if typed_char != correct_char:
            mistakes += 1
    if wpm >= 60:
        img_label.configure(image=tiger_img)
        feedback.configure(text=f"Okay TryHard! 🐅\nWPM: {wpm} | Mistakes: {mistakes}")
        
    elif wpm >=35:
        img_label.configure(image=cat_img)
        feedback.configure(text=f"Decent-ish! 🐈\nWPM: {wpm} | Mistakes: {mistakes}")
        
    else:
        img_label.configure(image=dino_img)
        feedback.configure(text=f"Fossilized 🦕\nWPM: {wpm} | Mistakes: {mistakes}")
        
    typing_box.configure(state="disabled")
    print("button pressed")

def reset_test():
    global rndm_para, start_time
    rndm_para = random.choice(paragraphs)
    para_label.configure(text=rndm_para)
    typing_box.configure(state="normal")
    typing_box.delete("1.0", "end")
    img_label.configure(image=cat_img)
    feedback.configure(text="Start typing and I’ll judge you :3")
    start_time = time.time()


    
enter_btn = ctk.CTkButton(app, fg_color="black", text="Enter", command=button_function, font=("Consolas", 14, "bold"))
enter_btn.pack(pady=10)

reset_btn = ctk.CTkButton(app, text="Reset", fg_color="black", command=reset_test, font=("Consolas", 14, "italic" ))
reset_btn.pack(padx=20)


app.mainloop()
