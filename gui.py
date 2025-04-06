import tkinter as tk
from tkinter import filedialog, messagebox
import os
from compress import compress_file
from decompress import decompress_file

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def select_output():
    file_path = filedialog.asksaveasfilename(defaultextension=".mtc")
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def run_compress():
    input_path = input_entry.get()
    output_path = output_entry.get()

    if not os.path.isfile(input_path):
        messagebox.showerror("Error", "Please select a valid input file.")
        return

    compress_file(input_path, output_path)
    messagebox.showinfo("Done", f"File compressed to:\n{output_path}")

def run_decompress():
    input_path = input_entry.get()
    output_path = output_entry.get()

    if not os.path.isfile(input_path):
        messagebox.showerror("Error", "Please select a valid input file.")
        return

    decompress_file(input_path, output_path)
    messagebox.showinfo("Done", f"File decompressed to:\n{output_path}")

# GUI Setup
root = tk.Tk()
root.title("Multithreaded File Compressor")

tk.Label(root, text="Input File:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=5)

tk.Label(root, text="Output File:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10)
tk.Button(root, text="Save As", command=select_output).grid(row=1, column=2, padx=5)

tk.Button(root, text="Compress", command=run_compress, width=20).grid(row=2, column=0, columnspan=3, pady=10)
tk.Button(root, text="Decompress", command=run_decompress, width=20).grid(row=3, column=0, columnspan=3, pady=5)

root.mainloop()