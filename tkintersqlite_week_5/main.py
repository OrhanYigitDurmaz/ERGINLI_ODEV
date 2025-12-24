import tkinter as tk
from tkinter import messagebox

from Database import Database

DB_NAME = "rehber.db"


class RehberUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Basit Telefon Rehberi")
        self.root.geometry("400x500")

        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(5, weight=1)

        self.db = Database(DB_NAME)

        # Ad
        tk.Label(root, text="Ad").grid(row=0, column=0, pady=5, sticky="w", padx=10)
        self.ad_giris = tk.Entry(root)
        self.ad_giris.grid(row=0, column=1, padx=10, sticky="ew")

        # Soyad
        tk.Label(root, text="Soyad").grid(row=1, column=0, pady=5, sticky="w", padx=10)
        self.soyad_giris = tk.Entry(root)
        self.soyad_giris.grid(row=1, column=1, padx=10, sticky="ew")

        # Telefon
        tk.Label(root, text="Telefon No").grid(
            row=2, column=0, pady=5, sticky="w", padx=10
        )
        self.tel_giris = tk.Entry(root)
        self.tel_giris.grid(row=2, column=1, padx=10, sticky="ew")

        self.ekle_btn = tk.Button(
            root, text="Rehbere Ekle", command=self.kisi_ekle_arayuz
        )

        self.ekle_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.listele_btn = tk.Button(
            root, text="Kayıtları Göster", command=self.kayitlari_goster_arayuz
        )
        self.listele_btn.grid(
            row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew"
        )

        self.liste_etiketi = tk.Label(
            root, text="", justify=tk.LEFT, anchor="nw", bg="#f0f0f0", relief="sunken"
        )
        self.liste_etiketi.grid(row=5, column=0, columnspan=2, padx=10, sticky="nsew")

        # --- Silme Bölümü ---
        tk.Label(root, text="Silinecek ID").grid(
            row=6, column=0, pady=5, sticky="w", padx=10
        )
        self.sil_giris = tk.Entry(root)
        self.sil_giris.grid(row=6, column=1, padx=10, sticky="ew")

        self.sil_btn = tk.Button(root, text="Kişiyi Sil", command=self.kisi_sil_arayuz)
        self.sil_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    def kisi_ekle_arayuz(self):
        ad = self.ad_giris.get()
        soyad = self.soyad_giris.get()
        tel = self.tel_giris.get()

        if ad and soyad and tel:
            self.db.kisi_ekle(ad, soyad, tel)

            self.ad_giris.delete(0, tk.END)
            self.soyad_giris.delete(0, tk.END)
            self.tel_giris.delete(0, tk.END)
            messagebox.showinfo("Başarılı", "Kişi Rehbere Eklendi!")
        else:
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun.")

    def kayitlari_goster_arayuz(self):
        kayitlar = self.db.kisileri_getir()

        yazdirilacak_metin = ""
        for kayit in kayitlar:
            yazdirilacak_metin += (
                f"ID: {kayit[0]} | {kayit[1]} {kayit[2]} | {kayit[3]}\n"
            )

        self.liste_etiketi.config(text=yazdirilacak_metin)

    def kisi_sil_arayuz(self):
        silinecek_id = self.sil_giris.get()
        if silinecek_id:
            try:
                self.db.kisi_sil(silinecek_id)

                self.sil_giris.delete(0, tk.END)
                messagebox.showinfo("Başarılı", "Kişi Silindi!")
                self.kayitlari_goster_arayuz()
            except Exception as e:
                messagebox.showerror("Hata", f"Silme işlemi başarısız: {e}")
        else:
            messagebox.showerror("Hata", "Lütfen bir ID giriniz.")


if __name__ == "__main__":
    root = tk.Tk()
    uygulama = RehberUygulamasi(root)
    root.mainloop()
