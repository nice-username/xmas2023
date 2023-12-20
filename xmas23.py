import tkinter as tk
from pygame import mixer
import random
import sys
import os

# Function to get the correct path for the resource
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Initialize the mixer for playing MIDI
mixer.init()

# Function to play MIDI music
def play_music():
    mixer.music.load(resource_path('xmas.mid'))
    mixer.music.play()

# Function to update the image for slideshow
def update_image():
    global img_index
    img_index += 1
    if img_index > 3:
        img_index = 1
    img_path = resource_path(f'img{img_index}.png')
    photo = tk.PhotoImage(file=img_path)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference!
    window.after(4000 + random.randint(1000, 2000), update_image)

# Main window setup
window = tk.Tk()
window.title("lizMasonXmas2023")
window.geometry("1024x1024")

# Start with the first image in the slideshow
img_index = 1
photo = tk.PhotoImage(file=resource_path(f'img{img_index}.png'))
image_label = tk.Label(window, image=photo)
image_label.place(x=0, y=0)

# Create solid black box
black_box = tk.Frame(window, height=128, bg='black')
black_box.place(relx=0.5, rely=1.0, anchor='s', relwidth=1.0)

# Create a label for the message
message_label = tk.Label(black_box, text="Merry Christmas Liz & Mason!\n~ Joe", fg='white', bg='black', font=('Verdana', 36))
message_label.pack(expand=True)

# Start the music and slideshow
play_music()
window.after(4000 + random.randint(1000, 2000), update_image)

window.mainloop()
