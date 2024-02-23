import tkinter as tk

def execute_python_code():
    code = code_entry.get("1.0", tk.END)  # Retrieve Python code from the text field
    try:
        exec(code)  # Execute Python code
    except Exception as e:
        result_text.config(text=f"Error: {e}")

# Create GUI
root = tk.Tk()
root.title("Python Executor")

# Text field for Python code
code_entry = tk.Text(root, height=10, width=40)
code_entry.pack(pady=10)

# Button to execute the code
execute_button = tk.Button(root, text="Execute", command=execute_python_code)
execute_button.pack(pady=10)

# Display for the result or error
result_text = tk.Label(root, text="")
result_text.pack(pady=10)

# Start GUI
root.mainloop()
