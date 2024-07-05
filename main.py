import sys
sys.dont_write_bytecode = True

import tkinter as tk
from tkinter import scrolledtext

import os
from dotenv import load_dotenv

from llm import Robot


def _print_message(pronoun:str, message:str) -> bool:

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{pronoun}: {message}\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)


def send_user_message():
    message = entry.get()
    if message:
        
        _print_message("User", message)
        entry.delete(0, tk.END)

        ans = robot.run(message) # wip
        
        _print_message("Robot", ans)


def show_result():
    chatbot_frame.pack_forget()
    result_frame.pack(fill='both', expand=True)


def on_quit():
    robot.quit()
    root.destroy()


if __name__ == "__main__":

    # Set up the main application window
    root = tk.Tk()
    root.title("NEED NAME")

    # Bind the window close event to the custom function
    root.protocol("WM_DELETE_WINDOW", on_quit)

    # Create Solar LLM object
    load_dotenv()
    API_KEY = os.getenv('SECRET_KEY')
    robot = Robot(API_KEY)

    ################################################ Chatbot #####################################################

    chatbot_frame = tk.Frame(root)
    chatbot_frame.pack(fill='both', expand=True)

    image_path = "image/Card_1.png"  # Ensure this is a path to a GIF or PPM/PGM image
    original_image = tk.PhotoImage(file=image_path)

    # Create a label widget to display the image
    scaled_image = original_image.subsample(3, 3)
    image_label = tk.Label(chatbot_frame, image=scaled_image)
    image_label.pack(padx=10, pady=10)

    # Create a scrolled text widget for the chat window
    chat_window = scrolledtext.ScrolledText(chatbot_frame, wrap=tk.WORD, state=tk.DISABLED)
    chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create an entry widget for typing messages
    entry = tk.Entry(chatbot_frame, width=80)
    entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

    # Create a button for sending messages
    send_button = tk.Button(chatbot_frame, text="Send", command=send_user_message)
    send_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Bind key press events to the on_key_press function
    root.bind('<Return>', lambda ev: send_user_message())

    ################################################ Result #####################################################

    result_frame = tk.Frame(root)



    ################################################ Main Loop ##################################################

    

    # Start the main event loop
    root.mainloop()