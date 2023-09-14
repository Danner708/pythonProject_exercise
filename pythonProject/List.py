import tkinter as tk


def create_app():
    app.title("Jegyzettömb alkalmazás")
    app.geometry("600x400")
    global text_widget
    text_widget = tk.Text(app, wrap=tk.WORD)
    text_widget.pack(expand=True, fill="both")


def new_note():
    text_widget.delete("1.0", tk.END)


def save_note():
    note = text_widget.get("1.0", tk.END)
    with open("jegyzet.txt", "w") as file:
        file.write(note)


def load_note():
    try:
        with open("jegyzet.txt", "r") as file:
            note = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, note)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    app = tk.Tk()
    create_app()

    new_button = tk.Button(app, text="Új", command=new_note)
    save_button = tk.Button(app, text="Mentés", command=save_note)
    load_button = tk.Button(app, text="Betöltés", command=load_note)

    new_button.pack()
    save_button.pack()
    load_button.pack()

    menu_bar = tk.Menu(app)
    app.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Fájl", menu=file_menu)
    file_menu.add_command(label="Új", command=new_note)
    file_menu.add_command(label="Mentés", command=save_note)
    file_menu.add_command(label="Betöltés", command=load_note)
    file_menu.add_separator()
    file_menu.add_command(label="Kilépés", command=app.quit)

    app.mainloop()
