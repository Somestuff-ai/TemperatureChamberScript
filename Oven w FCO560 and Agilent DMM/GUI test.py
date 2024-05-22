import customtkinter

# Set the appearance mode and theme
customtkinter.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Create the main window
root = customtkinter.CTk()

# Set the title and geometry of the window
root.title("CustomTkinter Example")
root.geometry("400x300")

# Create a label
label = customtkinter.CTkLabel(root, text="Hello, CustomTkinter!")
label.pack(pady=20)

# Create a button
button = customtkinter.CTkButton(root, text="Click Me", command=lambda: print("Button clicked!"))
button.pack(pady=10)

# Create an entry field
entry = customtkinter.CTkEntry(root, placeholder_text="Enter something")
entry.pack(pady=10)

# Run the main event loop
root.mainloop()