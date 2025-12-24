import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.geometry("300x200")
root.title("DOSYA OKUMA")

dosyaadi = tk.StringVar()


content = ttk.Frame(root, padding="10")
content.grid(row=0, column=0, sticky="nsew")


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


namelbl1 = ttk.Label(content, text="Dosya Adı:")
namelbl1.grid(row=0, column=0, sticky="w", padx=(0, 5), pady=5)

dosya_entry = ttk.Entry(content, textvariable=dosyaadi, width=50)
dosya_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)


def dosya_oku():
    """Dosyayı oku ve içeriği göster"""
    dosya_yolu = dosyaadi.get().strip()

    if not dosya_yolu:
        messagebox.showwarning("Uyarı", "Lütfen bir dosya adı girin!")
        return

    try:
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            icerik_text.delete("1.0", "end")
            icerik_text.insert("1.0", icerik)
    except Exception as e:
        messagebox.showerror("hata", f"hata cıktı: {str(e)}")


oku_button = ttk.Button(content, text="Oku", default="active", command=dosya_oku)
oku_button.grid(row=0, column=3, padx=5, pady=5)


icerik_label = ttk.Label(content, text="Okunan İçerik:")
icerik_label.grid(row=1, column=0, rowspan=3, sticky="w", pady=(10, 5))


icerik_text = tk.Text(content, wrap="word")
icerik_text.grid(row=2, column=1, columnspan=3, sticky="nsew", pady=5)

content.columnconfigure(1, weight=1)
content.rowconfigure(2, weight=1)


root.mainloop()
