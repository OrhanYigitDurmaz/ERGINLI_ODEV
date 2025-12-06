"""
Comprehensive tests for the Contact Book (Kişi Rehberi) application.

This test suite covers:
- kisi_ekle(): Adding contacts with various edge cases
- kisileri_listele(): Listing contacts with various file states
- kisi_ara(): Searching contacts with various scenarios
- kisi_sil(): Deleting contacts with various edge cases
- menu(): Menu navigation and input handling

Run with: python -m pytest test_main.py -v
Or: python -m unittest test_main -v
"""

import os
import shutil
import tempfile
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

# Import the module to test
import main


class TestBase(unittest.TestCase):
    """Base class for tests with common setup/teardown."""

    def setUp(self):
        """Create a temporary directory and set up test file path."""
        self.test_dir = tempfile.mkdtemp()
        self.original_rehber_file = main.REHBER_FILE
        self.test_rehber_file = os.path.join(self.test_dir, "rehber.txt")
        main.REHBER_FILE = self.test_rehber_file

    def tearDown(self):
        """Clean up temporary directory and restore original file path."""
        main.REHBER_FILE = self.original_rehber_file
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def create_test_file(self, content):
        """Helper to create test file with given content."""
        with open(self.test_rehber_file, "w", encoding="utf-8") as f:
            f.write(content)

    def read_test_file(self):
        """Helper to read test file content."""
        with open(self.test_rehber_file, "r", encoding="utf-8") as f:
            return f.read()


# =============================================================================
# Tests for kisi_ekle() - Add Contact
# =============================================================================


