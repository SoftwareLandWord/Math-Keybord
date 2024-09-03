import tkinter as tk

class MathChemKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Math & Chemistry Keyboard")
        
        self.root.configure(bg="black")

        self.text_entry = tk.Entry(root, width=80, bg="black", fg="white")
        self.text_entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('⁰', 1, 1), ('¹', 1, 2), ('²', 1, 3),
            ('³', 2, 1), ('⁴', 2, 2), ('⁵', 2, 3),
            ('⁶', 3, 1), ('⁷', 3, 2), ('⁸', 3, 3), ('₀', 4, 1),
            ('⁹', 1, 4), ('¹⁰', 2, 4), ('⁻', 3, 4), ('⁺', 4, 4),
            ('(', 4, 2), (')', 4, 3), ('ⁿ', 1, 5), ('√', 2, 5),
            ('H₂O', 3, 5), ('CO₂', 4, 5),
            ('₂', 5, 1), ('₃', 5, 2), ('₄', 5, 3),
            ('₅', 6, 1), ('₆', 6, 2), ('₇', 6, 3),
            ('₈', 7, 1), ('₉', 7, 2), ('₊', 7, 3), ('₋', 2, 6),
            ('₁', 8, 1),
        ]
        buttons.sort(key=lambda x: x[0])
        row, column = 1, 1
        for idx, (text, _, _) in enumerate(buttons):
            if idx % 6 == 0 and idx != 0:  # 6 buttons per row
                row += 1
                column = 1
            button = tk.Button(self.root, text=text, width=10, height=3, bg="white", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)
            column += 1

    def on_button_click(self, char):
        current_text = self.text_entry.get()
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(tk.END, current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathChemKeyboard(root)
    root.mainloop()