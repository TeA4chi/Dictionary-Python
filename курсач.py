import tkinter as tk
from tkinter import messagebox
import json #легше читати, добре робить з пайтон, підтримка unicode
import os

# Глобальний словник для зберігання слів
dictionary = {}
FILE_NAME = "dictionary.json"

#завантаження слова з файлу
def load_dictionary():
    global dictionary
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            dictionary = json.load(f) #загрузка файлу

#збереження слова у файл
def save_dictionary():
    with open(FILE_NAME, 'w', encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4) #f-файловий об'єкт(вище), ensure щоб уникнути юнікоду(коли укр сим. робл. типу \u043f)



def add_word_window():
    add_window = tk.Toplevel(window)
    add_window.title("Додати слово")
    add_window.geometry("1000x800")
    add_window.config(bg='#E0DFA6')

    # Рядок для англійського слова
    tk.Label(add_window, text="Англійською", font=("Arial", 18), bg='#E0DFA6').pack(pady=10)
    english_entry = tk.Entry(add_window, font=("Arial", 18))
    english_entry.pack()

    # Рядок для українського слова
    tk.Label(add_window, text="Українською:", font=("Arial", 18), bg="#E0DFA6").pack(pady=10)
    ukraine_entry = tk.Entry(add_window, font=("Arial", 18))
    ukraine_entry.pack()

    def save_word():
        english = english_entry.get().strip().lower() #.get-отримання, .strip-видалення пустих символів і пробілів, .lower-нижній регістр
        ukraine = ukraine_entry.get().strip().lower() #.get-отримання, .strip-видалення пустих символів і пробілів, .lower-нижній регістр
        if english and ukraine:
            dictionary[ukraine] = english
            save_dictionary() #save в словник
            messagebox.showinfo("Успіх", "Слово успішно додане")
            english_entry.delete(0, tk.END) #очистка рядка після введення слова
            ukraine_entry.delete(0, tk.END) #очистка рядка після введення слова
        else:
            messagebox.showerror("Помилка", "Заповніть два поля")

    # Кнопка "Зберегти"
    save_button = tk.Button(add_window, text="Зберегти", command=save_word, width=16, height=3, bg="#4CAF50", fg="white", font=("Arial", 14))
    save_button.pack(pady=20)

    # Кнопка "Назад"
    back_button = tk.Button(add_window, text="Назад", command=add_window.destroy, width=16, height=3, bg="#f44336", fg="white", font=("Arial", 14))
    back_button.pack()

def window_find_word():
    find_window = tk.Toplevel(window)
    find_window.title("Знайти слово")
    find_window.geometry("1000x800")
    find_window.config(bg="#E0DFA6")

    # Рядок для пошуку слова
    tk.Label(find_window, text="Для пошуку введіть слово українською", font=("Arial", 18), bg="#E0DFA6").pack(pady=10)
    word_entry = tk.Entry(find_window, font=("Arial", 18))
    word_entry.pack()

    # Рядок для виведення результату
    result_label = tk.Label(find_window, text="", font=("Arial", 18), bg="#E0DFA6")
    result_label.pack(pady=20)

    def search_word():
        word = word_entry.get().strip().lower() #.get-отримання, .strip-видалення пустих символів і пробілів, .lower-нижній регістр
        if word in dictionary:
            result_label.config(text=f"Англійською: {dictionary[word]}")
        else:
            result_label.config(text="Слово не знайдено")

    # Кнопка "Знайти"
    search_button = tk.Button(find_window, text="Знайти", command=search_word, width=17, height=3, bg="#ff0000", fg="white", font=("Arial", 14))
    search_button.pack(pady=10)

    # Кнопка "Назад"
    back_button = tk.Button(find_window, text="Назад", command=find_window.destroy, width=17, height=3, bg="#ff0000", fg="white", font=("Arial", 14))
    back_button.pack()

# Головне вікно
window = tk.Tk()
window.title('Словник')
window.minsize(1000, 800)
window.config(bg="#E0DFA6")

#завантаження файлу з словника коли програма запускається
load_dictionary()

# Заголовок
tk.Label(window, text="Словник", font=("Arial", 40), bg="#E0DFA6", fg="#000000").place(relx=0.5, rely=0.2, anchor='center')

# Кнопка "Додати слово"
tk.Button(window, text="Додати слово", width=22, height=6, command=add_word_window, bg="#ff0000", fg="white", font=("Arial", 14)).place(relx=0.3, rely=0.6, anchor='center')

# Кнопка "Знайти слово"
tk.Button(window, text="Знайти слово", width=22, height=6, command=window_find_word, bg="#ff0000", fg="white", font=("Arial", 14)).place(relx=0.7, rely=0.6, anchor='center')

tk.mainloop()