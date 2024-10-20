import webbrowser
import tkinter as tk

# Define the links for each lesson
lessons = {
    "Trial": ['https://scratch.mit.edu/projects/812789044/', 'link2', 'https://scratch.mit.edu/projects/812789991/','link4'],
    1: ['link1', 'https://scratch.mit.edu/projects/805576673'],
    2: ['link2', 'https://scratch.mit.edu/projects/826186139'],
    # Add links for other lessons similarly
    # ...
}

def open_links(links):
    for link in links:
        webbrowser.open_new_tab(link)

def create_button(root, lesson_name, links):
    def callback():
        open_links(links)

    button = tk.Button(root, text=f"Lesson {lesson_name}", command=callback, background="Salmon")
    button.pack(ipadx=19,ipady = 6, pady=5)


# Create the main window
root = tk.Tk()
root.geometry("400x600")
root.title("2D Games with ROBLOX")

# Create buttons for each lesson
for lesson_name, links in lessons.items():
    create_button(root, lesson_name, links)

# Start the main loop
root.mainloop()
