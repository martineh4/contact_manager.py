# test_contact_manager.py

import unittest
import contact_manager
from contact_manager import DuplicateContactError


class TestContactManager(unittest.TestCase):
    def setUp(self):
        """Clear contacts before each test."""
        contact_manager.contacts.clear()

    def test_add_contact(self):
        """Test adding a new contact."""
        result = contact_manager.add_contact("Hannah", "111")
        self.assertEqual(result, "Added Hannah to contacts.")
        self.assertIn("Hannah", contact_manager.contacts)

    def test_add_duplicate_contact(self):
        """Test adding a duplicate contact raises DuplicateContactError."""
        contact_manager.add_contact("Kaleb", "222")
        with self.assertRaises(DuplicateContactError):
            contact_manager.add_contact("Kaleb", "333")

    def test_find_existing_contact(self):
        """Test finding an existing contact returns the correct phone number."""
        contact_manager.add_contact("Layla", "444")
        result = contact_manager.find_contact("Layla")
        self.assertEqual(result, "444")

    def test_find_nonexistent_contact(self):
        """Test finding a non-existent contact returns None."""
        result = contact_manager.find_contact("DoesNotExist")
        self.assertIsNone(result)

    def test_delete_existing_contact(self):
        """Test deleting an existing contact."""
        contact_manager.add_contact("Beth", "555")
        result = contact_manager.delete_contact("Beth")
        self.assertEqual(result, "Deleted Beth.")
        self.assertNotIn("Beth", contact_manager.contacts)

    def test_delete_nonexistent_contact(self):
        """Test deleting a non-existent contact returns None."""
        result = contact_manager.delete_contact("Ryan")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
