import tkinter as tk
import random

# Dictionary with words and their corresponding clues
clues = {
    "secret": "Something kept hidden",
    "stage": "A raised platform",
    "table": "An item of furniture with a flat top",
    "order": "A request to make or supply goods",
    "action": "The fact or process of doing something",
    "revival": "A process of becoming popular or active again",
    "load": "An amount of something that is carried",
    "shatter": "To break suddenly into many small pieces",
    "addicted": "Physically or mentally dependent on a substance",
    "colorful": "Full of color or brightly colored",
    "hierarchy": "A system of ranking according to status or authority",
    "spectrum": "A band of colors, as seen in a rainbow",
    "threshold": "The point of beginning or entrance",
    "syndrome": "A group of symptoms that consistently occur together",
    "circumstances": "The conditions affecting a situation"
}

# Function to start the game
def start_game():
    global ran, guesses, turns
    guesses = ''
    difficulty = Difficulty.get()
    if difficulty == "Easy":
        words = ["secret", "stage", "table", "order", "action"]
    elif difficulty == "Medium":
        words = ["revival", "load", "shatter", "addicted", "colorful"]
    elif difficulty == "Hard":
        words = ["hierarchy", "spectrum", "threshold", "syndrome", "circumstances"]
    else:
        lbl_result.config(text="Please select a difficulty level")
        return

    ran = random.choice(words)
    turns = 10
    update_display()
    lbl_clue.config(text=f"Clue: {clues[ran]}")
    lbl_result.config(text="Game started! Good luck!")

    # Show the entry and guess button
    entry_guess.grid(column=0, row=7, columnspan=2)
    btn_guess.grid(column=2, row=7)

# Function to update the display
def update_display():
    display_word = ''.join([char if char in guesses else '_' for char in ran])
    lbl_word.config(text=display_word)
    lbl_turns.config(text=f"You have {turns} guesses left")

# Function to process the guess
def process_guess():
    global turns, guesses
    guess = entry_guess.get().lower()
    entry_guess.delete(0, tk.END)

    if guess in guesses:
        lbl_result.config(text="You already guessed that letter!")
        return

    guesses += guess
    if guess not in ran:
        turns -= 1

    update_display()

    if turns == 0:
        lbl_result.config(text=f"You Lose! The word was: {ran}")
    elif all(char in guesses for char in ran):
        lbl_result.config(text="You won!")

win = tk.Tk()
win.geometry("500x400")
win.title("Hangman")

Difficulty = tk.StringVar()
Difficulty.set(None)

# Widgets
lbl = tk.Label(win, text="Hangman", font=("Showcard Gothic", 15))
lbl2 = tk.Label(win, text="Difficulty (Easy, Medium, Hard)", font=("Sagoe UI Variable", 10))
lbl_word = tk.Label(win, text="", font=("Sagoe UI Variable", 20))
lbl_turns = tk.Label(win, text="", font=("Sagoe UI Variable", 10))
lbl_clue = tk.Label(win, text="", font=("Sagoe UI Variable", 10))
lbl_result = tk.Label(win, text="", font=("Sagoe UI Variable", 10))
entry_guess = tk.Entry(win, font=("Sagoe UI Variable", 10))
btn_guess = tk.Button(win, text="Guess", command=process_guess)
btn_start = tk.Button(win, text="Start Game", command=start_game)
Rad1 = tk.Radiobutton(win, text="Easy", value="Easy", variable=Difficulty)
Rad2 = tk.Radiobutton(win, text="Medium", value="Medium", variable=Difficulty)
Rad3 = tk.Radiobutton(win, text="Hard", value="Hard", variable=Difficulty)

# Placement
lbl.grid(column=0, row=0, columnspan=3, pady=10)
lbl2.grid(column=0, row=1, columnspan=3)
Rad1.grid(column=0, row=2, padx=50)
Rad2.grid(column=1, row=2, padx=50)
Rad3.grid(column=2, row=2, padx=50)
btn_start.grid(column=1, row=3, pady=10)
lbl_clue.grid(column=0, row=4, columnspan=3, pady=10)
lbl_word.grid(column=0, row=5, columnspan=3, pady=10)
lbl_turns.grid(column=0, row=6, columnspan=3, pady=10)
entry_guess.grid(column=0, row=7, columnspan=2)
btn_guess.grid(column=2, row=7)
lbl_result.grid(column=0, row=8, columnspan=3, pady=10)

# Initially hide the entry and guess button
entry_guess.grid_forget()
btn_guess.grid_forget()

win.mainloop()
