import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QWidget,
)

# Assuming Database.py exists in the same directory as per your original code
from Database import Database

DB_NAME = "rehber.db"


class RehberUygulama(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basit Telefon Rehberi")
        self.resize(400, 500)

        # Initialize Database
        self.db = Database(DB_NAME)

        # Setup Layout
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()

        # --- Ad ---
        layout.addWidget(QLabel("Ad"), 0, 0)
        self.ad_giris = QLineEdit()
        layout.addWidget(self.ad_giris, 0, 1)

        # --- Soyad ---
        layout.addWidget(QLabel("Soyad"), 1, 0)
        self.soyad_giris = QLineEdit()
        layout.addWidget(self.soyad_giris, 1, 1)

        # --- Telefon ---
        layout.addWidget(QLabel("Telefon No"), 2, 0)
        self.tel_giris = QLineEdit()
        layout.addWidget(self.tel_giris, 2, 1)

        # --- Ekle Butonu ---
        self.ekle_btn = QPushButton("Rehbere Ekle")
        self.ekle_btn.clicked.connect(self.kisi_ekle)
        layout.addWidget(self.ekle_btn, 3, 0, 1, 2)  # Span 1 row, 2 cols

        # --- Listele Butonu ---
        self.listele_btn = QPushButton("Kayıtları Göster")
        self.listele_btn.clicked.connect(self.kayitlari_goster)
        layout.addWidget(self.listele_btn, 4, 0, 1, 2)

        # --- Liste Alanı ---
        # Using QTextEdit instead of Label for better scrolling support
        self.liste_alani = QTextEdit()
        self.liste_alani.setReadOnly(True)
        self.liste_alani.setStyleSheet("background-color: #f0f0f0;")
        layout.addWidget(self.liste_alani, 5, 0, 1, 2)

        # --- Silinecek ID ---
        layout.addWidget(QLabel("Silinecek ID"), 6, 0)
        self.sil_giris = QLineEdit()
        layout.addWidget(self.sil_giris, 6, 1)

        # --- Sil Butonu ---
        self.sil_btn = QPushButton("Kişiyi Sil")
        self.sil_btn.clicked.connect(self.kisi_sil)
        layout.addWidget(self.sil_btn, 7, 0, 1, 2)

        # Apply layout to window
        self.setLayout(layout)

    def kisi_ekle(self):
        ad = self.ad_giris.text()
        soyad = self.soyad_giris.text()
        tel = self.tel_giris.text()

        if ad and soyad and tel:
            self.db.kisi_ekle(ad, soyad, tel)

            self.ad_giris.clear()
            self.soyad_giris.clear()
            self.tel_giris.clear()

            QMessageBox.information(self, "Başarılı", "Kişi Rehbere Eklendi!")
            self.kayitlari_goster()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def kayitlari_goster(self):
        kayitlar = self.db.kisileri_getir()

        yazdirilacak_metin = ""
        for kayit in kayitlar:
            # Assuming format: (ID, Ad, Soyad, Tel) based on original logic
            yazdirilacak_metin += (
                f"ID: {kayit[0]} | {kayit[1]} {kayit[2]} | {kayit[3]}\n"
            )

        self.liste_alani.setText(yazdirilacak_metin)

    def kisi_sil(self):
        silinecek_id = self.sil_giris.text()
        if silinecek_id:
            try:
                self.db.kisi_sil(silinecek_id)

                self.sil_giris.clear()
                QMessageBox.information(self, "Başarılı", "Kişi Silindi!")
                self.kayitlari_goster()
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Silme işlemi başarısız: {e}")
        else:
            QMessageBox.critical(self, "Hata", "Lütfen bir ID giriniz.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RehberUygulama()
    window.show()
    sys.exit(app.exec())
