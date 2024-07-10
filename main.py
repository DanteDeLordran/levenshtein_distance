from tkinter import messagebox
import tkinter as tk


def levenshtein_distance(_first: str, _last: str):
    first_len = len(_first) + 1
    last_len = len(_last) + 1

    matrix = [[0 for _ in range(last_len)] for _ in range(first_len)]

    for i in range(first_len):
        matrix[i][0] = i

    for i in range(last_len):
        matrix[0][i] = i

    for i in range(1, first_len):
        for j in range(1, last_len):
            cost = 0 if _first[i - 1] == _last[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    return matrix[first_len - 1][last_len - 1]


def binary_to_text(binary_string: str) -> str:
    binary_string.replace(" ", "")
    return ''.join(chr(int(binary_string[i * 8:i * 8 + 8], 2)) for i in range(len(binary_string) // 8))


def calculate_distance(first_word, last_word):
    if first_word.isalpha() and last_word.isalpha():
        messagebox.showinfo("Result", f"The Levenshtein distance is: {levenshtein_distance(first_word, last_word)}")
    else:
        messagebox.showerror('Only letters', 'Binary must be a text!')


def check_binary():
    _entry_first = entry_first.get()
    _entry_last = entry_last.get()

    if not all(c in '01' for c in _entry_first) or not all(c in '01' for c in _entry_last) or not len(_entry_first) % 8 == 0 or not len(_entry_last) % 8 == 0:
        messagebox.showerror('Invalid input', 'Please enter valid binary words')
    else:
        first_word = binary_to_text(_entry_first)
        last_word = binary_to_text(_entry_last)
        if first_word and last_word:
            calculate_distance(first_word, last_word)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Levenshtein Distance Calculator")
    root.resizable(False, False)

    label_first = tk.Label(root, text="Enter the first word:")
    entry_first = tk.Entry(root)
    label_last = tk.Label(root, text="Enter the second word:")
    entry_last = tk.Entry(root)

    calculate_button = tk.Button(root, text="Calculate", command=check_binary)

    label_first.grid(row=0, column=0, padx=10, pady=5)
    entry_first.grid(row=0, column=1, padx=10, pady=5)
    label_last.grid(row=1, column=0, padx=10, pady=5)
    entry_last.grid(row=1, column=1, padx=10, pady=5)
    calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
