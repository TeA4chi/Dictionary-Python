import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

dictionary = {}
FILE_NAME = "dictionary.json"

def load_dictionary():
    global dictionary
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            dictionary = json.load(f)

def save_dictionary():
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)

def add_word_window():
    add_window = tk.Toplevel(window)
    add_window.title("Додати слово")
    add_window.geometry("1000x800")
    add_window.config(bg='#E0DFA6')

    tk.Label(add_window, text="Англійською", font=("Arial", 18), bg='#E0DFA6').pack(pady=10)
    english_entry = tk.Entry(add_window, font=("Arial", 18))
    english_entry.pack()

    tk.Label(add_window, text="Українською:", font=("Arial", 18), bg="#E0DFA6").pack(pady=10)
    ukraine_entry = tk.Entry(add_window, font=("Arial", 18))
    ukraine_entry.pack()

    def save_word():
        english = english_entry.get().strip().lower()
        ukraine = ukraine_entry.get().strip().lower()
        if english and ukraine:
            dictionary[ukraine] = english
            save_dictionary()
            messagebox.showinfo("Успіх", "Слово успішно додане")
            english_entry.delete(0, tk.END)
            ukraine_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Помилка", "Заповніть два поля")

    tk.Button(add_window, text="Зберегти", command=save_word, width=16, height=3, bg="#4CAF50", fg="white", font=("Arial", 14)).pack(pady=20)
    tk.Button(add_window, text="Назад", command=add_window.destroy, width=16, height=3, bg="#f44336", fg="white", font=("Arial", 14)).pack()

def window_find_word():
    find_window = tk.Toplevel(window)
    find_window.title("Знайти слово")
    find_window.geometry("1000x800")
    find_window.config(bg="#E0DFA6")

    tk.Label(find_window, text="Для пошуку введіть слово українською", font=("Arial", 18), bg="#E0DFA6").pack(pady=10)
    word_entry = tk.Entry(find_window, font=("Arial", 18))
    word_entry.pack()

    result_label = tk.Label(find_window, text="", font=("Arial", 18), bg="#E0DFA6")
    result_label.pack(pady=20)

    def search_word():
        word = word_entry.get().strip().lower()
        if word in dictionary:
            result_label.config(text=f"Англійською: {dictionary[word]}")
        else:
            result_label.config(text="Слово не знайдено")

    tk.Button(find_window, text="Знайти", command=search_word, width=17, height=3, bg="#ff0000", fg="white", font=("Arial", 14)).pack(pady=10)
    tk.Button(find_window, text="Назад", command=find_window.destroy, width=17, height=3, bg="#ff0000", fg="white", font=("Arial", 14)).pack()

def edit_word_window():
    edit_window = tk.Toplevel(window)
    edit_window.title("Редагувати слово")
    edit_window.geometry("1000x800")
    edit_window.config(bg="#E0DFA6")

    tk.Label(edit_window, text="Список слів (українською)", font=("Arial", 18), bg="#E0DFA6").pack(pady=10)

    listbox = tk.Listbox(edit_window, font=("Arial", 16), width=40, height=15)
    listbox.pack(pady=10)

    for ukr_words in dictionary:
        listbox.insert(tk.END, ukr_words)

    def edit_selected():
        selected = listbox.curselection()
        if not selected:
            messagebox.showwarning("Увага", "Виберіть слово для редагування")
            return

        index = selected[0]
        old_ukr = listbox.get(index)
        old_eng = dictionary[old_ukr]

        new_ukr = simpledialog.askstring("Редагувати українське слово", "Нове українське слово:", initialvalue=old_ukr)
        if not new_ukr:
            return

        new_eng = simpledialog.askstring("Редагувати англійське слово", "Нове англійське слово:", initialvalue=old_eng)
        if not new_eng:
            return

        del dictionary[old_ukr]
        dictionary[new_ukr.strip().lower()] = new_eng.strip().lower()
        save_dictionary()

        listbox.delete(index)
        listbox.insert(index, new_ukr.strip().lower())
        messagebox.showinfo("Успіх", "Слово відредаговано")

    tk.Button(edit_window, text="Редагувати вибране слово", command=edit_selected,
              width=25, height=2, bg="#4CAF50", fg="white", font=("Arial", 14)).pack(pady=10)

    tk.Button(edit_window, text="Назад", command=edit_window.destroy,
              width=25, height=2, bg="#f44336", fg="white", font=("Arial", 14)).pack()

# Головне вікно
window = tk.Tk()
window.title('Словник')
window.minsize(1000, 800)
window.config(bg="#E0DFA6")

load_dictionary()

tk.Label(window, text="Словник", font=("Arial", 40), bg="#E0DFA6", fg="#000000").place(relx=0.5, rely=0.2, anchor='center')

tk.Button(window, text="Додати слово", width=22, height=6, command=add_word_window,
          bg="#ff0000", fg="white", font=("Arial", 14)).place(relx=0.3, rely=0.6, anchor='center')

tk.Button(window, text="Знайти слово", width=22, height=6, command=window_find_word,
          bg="#ff0000", fg="white", font=("Arial", 14)).place(relx=0.7, rely=0.6, anchor='center')

tk.Button(window, text="Редагувати слово", width=22, height=6, command=edit_word_window,
          bg="#ff0000", fg="white", font=("Arial", 14)).place(relx=0.5, rely=0.8, anchor='center')

tk.mainloop()