class TestKisiEkle(TestBase):
    """Tests for the kisi_ekle (add contact) function."""

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_valid_contact(self, mock_stdout, mock_input):
        """Test adding a contact with valid inputs."""
        mock_input.side_effect = ["Ali Yılmaz", "555-1234", "ali@test.com"]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz|555-1234|ali@test.com", content)
        self.assertIn("✓ Kişi eklendi!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_empty_name(self, mock_stdout, mock_input):
        """Test that empty name is rejected."""
        mock_input.side_effect = ["", "555-1234", "ali@test.com"]
        main.kisi_ekle()

        self.assertFalse(os.path.exists(self.test_rehber_file))
        self.assertIn("❌ İsim boş olamaz!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_empty_phone(self, mock_stdout, mock_input):
        """Test that empty phone is rejected."""
        mock_input.side_effect = ["Ali Yılmaz", "", "ali@test.com"]
        main.kisi_ekle()

        self.assertFalse(os.path.exists(self.test_rehber_file))
        self.assertIn("❌ Telefon boş olamaz!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_empty_email(self, mock_stdout, mock_input):
        """Test that empty email is rejected."""
        mock_input.side_effect = ["Ali Yılmaz", "555-1234", ""]
        main.kisi_ekle()

        self.assertFalse(os.path.exists(self.test_rehber_file))
        self.assertIn("❌ Email boş olamaz!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_whitespace_only_name(self, mock_stdout, mock_input):
        """Test that whitespace-only name is rejected."""
        mock_input.side_effect = ["   ", "555-1234", "ali@test.com"]
        main.kisi_ekle()

        self.assertFalse(os.path.exists(self.test_rehber_file))
        self.assertIn("❌ İsim boş olamaz!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_pipe_in_name(self, mock_stdout, mock_input):
        """Test that pipe character is stripped from name."""
        mock_input.side_effect = ["Ali|Veli", "555-1234", "ali@test.com"]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("AliVeli|555-1234|ali@test.com", content)
        self.assertNotIn("Ali|Veli|", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_pipe_in_phone(self, mock_stdout, mock_input):
        """Test that pipe character is stripped from phone."""
        mock_input.side_effect = ["Ali Yılmaz", "555|1234", "ali@test.com"]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz|5551234|ali@test.com", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_pipe_in_email(self, mock_stdout, mock_input):
        """Test that pipe character is stripped from email."""
        mock_input.side_effect = ["Ali Yılmaz", "555-1234", "ali|test@test.com"]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz|555-1234|alitest@test.com", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_turkish_characters(self, mock_stdout, mock_input):
        """Test adding contact with Turkish characters."""
        mock_input.side_effect = ["Şükrü Öztürk", "555-1234", "sukru@test.com"]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("Şükrü Öztürk|555-1234|sukru@test.com", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_special_characters(self, mock_stdout, mock_input):
        """Test adding contact with special characters (except pipe)."""
        mock_input.side_effect = [
            "Ali 'The Best' Yılmaz",
            "+90 (555) 123-45-67",
            "ali.yilmaz@test.co.uk",
        ]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn(
            "Ali 'The Best' Yılmaz|+90 (555) 123-45-67|ali.yilmaz@test.co.uk", content
        )

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_multiple_contacts(self, mock_stdout, mock_input):
        """Test adding multiple contacts sequentially."""
        mock_input.side_effect = [
            "Ali Yılmaz",
            "555-1111",
            "ali@test.com",
            "Veli Kaya",
            "555-2222",
            "veli@test.com",
        ]
        main.kisi_ekle()
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz|555-1111|ali@test.com", content)
        self.assertIn("Veli Kaya|555-2222|veli@test.com", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_strips_whitespace(self, mock_stdout, mock_input):
        """Test that leading/trailing whitespace is stripped."""
        mock_input.side_effect = ["  Ali Yılmaz  ", "  555-1234  ", "  ali@test.com  "]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz|555-1234|ali@test.com", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_contact_only_pipe_in_name(self, mock_stdout, mock_input):
        """Test that name with only pipe character is rejected as empty."""
        mock_input.side_effect = ["|", "555-1234", "ali@test.com"]
        main.kisi_ekle()

        self.assertFalse(os.path.exists(self.test_rehber_file))
        self.assertIn("❌ İsim boş olamaz!", mock_stdout.getvalue())


# =============================================================================
# Tests for kisileri_listele() - List Contacts
# =============================================================================


class TestKisileriListele(TestBase):
    """Tests for the kisileri_listele (list contacts) function."""

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_valid_contacts(self, mock_stdout):
        """Test listing valid contacts."""
        self.create_test_file(
            "Ali|555-1111|ali@test.com\nVeli|555-2222|veli@test.com\n"
        )
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("Ali", output)
        self.assertIn("555-1111", output)
        self.assertIn("ali@test.com", output)
        self.assertIn("Veli", output)
        self.assertIn("555-2222", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_empty_file(self, mock_stdout):
        """Test listing when file is empty."""
        self.create_test_file("")
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("Rehber boş.", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_file_not_exists(self, mock_stdout):
        """Test listing when file doesn't exist."""
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("Henüz kayıtlı kişi yok.", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_file_with_empty_lines(self, mock_stdout):
        """Test listing file with empty lines mixed in."""
        self.create_test_file(
            "Ali|555-1111|ali@test.com\n\n\nVeli|555-2222|veli@test.com\n"
        )
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("Ali", output)
        self.assertIn("Veli", output)
        self.assertNotIn("Rehber boş", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_file_only_whitespace_lines(self, mock_stdout):
        """Test listing file with only whitespace lines."""
        self.create_test_file("   \n\n   \n")
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("Rehber boş.", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_malformed_data_too_few_fields(self, mock_stdout):
        """Test listing with malformed data (too few fields)."""
        self.create_test_file("Ali|555-1111\n")
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("[HATALI VERİ]", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_malformed_data_too_many_fields(self, mock_stdout):
        """Test listing with malformed data (too many fields)."""
        self.create_test_file("Ali|555-1111|ali@test.com|extra\n")
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("[HATALI VERİ]", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_mixed_valid_and_malformed(self, mock_stdout):
        """Test listing with both valid and malformed entries."""
        self.create_test_file(
            "Ali|555-1111|ali@test.com\nBAD_DATA\nVeli|555-2222|veli@test.com\n"
        )
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("Ali", output)
        self.assertIn("Veli", output)
        self.assertIn("[HATALI VERİ]", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_turkish_characters(self, mock_stdout):
        """Test listing contacts with Turkish characters."""
        self.create_test_file("Şükrü Öztürk|555-1111|sukru@test.com\n")
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("Şükrü Öztürk", output)


# =============================================================================
# Tests for kisi_ara() - Search Contact
# =============================================================================


class TestKisiAra(TestBase):
    """Tests for the kisi_ara (search contact) function."""

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_found_exact_match(self, mock_stdout, mock_input):
        """Test searching with exact name match."""
        self.create_test_file(
            "Ali Yılmaz|555-1111|ali@test.com\nVeli Kaya|555-2222|veli@test.com\n"
        )
        mock_input.return_value = "Ali Yılmaz"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Ali Yılmaz", output)
        self.assertIn("555-1111", output)
        self.assertNotIn("Kişi bulunamadı!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_found_partial_match(self, mock_stdout, mock_input):
        """Test searching with partial name match."""
        self.create_test_file(
            "Ali Yılmaz|555-1111|ali@test.com\nVeli Kaya|555-2222|veli@test.com\n"
        )
        mock_input.return_value = "Ali"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Ali Yılmaz", output)
        self.assertIn("555-1111", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_case_insensitive(self, mock_stdout, mock_input):
        """Test that search is case-insensitive."""
        self.create_test_file("Mehmet Kaya|555-1111|mehmet@test.com\n")
        mock_input.return_value = "MEHMET KAYA"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Mehmet Kaya", output)
        self.assertNotIn("Kişi bulunamadı!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_case_insensitive_turkish_i(self, mock_stdout, mock_input):
        """Test that search is case-insensitive with Turkish İ/i characters."""
        self.create_test_file("İbrahim Çelik|555-1111|ibrahim@test.com\n")
        mock_input.return_value = "İBRAHİM"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("İbrahim Çelik", output)
        self.assertNotIn("Kişi bulunamadı!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_case_insensitive_turkish_dotless_i(self, mock_stdout, mock_input):
        """Test that search is case-insensitive with Turkish I/ı characters."""
        self.create_test_file("Işık Yıldız|555-1111|isik@test.com\n")
        mock_input.return_value = "IŞIK"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Işık Yıldız", output)
        self.assertNotIn("Kişi bulunamadı!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_not_found(self, mock_stdout, mock_input):
        """Test searching for non-existent contact."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "Mehmet"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Kişi bulunamadı!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_empty_term(self, mock_stdout, mock_input):
        """Test that empty search term is rejected."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = ""
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("❌ Arama terimi boş olamaz!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_whitespace_only_term(self, mock_stdout, mock_input):
        """Test that whitespace-only search term is rejected."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "   "
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("❌ Arama terimi boş olamaz!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_file_not_exists(self, mock_stdout, mock_input):
        """Test searching when file doesn't exist."""
        mock_input.return_value = "Ali"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Henüz kayıtlı kişi yok.", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_multiple_matches(self, mock_stdout, mock_input):
        """Test searching returns multiple matches."""
        self.create_test_file(
            "Ali Yılmaz|555-1111|ali@test.com\nAli Kaya|555-2222|alik@test.com\nVeli|555-3333|veli@test.com\n"
        )
        mock_input.return_value = "Ali"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Ali Yılmaz", output)
        self.assertIn("Ali Kaya", output)
        self.assertNotIn("Veli", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_skips_malformed_data(self, mock_stdout, mock_input):
        """Test that search skips malformed data without crashing."""
        self.create_test_file(
            "Ali Yılmaz|555-1111|ali@test.com\nBAD_DATA\nAli Kaya|555-2222|alik@test.com\n"
        )
        mock_input.return_value = "Ali"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Ali Yılmaz", output)
        self.assertIn("Ali Kaya", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_turkish_characters(self, mock_stdout, mock_input):
        """Test searching with Turkish characters."""
        self.create_test_file("Şükrü Öztürk|555-1111|sukru@test.com\n")
        mock_input.return_value = "şükrü"
        main.kisi_ara()

        output = mock_stdout.getvalue()
        self.assertIn("Şükrü Öztürk", output)


# =============================================================================
# Tests for kisi_sil() - Delete Contact
# =============================================================================


class TestKisiSil(TestBase):
    """Tests for the kisi_sil (delete contact) function."""

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_valid_contact(self, mock_stdout, mock_input):
        """Test deleting a valid contact."""
        self.create_test_file(
            "Ali Yılmaz|555-1111|ali@test.com\nVeli Kaya|555-2222|veli@test.com\n"
        )
        mock_input.return_value = "1"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertNotIn("Ali Yılmaz", content)
        self.assertIn("Veli Kaya", content)
        self.assertIn("✓ Ali Yılmaz silindi!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_last_contact(self, mock_stdout, mock_input):
        """Test deleting the last remaining contact."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "1"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertEqual(content, "")
        self.assertIn("✓ Ali Yılmaz silindi!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_middle_contact(self, mock_stdout, mock_input):
        """Test deleting a contact from the middle of the list."""
        self.create_test_file(
            "Ali|555-1111|ali@test.com\nVeli|555-2222|veli@test.com\nCan|555-3333|can@test.com\n"
        )
        mock_input.return_value = "2"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali", content)
        self.assertNotIn("Veli", content)
        self.assertIn("Can", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_invalid_number_too_high(self, mock_stdout, mock_input):
        """Test deleting with number higher than available contacts."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "5"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz", content)
        self.assertIn("Geçersiz numara!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_invalid_number_zero(self, mock_stdout, mock_input):
        """Test deleting with number zero."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "0"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz", content)
        self.assertIn("Geçersiz numara!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_invalid_number_negative(self, mock_stdout, mock_input):
        """Test deleting with negative number."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "-1"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz", content)
        self.assertIn("Geçersiz numara!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_non_numeric_input(self, mock_stdout, mock_input):
        """Test deleting with non-numeric input."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "abc"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz", content)
        self.assertIn("Lütfen geçerli bir numara gir!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_empty_input(self, mock_stdout, mock_input):
        """Test deleting with empty input."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = ""
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz", content)
        self.assertIn("❌ Numara boş olamaz!", mock_stdout.getvalue())

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_whitespace_input(self, mock_stdout, mock_input):
        """Test deleting with whitespace-only input."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "   "
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz", content)
        self.assertIn("❌ Numara boş olamaz!", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_file_not_exists(self, mock_stdout):
        """Test deleting when file doesn't exist."""
        main.kisi_sil()

        output = mock_stdout.getvalue()
        self.assertIn("Henüz kayıtlı kişi yok.", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_empty_file(self, mock_stdout):
        """Test deleting from empty file."""
        self.create_test_file("")
        main.kisi_sil()

        output = mock_stdout.getvalue()
        self.assertIn("Rehber zaten boş.", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_with_malformed_data(self, mock_stdout, mock_input):
        """Test deleting from file with malformed data."""
        self.create_test_file(
            "Ali|555-1111|ali@test.com\nBAD_DATA\nVeli|555-2222|veli@test.com\n"
        )
        mock_input.return_value = "1"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertNotIn("Ali|555-1111", content)
        # BAD_DATA and Veli should still be there
        self.assertIn("BAD_DATA", content)
        self.assertIn("Veli", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_float_input(self, mock_stdout, mock_input):
        """Test deleting with float input."""
        self.create_test_file("Ali Yılmaz|555-1111|ali@test.com\n")
        mock_input.return_value = "1.5"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Ali Yılmaz", content)
        self.assertIn("Lütfen geçerli bir numara gir!", mock_stdout.getvalue())


# =============================================================================
# Tests for menu() - Main Menu
# =============================================================================


class TestMenu(TestBase):
    """Tests for the menu function."""

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_exit(self, mock_stdout, mock_input):
        """Test exiting the menu."""
        mock_input.return_value = "5"
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("Görüşürüz!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_invalid_choice(self, mock_stdout, mock_input):
        """Test invalid menu choice."""
        mock_input.side_effect = ["9", "5"]
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("Geçersiz seçim!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_empty_choice(self, mock_stdout, mock_input):
        """Test empty menu choice."""
        mock_input.side_effect = ["", "5"]
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("Geçersiz seçim!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_calls_kisi_ekle(self, mock_stdout, mock_input):
        """Test that menu option 1 calls kisi_ekle."""
        mock_input.side_effect = ["1", "Ali", "555-1234", "ali@test.com", "5"]
        main.menu()

        content = self.read_test_file()
        self.assertIn("Ali|555-1234|ali@test.com", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_calls_kisileri_listele(self, mock_stdout, mock_input):
        """Test that menu option 2 calls kisileri_listele."""
        self.create_test_file("Ali|555-1234|ali@test.com\n")
        mock_input.side_effect = ["2", "5"]
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("Ali", output)
        self.assertIn("555-1234", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_calls_kisi_ara(self, mock_stdout, mock_input):
        """Test that menu option 3 calls kisi_ara."""
        self.create_test_file("Ali|555-1234|ali@test.com\n")
        mock_input.side_effect = ["3", "Ali", "5"]
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("İsim: Ali", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_calls_kisi_sil(self, mock_stdout, mock_input):
        """Test that menu option 4 calls kisi_sil."""
        self.create_test_file("Ali|555-1234|ali@test.com\n")
        mock_input.side_effect = ["4", "1", "5"]
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("✓ Ali silindi!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_displays_header(self, mock_stdout, mock_input):
        """Test that menu displays the header."""
        mock_input.return_value = "5"
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("KİŞİ REHBERİ UYGULAMASI", output)
        self.assertIn("1. Kişi Ekle", output)
        self.assertIn("2. Kişileri Listele", output)
        self.assertIn("3. Kişi Ara", output)
        self.assertIn("4. Kişi Sil", output)
        self.assertIn("5. Çıkış", output)


# =============================================================================
# Integration Tests
# =============================================================================


class TestIntegration(TestBase):
    """Integration tests for the full workflow."""

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_full_workflow_add_list_search_delete(self, mock_stdout, mock_input):
        """Test full workflow: add -> list -> search -> delete."""
        mock_input.side_effect = [
            "1",  # Menu: Add contact
            "Ali Yılmaz",
            "555-1234",
            "ali@test.com",  # Contact details
            "1",  # Menu: Add another contact
            "Veli Kaya",
            "555-5678",
            "veli@test.com",  # Contact details
            "2",  # Menu: List contacts
            "3",  # Menu: Search contact
            "Ali",  # Search term
            "4",  # Menu: Delete contact
            "1",  # Delete first contact
            "2",  # Menu: List contacts (verify deletion)
            "5",  # Menu: Exit
        ]
        main.menu()

        output = mock_stdout.getvalue()
        # Verify both contacts were added
        self.assertIn("✓ Kişi eklendi!", output)
        # Verify search found Ali
        self.assertIn("İsim: Ali Yılmaz", output)
        # Verify Ali was deleted
        self.assertIn("✓ Ali Yılmaz silindi!", output)

        # Verify final state of file
        content = self.read_test_file()
        self.assertNotIn("Ali Yılmaz", content)
        self.assertIn("Veli Kaya", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_search_with_special_characters(self, mock_stdout, mock_input):
        """Test adding and searching contact with special Turkish characters."""
        mock_input.side_effect = [
            "1",  # Menu: Add contact
            "Şükrü Öztürk",
            "555-1234",
            "sukru@test.com",  # Contact with Turkish chars
            "3",  # Menu: Search
            "şükrü",  # Search term (lowercase)
            "5",  # Exit
        ]
        main.menu()

        output = mock_stdout.getvalue()
        self.assertIn("Şükrü Öztürk", output)
        self.assertNotIn("Kişi bulunamadı!", output)


# =============================================================================
# Edge Case Tests
# =============================================================================


class TestEdgeCases(TestBase):
    """Tests for various edge cases."""

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_very_long_input(self, mock_stdout, mock_input):
        """Test handling very long input strings."""
        long_name = "A" * 1000
        long_phone = "5" * 100
        long_email = "a" * 500 + "@test.com"
        mock_input.side_effect = [long_name, long_phone, long_email]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn(long_name, content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_unicode_emoji_in_input(self, mock_stdout, mock_input):
        """Test handling emoji in input."""
        mock_input.side_effect = ["Ali 😀", "555-1234", "ali@test.com"]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertIn("Ali 😀", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_newline_characters_stripped(self, mock_stdout, mock_input):
        """Test that newline characters in input don't break the format."""
        # strip() should handle this
        mock_input.side_effect = ["Ali\n", "555-1234\n", "ali@test.com\n"]
        main.kisi_ekle()

        content = self.read_test_file()
        lines = [l for l in content.split("\n") if l.strip()]
        self.assertEqual(len(lines), 1)  # Should be only one line

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_single_field_entry(self, mock_stdout):
        """Test listing entry with only one field (no pipes)."""
        self.create_test_file("OnlyName\n")
        main.kisileri_listele()

        output = mock_stdout.getvalue()
        self.assertIn("[HATALI VERİ]", output)
        self.assertIn("OnlyName", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_preserves_file_encoding(self, mock_stdout, mock_input):
        """Test that delete operation preserves UTF-8 encoding."""
        self.create_test_file(
            "Şükrü|555-1111|sukru@test.com\nÖzlem|555-2222|ozlem@test.com\n"
        )
        mock_input.return_value = "1"
        main.kisi_sil()

        content = self.read_test_file()
        self.assertIn("Özlem", content)
        self.assertNotIn("Şükrü", content)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_multiple_pipes_in_all_fields(self, mock_stdout, mock_input):
        """Test that multiple pipe characters are all removed."""
        mock_input.side_effect = ["A|l|i", "5|5|5", "a|@|t.com"]
        main.kisi_ekle()

        content = self.read_test_file()
        self.assertEqual(content.count("|"), 2)  # Only the delimiters


if __name__ == "__main__":
    unittest.main(verbosity=2)
