import tkinter as tk
from tkinter import ttk


class Windows11Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("800x1200")
        self.root.minsize(280, 400)

        # Colors
        self.bg_color = "#202020"
        self.number_btn_color = "#3b3b3b"
        self.function_btn_color = "#323232"
        self.equals_btn_color = "#76b9ed"
        self.text_color = "#ffffff"
        self.dimmed_text_color = "#858585"

        self.root.configure(bg=self.bg_color)

        # Configure styles
        self.setup_styles()

        # Build UI
        self.create_header()
        self.create_display()
        self.create_memory_row()
        self.create_button_grid()

        # Configure grid weights for responsiveness
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=0)  # Header - fixed
        self.root.grid_rowconfigure(1, weight=0)  # Display - fixed
        self.root.grid_rowconfigure(2, weight=0)  # Memory row - fixed
        self.root.grid_rowconfigure(3, weight=1)  # Button grid - expandable

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Configure button styles
        self.style.configure(
            "Number.TButton",
            background=self.number_btn_color,
            foreground=self.text_color,
            font=("Segoe UI", 14),
            borderwidth=0,
            focuscolor=self.number_btn_color,
            padding=(10, 15),
        )
        self.style.map(
            "Number.TButton",
            background=[("active", "#4a4a4a"), ("pressed", "#555555")],
            foreground=[("active", self.text_color)],
        )

        self.style.configure(
            "Function.TButton",
            background=self.function_btn_color,
            foreground=self.text_color,
            font=("Segoe UI", 13),
            borderwidth=0,
            focuscolor=self.function_btn_color,
            padding=(10, 15),
        )
        self.style.map(
            "Function.TButton",
            background=[("active", "#424242"), ("pressed", "#4a4a4a")],
            foreground=[("active", self.text_color)],
        )

        self.style.configure(
            "Equals.TButton",
            background=self.equals_btn_color,
            foreground="#000000",
            font=("Segoe UI", 16, "bold"),
            borderwidth=0,
            focuscolor=self.equals_btn_color,
            padding=(10, 15),
        )
        self.style.map(
            "Equals.TButton",
            background=[("active", "#8ec9f7"), ("pressed", "#5aa9dd")],
            foreground=[("active", "#000000")],
        )

    def create_header(self):
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        header_frame.grid_columnconfigure(1, weight=1)

        # Hamburger menu
        hamburger = tk.Label(
            header_frame,
            text="☰",
            font=("Segoe UI", 14),
            fg=self.text_color,
            bg=self.bg_color,
            cursor="hand2",
        )
        hamburger.grid(row=0, column=0, padx=(0, 10))

        # "Standard" text
        title = tk.Label(
            header_frame,
            text="Standard",
            font=("Segoe UI", 16, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
        )
        title.grid(row=0, column=1, sticky="w")

        # Right icons frame
        icons_frame = tk.Frame(header_frame, bg=self.bg_color)
        icons_frame.grid(row=0, column=2, sticky="e")

        # Keep on top icon (pin)
        pin_icon = tk.Label(
            icons_frame,
            text="📌",
            font=("Segoe UI", 11),
            fg=self.dimmed_text_color,
            bg=self.bg_color,
            cursor="hand2",
        )
        pin_icon.pack(side="left", padx=5)

        # History icon
        history_icon = tk.Label(
            icons_frame,
            text="🕐",
            font=("Segoe UI", 11),
            fg=self.dimmed_text_color,
            bg=self.bg_color,
            cursor="hand2",
        )
        history_icon.pack(side="left", padx=5)

    def create_display(self):
        display_frame = tk.Frame(self.root, bg=self.bg_color, height=140)
        display_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 15))
        display_frame.grid_columnconfigure(0, weight=1)
        display_frame.grid_rowconfigure(0, weight=1)
        display_frame.grid_propagate(False)

        # Display number
        display_label = tk.Label(
            display_frame,
            text="0",
            font=("Segoe UI", 48, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
            anchor="se",
        )
        display_label.grid(row=0, column=0, sticky="se", padx=5, pady=5)

    def create_memory_row(self):
        memory_frame = tk.Frame(self.root, bg=self.bg_color)
        memory_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 5))

        memory_buttons = ["MC", "MR", "M+", "M-", "MS", "M▾"]

        for i, text in enumerate(memory_buttons):
            memory_frame.grid_columnconfigure(i, weight=1)
            label = tk.Label(
                memory_frame,
                text=text,
                font=("Segoe UI", 10),
                fg=self.dimmed_text_color,
                bg=self.bg_color,
                cursor="hand2",
            )
            label.grid(row=0, column=i, sticky="ew")

    def create_button_grid(self):
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.grid(row=3, column=0, sticky="nsew", padx=3, pady=3)

        # Configure grid weights for responsiveness
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1, uniform="btn")
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1, uniform="btn")

        # Button definitions: (text, style)
        buttons = [
            # Row 1
            ("%", "Function"),
            ("CE", "Function"),
            ("C", "Function"),
            ("⌫", "Function"),
            # Row 2
            ("¹/ₓ", "Function"),
            ("x²", "Function"),
            ("²√x", "Function"),
            ("÷", "Function"),
            # Row 3
            ("7", "Number"),
            ("8", "Number"),
            ("9", "Number"),
            ("×", "Function"),
            # Row 4
            ("4", "Number"),
            ("5", "Number"),
            ("6", "Number"),
            ("−", "Function"),
            # Row 5
            ("1", "Number"),
            ("2", "Number"),
            ("3", "Number"),
            ("+", "Function"),
            # Row 6
            ("⁺/₋", "Number"),
            ("0", "Number"),
            (".", "Number"),
            ("=", "Equals"),
        ]

        for idx, (text, style) in enumerate(buttons):
            row = idx // 4
            col = idx % 4

            btn = ttk.Button(button_frame, text=text, style=f"{style}.TButton")
            btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)


def main():
    root = tk.Tk()
    app = Windows11Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
