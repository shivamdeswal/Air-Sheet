import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def run_program1():
    try:
        subprocess.run([sys.executable, 'airSheet\\drawShapes.py'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run the program: {e}")

def run_program2():
    try:
        subprocess.run([sys.executable, 'airSheet\\drawColors.py'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run the program: {e}")

def run_program3():
    try:
        subprocess.run([sys.executable, 'game.py'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run the program: {e}")

def main():
    global root
    root = tk.Tk()
    root.title("Choose a Program")
    root.geometry("800x600")

    frame = tk.Frame(root, bg='white')
    frame.pack(fill=tk.BOTH, expand=True)

    logo_image = Image.open("logo.png")
    logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(frame, image=logo_photo, bg='white')
    logo_label.image = logo_photo  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=20)
    
    func_label = tk.Label(frame, text="Welcome To Air Sheet", font=("Helvetica", 16), bg='white')
    func_label.pack(pady=10, anchor=tk.N)
    
    button_frame = tk.Frame(frame, bg='white')
    button_frame.pack(pady=10)

    def create_button(parent, command, text):
        button = tk.Button(parent, command=command, text=text, compound="center", font=("Helvetica", 16), bg="grey", width=25, height=3)
        return button
    
    btn1 = create_button(button_frame, run_program1, "Drawing shapes and tools")
    btn1.grid(row=0, column=0, pady=5)
    
    btn2 = create_button(button_frame, run_program2, "Drawing with different colors")
    btn2.grid(row=1, column=0, pady=5)
    
    btn3 = create_button(button_frame, run_program3, "Flappy Bird Game")
    btn3.grid(row=2, column=0, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
