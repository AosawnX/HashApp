import tkinter as tk
from tkinter import filedialog, messagebox
from hasher import hash_text, hash_file
from utils import validate_file, get_file_type

def hash_input():
    input_type = input_type_var.get()
    if input_type == "Text":
        text = text_input.get("1.0",tk.END).strip()
        if not text:
            messagebox.showerror("Uh Oh!","Text input cannot be empty")
            return
        hashed_value = hash_text(text)
    else:
        file_path = file_path_entry.get()
        if not validate_file(file_path):
            messagebox.showerror("Uh Oh!","Invalid file or file exceeds size limit.")
            return
        file_type = get_file_type(file_path)
        if input_type == "Image" and file_type!= "image":
            messagebox.showerror("Uh Oh!", "Selected file is not an image")
            return
        elif input_type == "Video" and file_type != "video":
            messagebox.showerror("Uh Oh!", "Selected file is not a video!")
            return
        hashed_value = hash_file(file_path)

    result_text.set(f"Hash: {hashed_value}")


def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_entry.delete(0,tk.END)
        file_path_entry.insert(0,file_path)


root = tk.Tk()
root.title("HashApp by AosawnX")


input_type_var = tk.StringVar(value="Text")
tk.Radiobutton(root, text="Text", variable=input_type_var, value="Text").pack()
tk.Radiobutton(root, text="Image", variable=input_type_var, value="Image").pack()
tk.Radiobutton(root, text="Video", variable=input_type_var, value="Video").pack()

tk.Label(root, text="Enter Text:").pack(pady=5)
text_input = tk.Text(root, height=5, width=40)
text_input.pack()


tk.Label(root, text="Or Select File:").pack(pady=5)
file_path_entry = tk.Entry(root, width=40)
file_path_entry.pack()
tk.Button(root, text="Browse", command=browse_file).pack(pady=5)

tk.Button(root, text="Generate Hash", command=hash_input).pack(pady=10)


result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, wraplength=400, fg="blue").pack(pady=10)

root.mainloop()