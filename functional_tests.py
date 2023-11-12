from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def create_entry_in_list(self, entry_text):
        # She is invited to enter a to-do item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        inputbox.send_keys(entry_text)

        # When she hits enter, the page updates, and now the page lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is typing fly-fishing lures)
        self.create_entry_in_list("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # 1: "Buy peacock feathers" as an item in a to-do list
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.create_entry_in_list("Use peacock feathers to make a fly")

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main()
