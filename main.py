import sys
sys.dont_write_bytecode = True

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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

        ans = robot.run(message)
        
        _print_message("Robot", ans)

        _print_message("System", "==========================================")
        _print_message("Robot", "What does it look like?")




def start_test():
    age = age_entry
    gender = gender_var.get()
    country = country_var.get()

    # Create Solar LLM object
    global robot
    robot = Robot(age, gender, country)
    #robot.bind_tools([tool_req_more_info])

    profile_frame.pack_forget()
    chatbot_frame.pack(fill='both', expand=True)
    
    # Bind key press events to the on_key_press function
    root.bind('<Return>', lambda ev: send_user_message())

    _print_message("Robot", "What does it look like?")


def on_quit():
    root.destroy()



CUR_CARD_NUM = 1
MAX_CARD_NUM = 1

if __name__ == "__main__":

    # Set up the main application window
    root = tk.Tk()
    root.title("NEED NAME")

    # Bind the window close event to the custom function
    root.protocol("WM_DELETE_WINDOW", on_quit)

    ################################################ Profile #####################################################

    profile_frame = tk.Frame(root)
    profile_frame.pack(fill='both', expand=True)

    age_label = tk.Label(profile_frame, text="Age:")
    age_label.grid(row=0, column=0, padx=10, pady=10)
    age_entry = tk.Entry(profile_frame)
    age_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

    # Create and place the gender label and radio buttons
    gender_label = tk.Label(profile_frame, text="Gender:")
    gender_label.grid(row=1, column=0, padx=10, pady=10)
    gender_var = tk.StringVar(value="Male")
    gender_male = tk.Radiobutton(profile_frame, text="Male", variable=gender_var, value="Male")
    gender_male.grid(row=1, column=1, padx=10, pady=5, sticky='w')
    gender_female = tk.Radiobutton(profile_frame, text="Female", variable=gender_var, value="Female")
    gender_female.grid(row=1, column=2, padx=10, pady=5, sticky='w')
    gender_others = tk.Radiobutton(profile_frame, text="Others", variable=gender_var, value="Others")
    gender_others.grid(row=1, column=3, padx=10, pady=5, sticky='w')

    # Create and place the country label and entry
    country_label = tk.Label(profile_frame, text="Country:")
    country_label.grid(row=2, column=0, padx=10, pady=10)
    country_var = tk.StringVar()
    country_combobox = ttk.Combobox(profile_frame, textvariable=country_var)
    country_combobox['values'] = ("South Korea", "United State", "Canada", "Japan", "China", "Australia")
    country_combobox.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
    country_combobox.current(0)  # Set default value

    # Create and place the submit button
    submit_button = tk.Button(profile_frame, text="Submit", command=start_test)
    submit_button.grid(row=3, columnspan=4, pady=20)

    ################################################ Chatbot #####################################################

    chatbot_frame = tk.Frame(root)


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

    ################################################ Main Loop ##################################################

    # Start the main event loop
    root.mainloop()