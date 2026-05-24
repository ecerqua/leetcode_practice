import customtkinter as ctk
from customtkinter import CTkTextbox
from gemini_tutor import ai_tutor

# Inititalize the main window
root = ctk.CTk()
root.title("Gemini Leetcode Tutor")
root.geometry("740x1080")

# Add a label to the prompt
prompt_box_label = ctk.CTkLabel(root, text="Enter your question below:", font=("Arial", 18))
prompt_box_label.pack(pady=5)

prompt_box = CTkTextbox(root, width=550, height=300, font=("Arial", 16))
prompt_box.pack(pady=5, padx=5, fill=ctk.BOTH, expand=False)

def get_response():
    response = ai_tutor(prompt_box.get("1.0", ctk.END))
    answer_box.insert("1.0", response)

submit_button = ctk.CTkButton(root, text="Submit", command=get_response)
submit_button.pack(pady=5)

answer_box = CTkTextbox(root, width=550, height=300, font=("Arial", 16), )
answer_box.pack(pady=5, padx=5, fill=ctk.BOTH, expand=False)


root.mainloop()